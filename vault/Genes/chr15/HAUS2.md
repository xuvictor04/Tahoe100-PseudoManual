---
symbol: "HAUS2"
type: "gene"
col: 6072
ensembl_id: "ENSG00000137814"
name: "HAUS augmin like complex subunit 2"
location: "15q15.2"
module: 83
arm: "+"
pooled_cpm: 25.99
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# HAUS2

*HAUS augmin like complex subunit 2* — 15q15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +16.8, q 0e+00, up in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.35× (z +15.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.805× (z -5.5, q 3e-05, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.376×; ⚠ cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.338×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL6]] (+0.57, fdr 8e-05), [[ZNF621]] (+0.55, fdr 1e-04), [[ADAL]] (+0.53, fdr 2e-04); moves opposite to [[EGFL7]] (-0.46, fdr 2e-04), [[GUSBP18]] (-0.45, fdr 3e-04), [[C1GALT1C1]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.96×** | +16.8 | 0e+00 | 42/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +15.1 | 0e+00 | 43/48 (HOP62, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +14.9 | 0e+00 | 38/47 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +11.1 | 1e-26 | 42/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.80×** | +10.4 | 4e-23 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.78×** | +10.2 | 2e-22 | 32/42 (KATO III, PANC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +9.2 | 2e-18 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.62×** | +8.5 | 2e-15 | 30/46 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.4 | 2e-15 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +8.0 | 9e-14 | 35/48 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.72×** | +7.5 | 4e-12 | 27/36 (NCI-H460, LoVo, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.51×** | +6.7 | 8e-10 | 26/41 (MIA PaCa-2, PANC-1, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.56×** | +6.1 | 4e-08 | 29/47 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +5.8 | 2e-07 | 28/47 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.35×** | +5.3 | 4e-06 | 23/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.3 | 5e-06 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 22/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.003 | 15/47 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.004 | 9/48 (J82, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.005 | 18/48 (CFPAC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.014 | 13/47 (A-427, SW 900, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.026 | 12/48 (CFPAC-1, A498, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.028 | 8/48 (HT-29, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6072.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.376×; ⚠ cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.338×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.805×** | -5.5 | 3e-05 | 26/48 (HS-578T, A498, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 0.888× | -3.0 | 0.52 | 11/48 (CFPAC-1, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.0 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +14.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 27.5 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +19.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 25.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.4) | — |
| [[KATO III (line)]] | alt | 24.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.0) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[LoVo (line)]] | wt | 30.0 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.93× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.38× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 24.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.30× (z +13.2) | — |
| [[BT-474 (line)]] | alt | 17.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.29× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 25.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +17.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 24.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.68× (z +16.2) | — |
| [[Hs 766T (line)]] | wt | 21.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.77× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.338× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 24.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.98× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 25.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +15.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.5) | — |
| [[A-427 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[C32 (line)]] | wt | 18.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.15× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[J82 (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[LOX-IMVI (line)]] | wt | 28.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.97× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2347 (line)]] | alt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.61× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 27.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW 900 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +10.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 29.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.38× (z +9.1) | — |
| [[A498 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 14 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL6]] | +0.57 | +0.63 / +0.37 | both halves | 8e-05 |  |
| [[ZNF621]] | +0.55 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[ADAL]] | +0.53 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[ZNF382]] | +0.52 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[FBXO4]] | +0.51 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[CENPL]] | +0.49 | +0.49 / +0.38 | both halves | 6e-05 | pathway: Mitotic Prometaphase |
| [[C17orf75]] | +0.49 | +0.54 / +0.29 | both halves | 2e-04 |  |
| [[NNT-AS1]] | +0.49 | +0.56 / +0.32 | both halves | 2e-04 |  |
| [[ZNF85]] | +0.49 | +0.53 / +0.21 | both halves | 6e-04 |  |
| [[ZNF529-AS1]] | +0.49 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[TMEM222]] | +0.48 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[MAILR]] | +0.48 | +0.51 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGFL7]] | -0.46 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[GUSBP18]] | -0.45 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[C1GALT1C1]] | -0.44 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[HYAL2]] | -0.43 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[UQCRQ]] ⚠ | -0.43 | -0.40 / -0.32 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[XPR1]] | -0.42 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[COX6C]] | -0.42 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[PLCXD2]] | -0.41 | -0.39 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.9, 6.7); signed map (18.4, -19.3). **Vector** length 65.8, 12.5% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +15.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.5 | +16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.2 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.2 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +5.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | -0.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.1 | +4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | HAUS augmin like complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.2 — chr15:42,548,828-42,569,994 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10460, HsT17025; previously C15orf25, CEP27 |
| Gene groups (HGNC) | HAUS augmin like complex |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVX0](https://www.uniprot.org/uniprotkb/Q9NVX0) (HAUS augmin-like complex subunit 2):

> Contributes to mitotic spindle assembly, maintenance of centrosome integrity and completion of cytokinesis as part of the HAUS augmin-like complex.

**Summary**, from NCBI Gene [55142](https://www.ncbi.nlm.nih.gov/gene/55142):

> The protein encoded by this gene is a subunit of the augmin complex. The augmin complex plays a role in microtubule attachment to the kinetochore and central spindle formation. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:25530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25530) · Entrez [55142](https://www.ncbi.nlm.nih.gov/gene/55142) · UniProt [Q9NVX0](https://www.uniprot.org/uniprotkb/Q9NVX0) · Ensembl [ENSG00000137814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137814)

## Data

Gene col 6072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6072); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6072]; `tensor/DDL_lfc|DDL_z.npy` [6072]; `embed/gene_vectors.npy` [6072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6072 or target_col == 6072). Every well: [[HAUS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAUS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
