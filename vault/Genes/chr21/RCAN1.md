---
symbol: "RCAN1"
type: "gene"
col: 8227
ensembl_id: "ENSG00000159200"
name: "regulator of calcineurin 1"
location: "21q22.12"
module: 151
arm: "+"
pooled_cpm: 33.67
n_lines_expressing: 50
n_dd_up: 49
n_dd_down: 5
n_dd_up_clean: 35
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# RCAN1

*regulator of calcineurin 1* — 21q22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +15.7, q 0e+00, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.747× (z -5.2, q 1e-04, down in 19 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[HI-TOPK-032 (drug)]] 5 µM: 0.666× (z -3.9, q 0.017, down in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.0479×, C32 0.171×, H4 0.0853×, LoVo 0.189×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C32 0.168×, SHP-77 0.118×, LOX-IMVI 0.246×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H23 0.0766×, RKO 0.230×; ⚠ toxic); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 0.203×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (C32 0.248×); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.391×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB21]] (+0.55, fdr 4e-05), [[IL32]] (+0.53, fdr 2e-05), [[ALOXE3]] (+0.53, fdr 3e-05); moves opposite to [[FOXK1]] (-0.53, fdr 2e-05), [[MARCHF6]] (-0.51, fdr 3e-05), [[RBL2]] (-0.51, fdr 2e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ROBO4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 20 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +15.7 | 0e+00 | 34/46 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +14.6 | 1e-45 | 32/47 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.13×** | +13.8 | 4e-41 | 36/48 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +10.6 | 2e-24 | 33/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +10.0 | 1e-21 | 29/46 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +9.0 | 2e-17 | 27/48 (HOP62, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +8.4 | 5e-15 | 30/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +8.1 | 4e-14 | 28/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.28×** | +7.9 | 2e-13 | 28/46 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +7.6 | 2e-12 | 27/48 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +7.6 | 2e-12 | 24/48 (A-172, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +7.5 | 2e-12 | 24/48 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **2.18×** | +7.5 | 4e-12 | 28/47 (PANC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.48×** | +7.2 | 3e-11 | 24/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.09×** | +7.1 | 5e-11 | 26/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.04×** | +6.8 | 2e-10 | 25/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.03×** | +6.8 | 3e-10 | 27/45 (PANC-1, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.6 | 1e-09 | 27/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.8 | 2e-07 | 21/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8227.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.0479×, C32 0.171×, H4 0.0853×, LoVo 0.189×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C32 0.168×, SHP-77 0.118×, LOX-IMVI 0.246×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H23 0.0766×, RKO 0.230×; ⚠ toxic); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 0.203×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (C32 0.248×); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.391×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.747×** | -5.2 | 1e-04 | 19/31 (LOX-IMVI, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.762×** | -4.8 | 4e-04 | 19/45 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.666×** | -3.9 | 0.017 | 16/46 (LOX-IMVI, C32, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.080 | 14/48 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.703×** | -3.4 | 0.080 | 9/46 (C32, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 267 | 0 | 20 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.203× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 144 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0479× (z -24.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 12.4 | 6 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 7.73× (z +15.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.4) | — |
| [[A-172 (line)]] | wt | 63.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +16.8) | — |
| [[HS-578T (line)]] | alt | 20.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 29.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.37× (z +17.8) | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +11.2) | [[Digitoxin (drug)]] 0.05 µM 0.228× (z -10.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 46.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +15.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.291× (z -9.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 23.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +14.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 111 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.22× (z +13.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.05× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 22.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +15.2) | — |
| [[SW480 (line)]] | alt | 12.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 22.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +11.6) | — |
| [[H4 (line)]] | wt | 51.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0853× (z -13.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.3 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.96× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 19.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.5) | — |
| [[RKO (line)]] | wt | 40.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.230× (z -11.2) ⚠ toxic |
| [[A549 (line)]] | wt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.3) | — |
| [[J82 (line)]] | alt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.0) | — |
| [[KATO III (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 8.12× (z +12.8) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0766× (z -16.0) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 24.2 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.08× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 45.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +8.6) | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB21]] | +0.55 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[IL32]] | +0.53 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ALOXE3]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ABL2]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SAMD4A]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TNIP3]] | +0.51 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ENKUR]] | +0.50 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[TBX3]] | +0.50 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[CA13]] | +0.50 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[HCCS]] | +0.50 | +0.55 / +0.37 | both halves | 7e-05 |  |
| [[ROBO4]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[RND3]] | +0.49 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXK1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MARCHF6]] | -0.51 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[RBL2]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NUDT21]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[RCN2]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[FBXO25]] | -0.48 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[MZT1]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[RAB40B]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[PLXND1]] | -0.46 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[PPT2]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[RANBP9]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MPHOSPH9]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO4]] | B | ROBO4 activity raises RCAN1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without ROBO4 | 0.006 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[LINC01812]] | B | LINC01812 activity raises RCAN1's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.35× lower at baseline in the lines without LINC01812 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[TOP2A]] | B | TOP2A activity lowers RCAN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.383). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.1, 5.4); signed map (27.3, 11.3). **Vector** length 112, 28.6% of its response variance represented; |z| ≥ 3 in 1,375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +13.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +15.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +9.0 |
|  | [[EX229 (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +6.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.9 | +4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.8 | +6.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.1 | +7.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.8 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | regulator of calcineurin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.12 — chr21:34,513,142-34,615,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DSCR1 |
| Gene groups (HGNC) | Regulator of calcineurin family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [P53805](https://www.uniprot.org/uniprotkb/P53805) (Calcipressin-1):

> Inhibits calcineurin-dependent transcriptional responses by binding to the catalytic domain of calcineurin A. Could play a role during central nervous system development (By similarity).

**Summary**, from NCBI Gene [1827](https://www.ncbi.nlm.nih.gov/gene/1827):

> The protein encoded by this gene interacts with calcineurin A and inhibits calcineurin-dependent signaling pathways, possibly affecting central nervous system development. This gene is located in the minimal candidate region for the Down syndrome phenotype, and is overexpressed in the brain of Down syndrome fetuses. Chronic overexpression of this gene may lead to neurofibrillary tangles such as those associated with Alzheimer disease. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:3040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3040) · Entrez [1827](https://www.ncbi.nlm.nih.gov/gene/1827) · UniProt [P53805](https://www.uniprot.org/uniprotkb/P53805) · Ensembl [ENSG00000159200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159200)

## Data

Gene col 8227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8227); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8227]; `tensor/DDL_lfc|DDL_z.npy` [8227]; `embed/gene_vectors.npy` [8227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8227 or target_col == 8227). Every well: [[RCAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
