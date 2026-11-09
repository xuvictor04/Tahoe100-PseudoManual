---
symbol: "CHRAC1"
type: "gene"
col: 2465
ensembl_id: "ENSG00000104472"
name: "chromatin accessibility complex subunit 1"
location: "8q24.3"
module: 3
arm: "-"
pooled_cpm: 25.88
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CHRAC1

*chromatin accessibility complex subunit 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.09× (z +15.1, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 3.46×, SW480 5.10×, HT-29 3.70×, HOP62 4.25×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 5.51×, PANC-1 3.43×, A549 5.74×, KATO III 4.87×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 5.22×, HOP62 3.89×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.421× (z -11.6, q 2e-28, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEPROT]] (+0.69, fdr 7e-06), [[FGD5-AS1]] (+0.68, fdr 7e-06), [[HNRNPK]] (+0.68, fdr 1e-05); moves opposite to [[ATG4B]] (-0.68, fdr 1e-05), [[RPS26]] (-0.67, fdr 3e-05), [[MRPL55]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[OSBPL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2465.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 3.46×, SW480 5.10×, HT-29 3.70×, HOP62 4.25×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 5.51×, PANC-1 3.43×, A549 5.74×, KATO III 4.87×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 5.22×, HOP62 3.89×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +15.1 | 0e+00 | 43/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +13.0 | 5e-36 | 33/34 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +10.9 | 2e-25 | 35/38 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.66×** | +6.8 | 2e-09 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.58×** | +6.2 | 8e-08 | 32/47 (SW480, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.51×** | +5.6 | 2e-06 | 33/47 (SW480, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.39×** | +4.4 | 7e-04 | 22/45 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +4.3 | 0.001 | 27/47 (A549, HOP62, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.39×** | +4.3 | 0.001 | 23/45 (COLO 205, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.28×** | +3.3 | 0.054 | 19/46 (LoVo, SW480, …) | two highest doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.39×** | +3.2 | 0.076 | 12/43 (HOP62, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.076 | 8/48 (SW480, HOP62, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2465.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.421×** | -11.6 | 2e-28 | 44/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.442×** | -11.0 | 2e-25 | 46/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -10.9 | 3e-25 | 43/47 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.587×** | -7.1 | 1e-10 | 38/48 (LS 180, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.619×** | -6.4 | 1e-08 | 31/46 (C32, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.762×** | -5.2 | 2e-05 | 34/48 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.481×** | -5.1 | 2e-05 | 28/48 (NCI-H23, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.523×** | -4.5 | 4e-04 | 26/48 (A-427, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.724×** | -4.3 | 9e-04 | 23/47 (SK-MEL-2, HT-29, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -4.3 | 0.001 | 27/45 (A-427, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.659×** | -4.0 | 0.003 | 22/45 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.737×** | -3.7 | 0.012 | 21/48 (H4, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.3 | 0.044 | 20/47 (NCI-H2030, RKO, …) | top dose only |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.777×** | -3.3 | 0.046 | 17/47 (NCI-H2030, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.5 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +13.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -11.6) |
| [[SW480 (line)]] | alt | 16.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +12.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.236× (z -10.9) |
| [[A-427 (line)]] | wt | 30.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0774× (z -10.4) |
| [[HOP62 (line)]] | alt | 22.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +11.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 72.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +12.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 25.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.22× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 38.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.260× (z -11.1) |
| [[A498 (line)]] | wt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 23.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.74× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 41.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -11.8) |
| [[Hs 766T (line)]] | wt | 35.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 28.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +9.4) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.317× (z -9.1) |
| [[LS 180 (line)]] | wt | 21.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.252× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 17.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +11.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 42.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0592× (z -11.0) |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEPROT]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[FGD5-AS1]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[HNRNPK]] | +0.68 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ELK4]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PRKAR1A]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[AKAP11]] | +0.66 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.64 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TWF1]] | +0.62 | +0.46 / +0.72 | both halves | 2e-05 |  |
| [[MBNL3]] | +0.62 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[LIN7C]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[SCRN1]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4B]] | -0.68 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[RPS26]] | -0.67 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[MRPL55]] | -0.65 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RALA]] | -0.65 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TMEM208]] | -0.64 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[BAHD1]] | -0.63 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[ATP5MJ]] | -0.63 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[NSUN5P1-1]] | -0.62 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[MALSU1]] | -0.62 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[RBIS]] | -0.61 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[EML2]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[RALGDS]] | -0.60 | -0.40 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL7]] | B | OSBPL7 activity lowers CHRAC1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without OSBPL7 | 0.050 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.0, -22.1); signed map (17.8, -33.6). **Vector** length 97.6, 24.3% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.2 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.1 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.4 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.2 | +1.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +2.1 | +0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +1.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.8 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.4 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -4.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -2.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | chromatin accessibility complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:140,511,311-140,517,154 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHRAC15, YCL1 |
| Gene groups (HGNC) | Chromatin accessibility complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRG0](https://www.uniprot.org/uniprotkb/Q9NRG0) (Chromatin accessibility complex protein 1):

> Forms a complex with DNA polymerase epsilon subunit POLE3 and binds naked DNA, which is then incorporated into chromatin, aided by the nucleosome remodeling activity of ISWI/SNF2H and ACF1. Does not enhance nucleosome sliding activity of the ACF-5 ISWI chromatin remodeling complex.

**Summary**, from NCBI Gene [54108](https://www.ncbi.nlm.nih.gov/gene/54108):

> CHRAC1 is a histone-fold protein that interacts with other histone-fold proteins to bind DNA in a sequence-independent manner. These histone-fold protein dimers combine within larger enzymatic complexes for DNA transcription, replication, and packaging.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:13544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13544) · Entrez [54108](https://www.ncbi.nlm.nih.gov/gene/54108) · UniProt [Q9NRG0](https://www.uniprot.org/uniprotkb/Q9NRG0) · Ensembl [ENSG00000104472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104472)

## Data

Gene col 2465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2465); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2465]; `tensor/DDL_lfc|DDL_z.npy` [2465]; `embed/gene_vectors.npy` [2465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2465 or target_col == 2465). Every well: [[CHRAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
