---
symbol: "SMG1P5"
type: "gene"
col: 11422
ensembl_id: "ENSG00000183604"
name: "SMG1 pseudogene 5"
location: "16p11.2"
module: 16
arm: "-"
pooled_cpm: 16.23
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SMG1P5

*SMG1 pseudogene 5* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +8.0, q 5e-13, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.451× (z -9.6, q 4e-19, down in 35 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.626× (z -5.6, q 2e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF38]] (+0.71, fdr 7e-06), [[CCT6P3-1]] (+0.71, fdr 7e-06), [[SPATA33]] (+0.68, fdr 1e-05); moves opposite to [[CSTF2T]] (-0.68, fdr 7e-06), [[ZNF620]] (-0.65, fdr 7e-06), [[ZC3H11A]] (-0.65, fdr 3e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BHLHE41]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.0 | 5e-13 | 34/46 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +7.6 | 9e-12 | 36/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +7.0 | 5e-10 | 35/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +6.7 | 3e-09 | 32/47 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +6.6 | 4e-09 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +6.5 | 7e-09 | 30/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.1 | 1e-07 | 28/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.7 | 6e-07 | 27/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +5.6 | 2e-06 | 28/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +5.2 | 1e-05 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +5.1 | 2e-05 | 24/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +3.9 | 0.004 | 20/45 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.006 | 18/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.008 | 19/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.010 | 15/46 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.017 | 13/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.092 | 3/47 (LS 180, NCI-H2030, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.092 | 5/48 (A549, SW48, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11422.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.451×** | -9.6 | 4e-19 | 35/41 (SHP-77, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -8.8 | 5e-16 | 24/29 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.557×** | -6.5 | 1e-08 | 22/34 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -5.6 | 2e-06 | 25/48 (A549, A-172, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.658×** | -4.8 | 1e-04 | 21/47 (A-172, A549, …) | two highest doses | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.731×** | -3.8 | 0.015 | 18/48 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.736×** | -3.7 | 0.019 | 16/42 (hTERT-HPNE, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.054 | 12/48 (HS-578T, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.762×** | -3.3 | 0.068 | 18/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -3.2 | 0.080 | 18/47 (SW480, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[AZD-7648 (drug)]] 5 µM |  | **0.606×** | -3.2 | 0.081 | 16/45 (SW480, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.775× | -3.1 | 0.10 | 13/48 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.837× | -3.0 | 0.11 | 14/48 (SW1417, PANC-1, …) | top dose only |  |
| [[DT-061 (drug)]] 5 µM |  | 0.621× | -3.0 | 0.11 | 8/44 (SW 900, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.7 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0860× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.271× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.335× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[MK-3903 (drug)]] 5 µM 0.0589× (z -8.6) |
| [[A498 (line)]] | wt | 18.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -10.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 15.4 | 0 | 2 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0854× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -13.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -8.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.142× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LOX-IMVI (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -10.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0936× (z -10.0) |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -13.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 10.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +8.8) | — |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF38]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[CCT6P3-1]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[SPATA33]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[CORO7]] | +0.67 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[MFSD14CP]] | +0.66 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZNF250]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[SEC11A]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[FBXO31]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SMG1P2]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GIT1]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[UBE2G1]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF2T]] | -0.68 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[ZC3H11A]] | -0.65 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[ARCN1]] | -0.64 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[HNRNPH2]] | -0.64 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.64 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[TIGD2]] | -0.63 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[RTL6]] | -0.63 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[MIS12]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[ZNF776]] | -0.62 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[ZMYM4]] | -0.61 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[ANAPC13]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BHLHE41]] | B | BHLHE41 activity lowers SMG1P5's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.20× higher at baseline in the lines without BHLHE41 | 0.030 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[ARL14]] | B | ARL14 activity lowers SMG1P5's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.17× higher at baseline in the lines without ARL14 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-10.6, -5.5); signed map (-41.9, -0.6). **Vector** length 78.4, 15.7% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +7.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | -0.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -7.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +3.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SMG1 pseudogene 5 |
| Locus type | pseudogene |
| Location | 16p11.2 — chr16:30,267,553-30,335,054 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49862) · Entrez [595101](https://www.ncbi.nlm.nih.gov/gene/595101) · Ensembl [ENSG00000183604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183604)

## Data

Gene col 11422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11422); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11422]; `tensor/DDL_lfc|DDL_z.npy` [11422]; `embed/gene_vectors.npy` [11422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11422 or target_col == 11422). Every well: [[SMG1P5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG1P5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
