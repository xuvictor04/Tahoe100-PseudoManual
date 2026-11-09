---
symbol: "UBE2Q2"
type: "gene"
col: 6395
ensembl_id: "ENSG00000140367"
name: "ubiquitin conjugating enzyme E2 Q2"
location: "15q24.2"
module: 190
arm: "+"
pooled_cpm: 66.64
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# UBE2Q2

*ubiquitin conjugating enzyme E2 Q2* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.48× (z +9.1, q 7e-17, up in 33 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.41× (z +8.2, q 6e-14, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.311× (z -28.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2Q2P1]] (+0.60, fdr 7e-06), [[HSPE1-MOB4]] (+0.60, fdr 1e-05), [[ECPAS]] (+0.60, fdr 2e-05); moves opposite to [[CAAP1]] (-0.54, fdr 1e-05), [[NCEH1]] (-0.51, fdr 3e-05), [[INIP]] (-0.50, fdr 4e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +9.1 | 7e-17 | 33/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +8.2 | 6e-14 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +6.1 | 2e-07 | 21/49 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.9 | 5e-07 | 25/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +5.8 | 1e-06 | 25/48 (SW480, RPMI-7951, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +5.1 | 4e-05 | 17/49 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.22×** | +4.7 | 3e-04 | 22/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +4.6 | 3e-04 | 18/48 (HT-29, LoVo, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.3 | 0.001 | 17/45 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.003 | 18/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.013 | 12/48 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.045 | 11/49 (LoVo, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.045 | 7/48 (HS-578T, A549, …) | top dose only | plate-row cell shift |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.045 | 14/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.054 | 16/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.10× | +3.1 | 0.064 | 0/49 | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.13× | +3.0 | 0.088 | 6/48 (BT-474, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.311×** | -28.0 | 0e+00 | 47/48 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.323×** | -27.1 | 0e+00 | 47/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.384×** | -23.0 | 0e+00 | 47/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.502×** | -16.5 | 0e+00 | 41/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.670×** | -13.6 | 4e-40 | 34/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.648×** | -10.0 | 1e-21 | 29/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.562×** | -7.2 | 4e-11 | 29/49 (HOP62, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -7.1 | 6e-11 | 23/48 (SW480, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.751×** | -6.9 | 4e-10 | 29/48 (AsPC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -6.7 | 1e-09 | 27/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.755×** | -6.5 | 5e-09 | 32/47 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.779×** | -6.0 | 1e-07 | 29/49 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.780×** | -6.0 | 1e-07 | 23/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.630×** | -5.8 | 3e-07 | 28/49 (A-172, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.727×** | -4.0 | 0.002 | 23/48 (KATO III, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.856× | -3.7 | 0.007 | 19/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 60.6 | 5 (5 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.228× (z -22.1) |
| [[A-172 (line)]] | wt | 70.6 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -26.2) |
| [[HOP62 (line)]] | alt | 91.8 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -19.8) |
| [[PANC-1 (line)]] | alt | 66.9 | 2 (1 ⚠) | 5 | [[Niclosamide (olamine) (drug)]] 5 µM 1.79× (z +8.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.72× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -16.3) |
| [[A549 (line)]] | wt | 109 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -20.8) |
| [[Hs 766T (line)]] | wt | 75.3 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -19.4) |
| [[hTERT-HPNE (line)]] | wt | 82.8 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -17.2) |
| [[LoVo (line)]] | wt | 40.5 | 3 (3 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 84.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 56.2 | 3 (3 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.46× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -13.3) |
| [[SNU-423 (line)]] | alt | 67.3 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -18.8) |
| [[J82 (line)]] | alt | 73.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.9) |
| [[NCI-H23 (line)]] | alt | 42.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.6) |
| [[RKO (line)]] | wt | 92.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -15.9) |
| [[A-427 (line)]] | wt | 42.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.317× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 54.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -15.1) |
| [[C32 (line)]] | wt | 53.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -13.1) |
| [[HS-578T (line)]] | alt | 87.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 125 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 72.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.05 µM 0.389× (z -9.6) |
| [[A498 (line)]] | wt | 39.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 89.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -14.5) |
| [[HT-29 (line)]] | alt | 59.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -12.9) |
| [[LS 180 (line)]] | wt | 34.3 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -20.2) |
| [[NCI-H1573 (line)]] | alt | 46.2 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.364× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 93.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 56.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -13.9) |
| [[SW1417 (line)]] | alt | 70.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.360× (z -11.2) |
| [[H4 (line)]] | wt | 69.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -10.3) |
| [[SHP-77 (line)]] | alt | 65.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -9.9) |
| [[SW48 (line)]] | wt | 71.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -12.8) |
| [[AN3 CA (line)]] | alt | 109 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -10.5) |
| [[BT-474 (line)]] | alt | 64.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 44.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -11.0) |
| [[SNU-1 (line)]] | wt | 63.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 52.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0607× (z -8.8) |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -10.2) |
| [[C-33 A (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2Q2P1]] | +0.60 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[HSPE1-MOB4]] | +0.60 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ECPAS]] | +0.60 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[GPR161]] | +0.57 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[SMG1P5]] | +0.55 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ATP2C1]] | +0.55 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MID2]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[FHIP2A]] | +0.55 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[PAQR3]] | +0.54 | +0.55 / +0.30 | both halves | 2e-04 |  |
| [[PCGF5]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[RNF38]] | +0.54 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[DGKE]] | +0.53 | +0.39 / +0.41 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAAP1]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NCEH1]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[INIP]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[FAF2]] | -0.50 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[IER2]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[SRSF9]] ⚠ | -0.49 | -0.44 / -0.33 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SPG11]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[DIABLO]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[LIMA1]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SYTL2]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PHACTR4]] | -0.48 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ABCF1]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CHTOP]] | -0.48 | -0.54 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers UBE2Q2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.8, 16.8); signed map (-22.0, -0.9). **Vector** length 106, 29.3% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +12.9 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.2 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +6.5 | -3.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.5 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +5.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.2 | -7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -6.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.7 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 Q2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,843,307-75,901,078 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762C143 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2; RWD domain containing |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVN8](https://www.uniprot.org/uniprotkb/Q8WVN8) (Ubiquitin-conjugating enzyme E2 Q2):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-48'-linked polyubiquitination.

**Summary**, from NCBI Gene [92912](https://www.ncbi.nlm.nih.gov/gene/92912):

> Enables ubiquitin-protein transferase activity. Involved in protein K48-linked ubiquitination. Predicted to be located in cytosol. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19248) · Entrez [92912](https://www.ncbi.nlm.nih.gov/gene/92912) · UniProt [Q8WVN8](https://www.uniprot.org/uniprotkb/Q8WVN8) · Ensembl [ENSG00000140367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140367)

## Data

Gene col 6395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6395); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6395]; `tensor/DDL_lfc|DDL_z.npy` [6395]; `embed/gene_vectors.npy` [6395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6395 or target_col == 6395). Every well: [[UBE2Q2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2Q2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
