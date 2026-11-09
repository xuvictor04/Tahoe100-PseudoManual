---
symbol: "SMARCD2"
type: "gene"
col: 2977
ensembl_id: "ENSG00000108604"
name: "SWI/SNF related BAF chromatin remodeling complex subunit D2"
location: "17q23.3"
module: 11
arm: "-"
pooled_cpm: 20.55
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SMARCD2

*SWI/SNF related BAF chromatin remodeling complex subunit D2* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +12.1, q 5e-31, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.523× (z -13.1, q 1e-36, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD81]] (+0.71, fdr 7e-06), [[WDR5]] (+0.65, fdr 1e-05), [[RPA1]] (+0.65, fdr 1e-05); moves opposite to [[UBXN4]] (-0.68, fdr 1e-05), [[NEPRO-AS1]] (-0.68, fdr 1e-05), [[THAP5]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +12.1 | 5e-31 | 39/47 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.20×** | +11.5 | 4e-28 | 37/42 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.13×** | +11.1 | 4e-26 | 41/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.97×** | +9.9 | 8e-21 | 40/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.01×** | +9.8 | 1e-20 | 29/33 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.82×** | +8.8 | 2e-16 | 38/47 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.51×** | +6.0 | 2e-07 | 31/43 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.56×** | +5.9 | 3e-07 | 24/38 (HT-29, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +5.1 | 2e-05 | 27/46 (Panc 03.27, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +4.8 | 1e-04 | 24/46 (SK-MEL-2, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.39×** | +4.6 | 2e-04 | 26/44 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.004 | 9/47 (NCI-H460, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.29×** | +3.8 | 0.007 | 20/46 (KATO III, LS 180, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.30×** | +3.7 | 0.008 | 20/46 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.30×** | +3.7 | 0.008 | 19/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.027 | 10/45 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.093 | 8/47 (NCI-H460, CFPAC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2977.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.523×** | -13.1 | 1e-36 | 40/47 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.477×** | -9.1 | 4e-17 | 32/45 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.705×** | -4.9 | 2e-04 | 24/46 (NCI-H23, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.3 | 0.12 | 3/48 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.811× | -3.0 | 0.28 | 15/47 (A-427, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.1 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +11.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.49× (z +9.4) ⚠ cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.4) |
| [[A-172 (line)]] | wt | 19.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 34.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -8.7) |
| [[LoVo (line)]] | wt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 21.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 15.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -10.4) |
| [[PANC-1 (line)]] | alt | 14.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.2) |
| [[A-427 (line)]] | wt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.5) |
| [[A498 (line)]] | wt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A549 (line)]] | wt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0993× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0793× (z -9.0) |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.175× (z -9.3) |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -13.5) |
| [[HS-578T (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -8.7) |
| [[HT-29 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.9) |
| [[J82 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.6) |
| [[KATO III (line)]] | alt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.0) |
| [[RKO (line)]] | wt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -10.9) |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD81]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[WDR5]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[RPA1]] | +0.65 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD13D]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[GIT1]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[AP2A1]] | +0.64 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[POLR2F]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[SETD3]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[DHPS]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PIGF]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.62 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN4]] | -0.68 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.68 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[THAP5]] | -0.67 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.67 | -0.71 / -0.49 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.66 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[LZIC]] | -0.66 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[TRIP11]] | -0.65 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[ARL14EP]] | -0.65 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[METTL18]] | -0.65 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.64 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[SNRNP27]] | -0.64 | -0.77 / -0.37 | both halves | 8e-05 |  |
| [[NSRP1]] | -0.64 | -0.69 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.3, 8.8); signed map (-46.9, -4.2). **Vector** length 83.2, 18.7% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +12.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.7 | +9.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.6 | +8.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | +3.5 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +5.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +4.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.1 | -13.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,832,081-63,843,065 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAF60B, Rsc6p, CRACD2, PRO2451 |
| Gene groups (HGNC) | BAF complex subunits; PBAF complex subunits; GBAF complex subunits |
| Reactome | 21 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the polybromo-BAF (pBAF) complex; Formation of the embryonic stem cell BAF (esBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92925](https://www.uniprot.org/uniprotkb/Q92925) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily D member 2):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Critical regulator of myeloid differentiation, controlling granulocytopoiesis and the expression of genes involved in neutrophil granule formation.

**Summary**, from NCBI Gene [6603](https://www.ncbi.nlm.nih.gov/gene/6603):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and has sequence similarity to the yeast Swp73 protein. Alternatively spliced transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:11107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11107) · Entrez [6603](https://www.ncbi.nlm.nih.gov/gene/6603) · UniProt [Q92925](https://www.uniprot.org/uniprotkb/Q92925) · Ensembl [ENSG00000108604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108604)

## Data

Gene col 2977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2977); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2977]; `tensor/DDL_lfc|DDL_z.npy` [2977]; `embed/gene_vectors.npy` [2977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2977 or target_col == 2977). Every well: [[SMARCD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
