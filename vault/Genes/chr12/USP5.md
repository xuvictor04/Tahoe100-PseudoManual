---
symbol: "USP5"
type: "gene"
col: 3255
ensembl_id: "ENSG00000111667"
name: "ubiquitin specific peptidase 5"
location: "12p13.31"
module: 25
arm: "+"
pooled_cpm: 23.32
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# USP5

*ubiquitin specific peptidase 5* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.34× (z +16.5, q 0e+00, up in 34 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.41× (z +12.5, q 9e-34, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -13.4, q 5e-38, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB2]] (+0.75, fdr 7e-06), [[TRRAP]] (+0.72, fdr 7e-06), [[NECAB3]] (+0.72, fdr 7e-06); moves opposite to [[BTG1]] (-0.65, fdr 7e-06), [[ACAP1]] (-0.64, fdr 7e-06), [[TNRC6C]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[B4GALNT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +16.5 | 0e+00 | 34/35 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +15.5 | 0e+00 | 41/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.41×** | +12.5 | 9e-34 | 45/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.34×** | +12.1 | 1e-31 | 45/48 (HOP62, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.28×** | +11.1 | 2e-26 | 41/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +10.3 | 7e-23 | 36/40 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.7 | 2e-04 | 25/47 (A-427, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.008 | 20/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.6 | 0.015 | 18/40 (SNU-423, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.6 | 0.015 | 12/30 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.045 | 10/47 (NCI-H460, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.045 | 16/48 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.1 | 0.075 | 0/48 | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.51×** | +3.1 | 0.083 | 12/46 (NCI-H23, C32, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +3.1 | 0.083 | 9/48 (HOP62, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -13.4 | 5e-38 | 39/47 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.489×** | -10.2 | 7e-22 | 34/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.743×** | -5.9 | 6e-07 | 32/48 (A498, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.696×** | -5.2 | 3e-05 | 27/47 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.697×** | -5.1 | 3e-05 | 27/47 (A498, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.694×** | -5.0 | 5e-05 | 26/48 (J82, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.732×** | -4.4 | 7e-04 | 21/48 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.746×** | -4.2 | 0.002 | 22/48 (NCI-H1792, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.760×** | -3.7 | 0.011 | 17/47 (Hs 766T, A-172, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.783×** | -3.5 | 0.029 | 14/48 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.844× | -3.4 | 0.035 | 14/48 (RPMI-7951, HCT15, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.846× | -3.3 | 0.038 | 20/48 (A498, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.787×** | -3.3 | 0.038 | 16/48 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 0.851× | -3.2 | 0.052 | 10/48 (SW 1271, CFPAC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.4) |
| [[PANC-1 (line)]] | alt | 17.4 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.16× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.0) |
| [[HOP62 (line)]] | alt | 18.7 | 3 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.78× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 38.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 16.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.5) |
| [[SW480 (line)]] | alt | 32.5 | 3 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.31× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.6) |
| [[A-427 (line)]] | wt | 72.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.74× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -24.5) |
| [[A498 (line)]] | wt | 34.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.8) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.475× (z -10.1) ⚠ cell-cycle shift, explains ~70% of this change |
| [[A549 (line)]] | wt | 18.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.11× (z +10.0) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -14.7) |
| [[HT-29 (line)]] | alt | 16.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.2) |
| [[J82 (line)]] | alt | 21.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -17.3) |
| [[KATO III (line)]] | alt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 18.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 56.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.2) |
| [[SW 900 (line)]] | alt | 31.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -10.0) |
| [[SW48 (line)]] | wt | 22.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -9.3) |
| [[A-172 (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +8.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 11.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.53× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +10.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.3) |
| [[LS 180 (line)]] | wt | 23.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.93× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.8) |
| [[SNU-1 (line)]] | wt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.1) |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB2]] | +0.75 | +0.76 / +0.74 | both halves | 7e-06 | pathway: Deubiquitination |
| [[TRRAP]] | +0.72 | +0.71 / +0.75 | both halves | 7e-06 | pathway: Deubiquitination |
| [[NECAB3]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PRPS1]] | +0.72 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[ELAC2]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[AP3M1]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GPN1]] | +0.70 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[POMT2]] | +0.69 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ACTR1A]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[BABAM1]] | +0.69 | +0.77 / +0.54 | both halves | 1e-05 | pathway: Deubiquitination |
| [[CCT3]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ABCB8]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTG1]] | -0.65 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[ACAP1]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.64 | -0.69 / -0.59 | both halves | 7e-06 |  |
| [[POLR1H]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[LRCH3]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[PIM3]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[METTL23]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[EIF1B]] | -0.57 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.57 | -0.53 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALNT1]] | B | B4GALNT1 activity raises USP5's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without B4GALNT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises USP5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises USP5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.1, -13.1); signed map (-29.1, -29.6). **Vector** length 107, 27.7% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.9 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.4 | +12.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.5 | +11.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.3 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +1.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.2 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -13.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -5.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -0.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.3 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,852,148-6,866,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IsoT |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 4 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Ub-specific processing proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [P45974](https://www.uniprot.org/uniprotkb/P45974) (Ubiquitin carboxyl-terminal hydrolase 5):

> Deubiquitinating enzyme that participates in a wide range of cellular processes by specifically cleaving isopeptide bonds between ubiquitin and substrate proteins or ubiquitin itself. Affects thereby important cellular signaling pathways such as NF-kappa-B, Wnt/beta-catenin, and cytokine production by regulating ubiquitin-dependent protein degradation. Participates in the activation of the Wnt signaling pathway by promoting FOXM1 deubiquitination and stabilization that induces the recruitment …

**Summary**, from NCBI Gene [8078](https://www.ncbi.nlm.nih.gov/gene/8078):

> Ubiquitin (see MIM 191339)-dependent proteolysis is a complex pathway of protein metabolism implicated in such diverse cellular functions as maintenance of chromatin structure, receptor function, and degradation of abnormal proteins. A late step of the process involves disassembly of the polyubiquitin chains on degraded proteins into ubiquitin monomers. USP5 disassembles branched polyubiquitin chains by a sequential exo mechanism, starting at the proximal end of the chain (Wilkinson et al., …

**Accessions** — [HGNC:12628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12628) · Entrez [8078](https://www.ncbi.nlm.nih.gov/gene/8078) · UniProt [P45974](https://www.uniprot.org/uniprotkb/P45974) · Ensembl [ENSG00000111667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111667)

## Data

Gene col 3255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3255); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3255]; `tensor/DDL_lfc|DDL_z.npy` [3255]; `embed/gene_vectors.npy` [3255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3255 or target_col == 3255). Every well: [[USP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
