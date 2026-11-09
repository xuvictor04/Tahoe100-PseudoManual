---
symbol: "RYR2"
type: "gene"
col: 12631
ensembl_id: "ENSG00000198626"
name: "ryanodine receptor 2"
location: "1q43"
module: 75
arm: "+"
pooled_cpm: 24.05
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# RYR2

*ryanodine receptor 2* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.31× (z +16.9, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[IQ 1 (drug)]] 0.05 µM: 0.607× (z -4.7, q 0.001, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (C32 0.0772×; ⚠ transcription drop); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0650×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.0826×); [[Megestrol (drug)]] 0.5 µM in 1 line (COLO 205 0.0618×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CROCC]] (+0.72, fdr 1e-05), [[AP1G2-AS1]] (+0.71, fdr 7e-06), [[TTN]] (+0.67, fdr 7e-06); moves opposite to [[ISCA2]] (-0.60, fdr 5e-04), [[PET117]] (-0.58, fdr 3e-04), [[POP7]] (-0.57, fdr 2e-04).
> It is in [[Module 075]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12631.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.31×** | +16.9 | 0e+00 | 39/47 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +14.3 | 1e-43 | 39/46 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.03×** | +13.9 | 1e-41 | 31/38 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +11.0 | 8e-26 | 28/32 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.92×** | +10.7 | 1e-24 | 37/46 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.1 | 5e-22 | 24/27 (AsPC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.4 | 7e-06 | 20/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 4e-04 | 23/47 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.5 | 4e-04 | 18/46 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 4e-04 | 15/47 (PANC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.2 | 0.002 | 18/44 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.002 | 16/46 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.006 | 16/47 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +3.7 | 0.009 | 12/48 (NCI-H2030, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Delamanid (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.012 | 9/48 (NCI-H1792, SW480, …) | all doses, flat | position effect removed |
| [[Cepharanthine (drug)]] 0.05 µM |  | **1.47×** | +3.6 | 0.013 | 8/48 (NCI-H2030, LS 180, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.018 | 11/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.028 | 10/47 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Esmolol (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.030 | 10/48 (NCI-H1792, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Malotilate (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.035 | 7/46 (A549, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12631.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (C32 0.0772×; ⚠ transcription drop); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0650×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.0826×); [[Megestrol (drug)]] 0.5 µM in 1 line (COLO 205 0.0618×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[IQ 1 (drug)]] 0.05 µM |  | **0.607×** | -4.7 | 0.001 | 18/48 (KATO III, NCI-H460, …) | all doses, flat | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -3.8 | 0.040 | 14/46 (A-172, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | 0.696× | -3.5 | 0.11 | 16/47 (A498, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.714× | -3.2 | 0.19 | 17/46 (NCI-H1573, A498, …) | inconsistent across doses | position effect removed |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.737× | -3.1 | 0.21 | 11/45 (SW48, LS 180, …) | inconsistent across doses | position effect removed |
| [[4EGI-1 (drug)]] 0.05 µM |  | 0.725× | -3.1 | 0.21 | 10/48 (LoVo, SW 1271, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 17.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +12.0) | — |
| [[LoVo (line)]] | wt | 10.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +10.5) | — |
| [[SW480 (line)]] | alt | 9.99 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +10.9) | — |
| [[A-427 (line)]] | wt | 10.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.72× (z +9.1) | — |
| [[A549 (line)]] | wt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +11.7) | — |
| [[C32 (line)]] | wt | 13.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +14.3) | [[Pimozide (drug)]] 0.5 µM 0.0772× (z -10.6) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 12.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.49× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.7× (z +19.0) | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +12.6) | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0650× (z -9.1) |
| [[A-172 (line)]] | wt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 9.44 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.2× (z +8.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 9.17 | 0 | 1 | — | [[Megestrol (drug)]] 0.5 µM 0.0618× (z -8.5) |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0826× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 8.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.50× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 213 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 18.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +9.3) | — |
| [[SW48 (line)]] | wt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +11.2) | — |
| [[A498 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCC]] | +0.72 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[AP1G2-AS1]] | +0.71 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TTN]] | +0.67 | +0.63 / +0.59 | both halves | 7e-06 | pathway: Muscle contraction; STRING 774 |
| [[LHFPL3]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[THSD7B]] | +0.64 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[LINC01090]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TPTE2P6]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[DPP6]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 | same gene group |
| [[DLGAP1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[RMRP]] | +0.61 | +0.37 / +0.62 | both halves | 7e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | -0.60 | -0.24 / -0.61 | both halves | 5e-04 |  |
| [[PET117]] | -0.58 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[POP7]] | -0.57 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ZDHHC12]] | -0.56 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[PUSL1]] | -0.56 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[CPTP]] | -0.55 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[NOA1]] | -0.55 | -0.16 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[SAC3D1]] | -0.55 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[SDHAF1]] | -0.55 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[DCTPP1]] | -0.54 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[AURKAIP1]] | -0.54 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[WRAP73]] | -0.53 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[TMEM147]] | -0.53 | -0.49 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.6, 23.2); signed map (32.6, -20.0). **Vector** length 78.6, 13.9% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.2 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.0 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.9 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.2 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.1 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.8 | -0.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Thymol (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ryanodine receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:237,042,184-237,833,988 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARVC2, VTSIP; previously ARVD2 |
| Gene groups (HGNC) | Ryanodine receptors; EF-hand domain containing; Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 6 pathways, smallest: Ion homeostasis; Stimuli-sensing channels; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92736](https://www.uniprot.org/uniprotkb/Q92736) (Ryanodine receptor 2):

> Cytosolic calcium-activated calcium channel that mediates the release of Ca(2+) from the sarcoplasmic reticulum into the cytosol and thereby plays a key role in triggering cardiac muscle contraction. Aberrant channel activation can lead to cardiac arrhythmia. In cardiac myocytes, calcium release is triggered by increased Ca(2+) cytosolic levels due to activation of the L-type calcium channel CACNA1C. The calcium channel activity is modulated by formation of heterotetramers with RYR3. Required …

**Summary**, from NCBI Gene [6262](https://www.ncbi.nlm.nih.gov/gene/6262):

> This gene encodes a ryanodine receptor found in cardiac muscle sarcoplasmic reticulum. The encoded protein is one of the components of a calcium channel, composed of a tetramer of the ryanodine receptor proteins and a tetramer of FK506 binding protein 1B proteins, that supplies calcium to cardiac muscle. Mutations in this gene are associated with stress-induced polymorphic ventricular tachycardia and arrhythmogenic right ventricular dysplasia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10484) · Entrez [6262](https://www.ncbi.nlm.nih.gov/gene/6262) · UniProt [Q92736](https://www.uniprot.org/uniprotkb/Q92736) · Ensembl [ENSG00000198626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198626)

## Data

Gene col 12631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12631); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12631]; `tensor/DDL_lfc|DDL_z.npy` [12631]; `embed/gene_vectors.npy` [12631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12631 or target_col == 12631). Every well: [[RYR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RYR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
