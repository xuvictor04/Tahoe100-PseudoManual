---
symbol: "SNAPC4"
type: "gene"
col: 9166
ensembl_id: "ENSG00000165684"
name: "small nuclear RNA activating complex polypeptide 4"
location: "9q34.3"
module: 1
arm: "+"
pooled_cpm: 17.77
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SNAPC4

*small nuclear RNA activating complex polypeptide 4* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.85× (z +27.1, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Thymol (drug)]] 5 µM: 0.826× (z -3.9, q 0.035, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (AN3 CA 0.0527×, RPMI-7951 0.172×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.133×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (COLO 205 0.0719×); [[Silodosin (drug)]] 5 µM in 1 line (SHP-77 0.207×); [[Isocorydine (drug)]] 0.5 µM in 1 line (Hs 766T 0.212×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRD9]] (+0.59, fdr 1e-05), [[CLUH]] (+0.59, fdr 1e-05), [[DDX51]] (+0.58, fdr 1e-05); moves opposite to [[PLEKHA5]] (-0.54, fdr 5e-05), [[SDAD1P1]] (-0.48, fdr 6e-04), [[NEK7]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.85×** | +27.1 | 0e+00 | 46/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.88×** | +19.3 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.46×** | +17.6 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.74×** | +14.3 | 3e-44 | 43/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.73×** | +13.7 | 9e-41 | 41/46 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.62×** | +13.7 | 1e-40 | 47/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +9.5 | 2e-19 | 34/46 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +8.6 | 8e-16 | 38/48 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.69×** | +7.1 | 7e-11 | 32/44 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.76×** | +7.0 | 1e-10 | 33/47 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +6.9 | 2e-10 | 29/47 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +6.6 | 2e-09 | 26/45 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.5 | 4e-09 | 29/46 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.28×** | +6.1 | 4e-08 | 31/48 (LoVo, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +5.9 | 2e-07 | 27/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 6e-06 | 25/47 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.7 | 7e-05 | 21/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.79×** | +4.3 | 5e-04 | 17/46 (C-33 A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9166.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (AN3 CA 0.0527×, RPMI-7951 0.172×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.133×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (COLO 205 0.0719×); [[Silodosin (drug)]] 5 µM in 1 line (SHP-77 0.207×); [[Isocorydine (drug)]] 0.5 µM in 1 line (Hs 766T 0.212×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Thymol (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.035 | 17/48 (SW 900, HS-578T, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.682×** | -3.8 | 0.035 | 19/44 (LS 180, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.794× | -3.3 | 0.17 | 8/47 (RKO, J82, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 16.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +17.1) | — |
| [[A-172 (line)]] | wt | 25.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.21× (z +22.0) | — |
| [[HEC-1-A (line)]] | alt | 33.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +22.4) | — |
| [[LS 180 (line)]] | wt | 16.0 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +11.8) | [[XRK3F2 (drug)]] 0.5 µM 0.149× (z -8.5) |
| [[A549 (line)]] | wt | 13.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +14.6) | — |
| [[HOP62 (line)]] | alt | 13.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +15.3) | — |
| [[SW480 (line)]] | alt | 25.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.25× (z +16.6) | — |
| [[A498 (line)]] | wt | 26.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +16.9) | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.30× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 14.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +10.5) | [[Isocorydine (drug)]] 0.5 µM 0.212× (z -8.7) |
| [[RKO (line)]] | wt | 48.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +14.9) | — |
| [[SNU-423 (line)]] | alt | 17.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +16.8) | — |
| [[HCT15 (line)]] | alt | 30.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 13.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 8.25 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +15.2) | — |
| [[SHP-77 (line)]] | alt | 27.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.1) | [[Silodosin (drug)]] 5 µM 0.207× (z -9.3) |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0527× (z -9.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 7.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0719× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +9.1) | — |
| [[J82 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +16.2) | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.172× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +10.0) | — |
| [[SW48 (line)]] | wt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +9.7) | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD9]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CLUH]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[DDX51]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CPSF1]] | +0.57 | +0.23 / +0.60 | both halves | 5e-04 |  |
| [[INF2]] | +0.56 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[CHERP]] | +0.56 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[NOL6]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[IPO4]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ANAPC2]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[CACTIN]] | +0.54 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ATAD3B]] | +0.53 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[NOC2L]] | +0.53 | +0.36 / +0.54 | both halves | 9e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHA5]] | -0.54 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SDAD1P1]] | -0.48 | -0.21 / -0.51 | both halves | 6e-04 |  |
| [[NEK7]] | -0.47 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[TAX1BP1]] | -0.46 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[SEPTIN7]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MEGF9]] | -0.46 | -0.40 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[XPR1]] | -0.45 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[MPC2]] | -0.44 | -0.43 / -0.42 | both halves | 4e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[PEAK1]] | -0.44 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[MAGI3]] | -0.44 | -0.38 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.1, -40.6); signed map (1.8, -48.0). **Vector** length 51.8, 8.02% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +27.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.9 | +13.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +2.7 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | +0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -2.1 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +3.5 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear RNA activating complex polypeptide 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,375,567-136,400,176 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP190, PTFalpha, FLJ13451 |
| Gene groups (HGNC) | Myb/SANT domain containing; SNAP complex |
| Hallmark sets | DNA_REPAIR |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 3 Promoter; RNA Polymerase III Transcription Initiation; RNA Polymerase III Abortive And Retractive Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SXM2](https://www.uniprot.org/uniprotkb/Q5SXM2) (snRNA-activating protein complex subunit 4):

> Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box.

**Summary**, from NCBI Gene [6621](https://www.ncbi.nlm.nih.gov/gene/6621):

> This gene encodes the largest subunit of the small nuclear RNA-activating protein (SNAP) complex. The encoded protein contains a Myb DNA-binding domain, and is essential for RNA polymerase II and III polymerase transcription from small nuclear RNA promoters. A mutation in this gene is associated with ankylosing spondylitis. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:11137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11137) · Entrez [6621](https://www.ncbi.nlm.nih.gov/gene/6621) · UniProt [Q5SXM2](https://www.uniprot.org/uniprotkb/Q5SXM2) · Ensembl [ENSG00000165684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165684)

## Data

Gene col 9166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9166); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9166]; `tensor/DDL_lfc|DDL_z.npy` [9166]; `embed/gene_vectors.npy` [9166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9166 or target_col == 9166). Every well: [[SNAPC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAPC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
