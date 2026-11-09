---
symbol: "GRSF1"
type: "gene"
col: 5322
ensembl_id: "ENSG00000132463"
name: "G-rich RNA sequence binding factor 1"
location: "4q13.3"
module: 33
arm: "+"
pooled_cpm: 72.34
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# GRSF1

*G-rich RNA sequence binding factor 1* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.45× (z +8.3, q 4e-14, up in 31 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.41× (z +7.8, q 2e-12, up in 37 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.482×, SNU-1 0.544×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.328×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK7]] (+0.60, fdr 1e-05), [[PWP1]] (+0.55, fdr 2e-05), [[MRPS30]] (+0.54, fdr 1e-05); moves opposite to [[CRY1]] (-0.53, fdr 1e-05), [[STX5]] (-0.48, fdr 2e-05), [[COQ10B]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.45×** | +8.3 | 4e-14 | 31/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.8 | 2e-12 | 37/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +7.3 | 7e-11 | 1/50 (CHP-212) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.34×** | +6.4 | 2e-08 | 26/44 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +6.3 | 3e-08 | 30/48 (PANC-1, A-427, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.31×** | +6.1 | 7e-08 | 31/48 (NCI-H23, A549, …) | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.33×** | +6.1 | 7e-08 | 30/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.30×** | +5.9 | 3e-07 | 27/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.29×** | +5.6 | 1e-06 | 29/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.0 | 4e-05 | 23/48 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.9 | 4e-05 | 22/48 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.8 | 9e-05 | 27/50 (A-172, A-427, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.23×** | +4.6 | 2e-04 | 21/48 (LS 180, PANC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +4.3 | 8e-04 | 24/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 22/48 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +4.2 | 0.001 | 12/48 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.003 | 23/48 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.021 | 14/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.033 | 13/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.045 | 16/47 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.052 | 5/48 (C32, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.056 | 7/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +2.8 | 0.094 | 5/49 (AsPC-1, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5322.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.482×, SNU-1 0.544×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.328×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | 0.859× | -3.5 | 0.19 | 14/48 (HEC-1-A, HOP62, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.864× | -3.3 | 0.19 | 10/47 (C32, C-33 A, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.866× | -3.3 | 0.19 | 16/49 (KATO III, Hs 766T, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.870× | -3.2 | 0.21 | 8/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.872× | -3.1 | 0.21 | 3/48 (NCI-H2030, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.9 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.05× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A498 (line)]] | wt | 80.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 60.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 101 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.3) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 75.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 82.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.87× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.78× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 52.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.33× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 66.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 64.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H596 (line)]] | alt | 75.1 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.119× (z -8.8) |
| [[RKO (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK7]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PWP1]] | +0.55 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[MRPS30]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PTCD2]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 | STRING 471 |
| [[MRPS35]] | +0.53 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[GEMIN5]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[FAHD1]] | +0.48 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[RITA1]] | +0.47 | +0.44 / +0.40 | both halves | 4e-05 |  |
| [[AACSP1]] | +0.47 | +0.25 / +0.50 | both halves | 4e-04 |  |
| [[THOC7]] | +0.47 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[DNAJA2]] | +0.46 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[SLC25A36]] | +0.46 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRY1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[STX5]] | -0.48 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[COQ10B]] | -0.45 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[RAB5A]] | -0.44 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[WNT2B]] | -0.43 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[STK19]] | -0.43 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[LIN52]] | -0.42 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[SELENOK]] | -0.42 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[EML6]] | -0.41 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[HYPK]] | -0.41 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[CYSTM1]] | -0.40 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[CA5BP1]] | -0.40 | -0.23 / -0.41 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.327). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.9, -6.5); signed map (-18.0, -25.2). **Vector** length 79.4, 17.0% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.9 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.0 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -2.4 | +3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.3 | -0.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | G-rich RNA sequence binding factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:70,815,783-70,839,897 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 6 pathways, smallest: Mitochondrial RNA degradation; Viral mRNA Translation; Influenza Viral RNA Transcription and Replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12849](https://www.uniprot.org/uniprotkb/Q12849) (G-rich sequence factor 1):

> Regulator of post-transcriptional mitochondrial gene expression, required for assembly of the mitochondrial ribosome and for recruitment of mRNA and lncRNA. Binds RNAs containing the 14 base G-rich element. Preferentially binds RNAs transcribed from three contiguous genes on the light strand of mtDNA, the ND6 mRNA, and the long non-coding RNAs for MT-CYB and MT-ND5, each of which contains multiple consensus binding sequences. Involved in the degradosome-mediated decay of non-coding …

**Summary**, from NCBI Gene [2926](https://www.ncbi.nlm.nih.gov/gene/2926):

> The protein encoded by this gene is a cellular protein that binds RNAs containing the G-rich element. The protein is localized in the cytoplasm, and has been shown to stimulate translation of viral mRNAs in vitro. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4610](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4610) · Entrez [2926](https://www.ncbi.nlm.nih.gov/gene/2926) · UniProt [Q12849](https://www.uniprot.org/uniprotkb/Q12849) · Ensembl [ENSG00000132463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132463)

## Data

Gene col 5322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5322); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5322]; `tensor/DDL_lfc|DDL_z.npy` [5322]; `embed/gene_vectors.npy` [5322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5322 or target_col == 5322). Every well: [[GRSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
