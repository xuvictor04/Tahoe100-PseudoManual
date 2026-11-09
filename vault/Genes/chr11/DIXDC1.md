---
symbol: "DIXDC1"
type: "gene"
col: 7459
ensembl_id: "ENSG00000150764"
name: "DIX domain containing 1"
location: "11q23.1"
module: 17
arm: "+"
pooled_cpm: 31.63
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 34
n_dd_up_clean: 35
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DIXDC1

*DIX domain containing 1* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.79× (z +20.7, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.367× (z -20.2, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF150]] (+0.66, fdr 7e-06), [[DYNC2H1]] (+0.66, fdr 1e-05), [[CNTNAP1]] (+0.63, fdr 7e-06); moves opposite to [[QRICH2]] (-0.60, fdr 6e-05), [[TLNRD1]] (-0.58, fdr 1e-05), [[DDX5]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KDM2B-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 3 with an alert ⚠; shown: the 15 strongest. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +20.7 | 0e+00 | 42/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.37×** | +17.4 | 0e+00 | 41/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +16.7 | 0e+00 | 41/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.15×** | +15.5 | 0e+00 | 43/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +13.3 | 3e-38 | 34/48 (KATO III, SW1417, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.87×** | +12.6 | 2e-34 | 37/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.72×** | +10.9 | 8e-26 | 43/48 (SW1417, C-33 A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +9.1 | 8e-18 | 30/48 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.22×** | +8.4 | 3e-15 | 37/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +8.2 | 2e-14 | 29/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +7.1 | 5e-11 | 24/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 2e-09 | 28/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +6.5 | 3e-09 | 29/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +6.0 | 1e-07 | 24/48 (NCI-H1792, hTERT-HPNE, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.32×** | +5.6 | 1e-06 | 18/48 (HEC-1-A, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7459.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.367×** | -20.2 | 0e+00 | 42/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -17.6 | 0e+00 | 36/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.436×** | -16.7 | 0e+00 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.440×** | -15.9 | 0e+00 | 39/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.506×** | -13.7 | 8e-41 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.745×** | -8.4 | 4e-15 | 27/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -7.8 | 4e-13 | 25/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.718×** | -6.4 | 9e-09 | 26/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.731×** | -6.3 | 1e-08 | 28/48 (PANC-1, SW 1088, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.708×** | -6.3 | 1e-08 | 24/48 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.746×** | -5.9 | 2e-07 | 23/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.756×** | -5.6 | 8e-07 | 24/48 (H4, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.714×** | -5.6 | 1e-06 | 18/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.760×** | -5.5 | 1e-06 | 20/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Lucanthone (drug)]] 5 µM |  | **0.754×** | -5.5 | 2e-06 | 19/48 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -5.4 | 3e-06 | 19/48 (LOX-IMVI, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.723×** | -4.7 | 9e-05 | 15/48 (SK-MEL-2, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.647×** | -4.6 | 1e-04 | 13/48 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.9 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -16.8) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.186× (z -14.9) |
| [[PANC-1 (line)]] | alt | 47.5 | 6 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +12.7) | [[Digitoxin (drug)]] 0.5 µM 0.322× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 45.6 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.3) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.145× (z -11.1) |
| [[SW480 (line)]] | alt | 40.4 | 3 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.245× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.285× (z -13.3) |
| [[C32 (line)]] | wt | 69.0 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -17.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -14.4) |
| [[SW1417 (line)]] | alt | 35.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +21.1) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +11.6) | — |
| [[KATO III (line)]] | alt | 35.8 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 18.5 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.30× (z +10.5) | [[Digitoxin (drug)]] 0.5 µM 0.207× (z -9.9) |
| [[C-33 A (line)]] | alt | 107 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.288× (z -10.8) |
| [[HCT15 (line)]] | alt | 44.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -11.7) |
| [[Hs 766T (line)]] | wt | 32.2 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.183× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -9.5) |
| [[A-172 (line)]] | wt | 39.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 41.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 12.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.95× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.64× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 17.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +11.2) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Selinexor (drug)]] 5 µM 2.57× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.176× (z -8.8) |
| [[SNU-423 (line)]] | alt | 16.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.10× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.163× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.1 | 1 | 0 | [[Triamcinolone (drug)]] 0.5 µM 2.36× (z +8.6) | — |
| [[A549 (line)]] | wt | 10.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.79× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 73.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -9.9) |
| [[CHP-212 (line)]] | wt | 71.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -9.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +12.4) ⚠ position not correctable | — |
| [[J82 (line)]] | alt | 17.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 9.46 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.71× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 45.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 60.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -9.8) |
| [[SHP-77 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.187× (z -8.9) |
| [[A-427 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF150]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[DYNC2H1]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[CNTNAP1]] | +0.63 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RRAGD]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PPP1R3C]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[FLVCR2]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ALDH7A1]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC44A2]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ARL6]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PEX3]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A12]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRICH2]] | -0.60 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[TLNRD1]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[DDX5]] | -0.58 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ANKMY1]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[NEK10]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.57 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ZNF800]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TBILA]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[CLCF1]] | -0.54 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[RAB22A]] | -0.54 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[MUC20-OT1]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[MSRA]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM2B-DT]] | B | KDM2B-DT activity raises DIXDC1's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without KDM2B-DT | 0.073 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[ABL1]] | B | ABL1 activity lowers DIXDC1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 6.4% of all compounds | 0.081 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CNTNAP1]] | C | CNTNAP1 activity raises DIXDC1's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CNTNAP1 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (15.6, -11.2); signed map (-26.5, -10.6). **Vector** length 108, 30.4% of its response variance represented; |z| ≥ 3 in 1,670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.2 | +13.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.3 | +12.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.7 | +15.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.5 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.9 | +10.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.3 | +0.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.0 | +3.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +3.0 | +4.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.0 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.9 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.3 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | DIX domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:111,927,144-112,022,653 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1735, Dixin |
| Gene groups (HGNC) | Dishevelled segment polarity proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q155Q3](https://www.uniprot.org/uniprotkb/Q155Q3) (Dixin):

> Positive effector of the Wnt signaling pathway; activates WNT3A signaling via DVL2. Regulates JNK activation by AXIN1 and DVL2.

**Summary**, from NCBI Gene [85458](https://www.ncbi.nlm.nih.gov/gene/85458):

> The protein encoded by this gene is a positive regulator of the Wnt signaling pathway. The encoded protein is found associated with gamma tubulin at the centrosome. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:23695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23695) · Entrez [85458](https://www.ncbi.nlm.nih.gov/gene/85458) · UniProt [Q155Q3](https://www.uniprot.org/uniprotkb/Q155Q3) · Ensembl [ENSG00000150764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150764)

## Data

Gene col 7459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7459); `tables/drug_effects.parquet` (106 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7459]; `tensor/DDL_lfc|DDL_z.npy` [7459]; `embed/gene_vectors.npy` [7459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7459 or target_col == 7459). Every well: [[DIXDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIXDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
