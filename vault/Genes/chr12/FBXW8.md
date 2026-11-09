---
symbol: "FBXW8"
type: "gene"
col: 10549
ensembl_id: "ENSG00000174989"
name: "F-box and WD repeat domain containing 8"
location: "12q24.22"
module: 1
arm: "+"
pooled_cpm: 60.2
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FBXW8

*F-box and WD repeat domain containing 8* — 12q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.43× (z +5.5, q 2e-05, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HCT15 2.50×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.526× (z -14.1, q 3e-42, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ICE2]] (+0.64, fdr 1e-05), [[TXNRD3]] (+0.62, fdr 9e-06), [[DPH5]] (+0.60, fdr 1e-05); moves opposite to [[GRN]] (-0.53, fdr 3e-05), [[TPI1]] (-0.53, fdr 5e-05), [[ADD3]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10549.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HCT15 2.50×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-05 | 27/48 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.058 | 23/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.2 | 0.21 | 14/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.23× | +3.2 | 0.21 | 19/48 (SK-MEL-2, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10549.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.526×** | -14.1 | 3e-42 | 44/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.433×** | -13.0 | 6e-36 | 42/48 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.541×** | -9.5 | 4e-19 | 40/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.567×** | -8.8 | 2e-16 | 35/48 (H4, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.582×** | -8.4 | 6e-15 | 37/48 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.586×** | -8.3 | 1e-14 | 38/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -8.0 | 9e-14 | 36/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.588×** | -7.9 | 2e-13 | 27/43 (KATO III, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.603×** | -7.8 | 3e-13 | 34/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.627×** | -7.2 | 3e-11 | 31/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.624×** | -7.0 | 1e-10 | 33/48 (RKO, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.631×** | -6.9 | 3e-10 | 31/47 (LoVo, J82, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.648×** | -6.7 | 8e-10 | 38/48 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.641×** | -6.6 | 2e-09 | 35/50 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.658×** | -6.5 | 3e-09 | 34/48 (SW 1088, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.749×** | -4.5 | 2e-04 | 29/48 (C-33 A, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.611×** | -4.0 | 0.002 | 27/48 (A-427, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.790×** | -3.4 | 0.015 | 23/48 (PANC-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 91.6 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 48.9 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -12.5) |
| [[SW480 (line)]] | alt | 79.5 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.341× (z -13.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -11.5) |
| [[LoVo (line)]] | wt | 84.9 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.316× (z -10.7) |
| [[A549 (line)]] | wt | 65.9 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.276× (z -12.5) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.1) |
| [[J82 (line)]] | alt | 52.6 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -11.7) |
| [[KATO III (line)]] | alt | 53.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0757× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[AsPC-1 (line)]] | alt | 50.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0952× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.9) |
| [[H4 (line)]] | wt | 115 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0939× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[NCI-H23 (line)]] | alt | 77.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[A-172 (line)]] | wt | 60.6 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -16.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.9) |
| [[A498 (line)]] | wt | 68.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -16.6) |
| [[BT-474 (line)]] | alt | 90.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.294× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C32 (line)]] | wt | 53.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -15.3) |
| [[HS-578T (line)]] | alt | 61.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -15.9) |
| [[HT-29 (line)]] | alt | 57.7 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.217× (z -12.4) |
| [[SW1417 (line)]] | alt | 49.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -9.1) |
| [[HCT15 (line)]] | alt | 89.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.204× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 31.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.156× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~49% of this change · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.181× (z -9.0) |
| [[HOP62 (line)]] | alt | 59.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -14.3) |
| [[Hs 766T (line)]] | wt | 43.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[LS 180 (line)]] | wt | 35.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -9.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1573 (line)]] | alt | 67.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 39.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0576× (z -20.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 75.4 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0772× (z -11.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 85.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -13.1) |
| [[SNU-1 (line)]] | wt | 47.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.6) |
| [[SW48 (line)]] | wt | 59.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -11.5) |
| [[A-427 (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 77.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 70.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 69.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -12.1) |
| [[SHP-77 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[SNU-423 (line)]] | alt | 50.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -12.5) |
| [[SW 1088 (line)]] | alt | 92.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0558× (z -10.1) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW 900 (line)]] | alt | 37.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.8) |
| [[AN3 CA (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICE2]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[TXNRD3]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[DPH5]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GAR1]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TCERG1]] | +0.59 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[RIOX2]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SEC23IP]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RUSF1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NPRL3]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SRP72]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[FAM98A]] | +0.57 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[PIGL]] | +0.56 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRN]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TPI1]] | -0.53 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ADD3]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[POU2F1]] | -0.50 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[NPTN]] | -0.50 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[BMPR2]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TSC22D4]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.5, -38.1); signed map (-0.2, -39.8). **Vector** length 102, 31.0% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -14.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.0 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.9 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box and WD repeat domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22 — chr12:116,910,950-117,031,148 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX29, FBW6, FBW8; previously FBXO29 |
| Gene groups (HGNC) | WD repeat domain containing; F-box and WD repeat domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3Y1](https://www.uniprot.org/uniprotkb/Q8N3Y1) (F-box/WD repeat-containing protein 8):

> Substrate-recognition component of the Cul7-RING(FBXW8) ubiquitin ligase complex, which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. The Cul7-RING(FBXW8) complex mediates ubiquitination and consequent degradation of GORASP1, acting as a component of the ubiquitin ligase pathway that regulates Golgi morphogenesis and dendrite patterning in brain. Mediates ubiquitination and degradation of IRS1 in a mTOR-dependent manner: the Cul7-RING(FBXW8) complex …

**Summary**, from NCBI Gene [26259](https://www.ncbi.nlm.nih.gov/gene/26259):

> This gene encodes a member of the F-box protein family, members of which are characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into three classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein …

**Accessions** — [HGNC:13597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13597) · Entrez [26259](https://www.ncbi.nlm.nih.gov/gene/26259) · UniProt [Q8N3Y1](https://www.uniprot.org/uniprotkb/Q8N3Y1) · Ensembl [ENSG00000174989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174989)

## Data

Gene col 10549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10549); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10549]; `tensor/DDL_lfc|DDL_z.npy` [10549]; `embed/gene_vectors.npy` [10549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10549 or target_col == 10549). Every well: [[FBXW8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXW8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
