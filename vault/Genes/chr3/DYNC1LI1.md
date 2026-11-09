---
symbol: "DYNC1LI1"
type: "gene"
col: 6905
ensembl_id: "ENSG00000144635"
name: "dynein cytoplasmic 1 light intermediate chain 1"
location: "3p22.3"
module: 169
arm: "+"
pooled_cpm: 54.8
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# DYNC1LI1

*dynein cytoplasmic 1 light intermediate chain 1* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.16× (z +14.8, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.588× (z -9.8, q 4e-20, down in 34 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.790× (z -4.4, q 0.002, down in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-427 0.128×, LS 180 0.0970×, SW1417 0.168×, SW48 0.109×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LOX-IMVI 0.316×, Panc 03.27 0.329×, A-172 0.414×, SNU-1 0.293×, …; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.302×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf87]] (+0.67, fdr 1e-05), [[PAPOLG]] (+0.63, fdr 2e-05), [[MACIR]] (+0.62, fdr 1e-05); moves opposite to [[DAP]] (-0.58, fdr 3e-05), [[LINC00641]] (-0.52, fdr 6e-05), [[SCART1]] (-0.51, fdr 4e-05).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +14.8 | 0e+00 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.65×** | +13.7 | 3e-40 | 38/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.93×** | +12.6 | 4e-34 | 44/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +12.4 | 5e-33 | 46/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +11.0 | 4e-26 | 43/48 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +10.8 | 5e-25 | 36/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +10.0 | 1e-21 | 43/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +9.7 | 2e-20 | 38/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +8.6 | 7e-16 | 40/48 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +7.7 | 7e-13 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.9 | 3e-10 | 30/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +6.8 | 4e-10 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.8 | 4e-10 | 36/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +6.7 | 8e-10 | 31/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +6.1 | 4e-08 | 30/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.4 | 2e-06 | 29/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 3e-06 | 33/49 (PANC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 6e-06 | 28/48 (CFPAC-1, PANC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6905.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-427 0.128×, LS 180 0.0970×, SW1417 0.168×, SW48 0.109×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LOX-IMVI 0.316×, Panc 03.27 0.329×, A-172 0.414×, SNU-1 0.293×, …; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.302×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -9.8 | 4e-20 | 34/42 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.707×** | -6.7 | 8e-09 | 26/48 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -5.4 | 1e-05 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.790×** | -4.4 | 0.002 | 24/49 (AsPC-1, SW1417, …) | top dose only | plate-row cell shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.837× | -3.4 | 0.073 | 12/48 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.834× | -3.3 | 0.077 | 16/48 (AsPC-1, CHP-212, …) | top dose only | plate-row cell shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.830×** | -3.3 | 0.077 | 20/45 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.838× | -3.3 | 0.077 | 13/48 (hTERT-HPNE, LS 180, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.12 | 10/48 (Panc 03.27, CHP-212, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.844× | -3.0 | 0.15 | 9/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.7 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +16.7) | — |
| [[LoVo (line)]] | wt | 36.1 | 7 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.19× (z +12.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.85× (z +11.3) | — |
| [[SW480 (line)]] | alt | 63.6 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +14.3) | — |
| [[LS 180 (line)]] | wt | 37.3 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0970× (z -19.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 48.1 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 106 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -18.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 39.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +10.3) | — |
| [[C32 (line)]] | wt | 38.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.01× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 51.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +10.8) | — |
| [[KATO III (line)]] | alt | 34.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 80.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 50.1 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.31× (z +9.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +8.9) | — |
| [[SW48 (line)]] | wt | 67.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.23× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.109× (z -16.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 67.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -17.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 71.4 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.14× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -23.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 64.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -10.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 87.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 45.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +9.0) | — |
| [[A498 (line)]] | wt | 37.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 68.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C-33 A (line)]] | alt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -13.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -13.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 72.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 88.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 84.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.302× (z -40.8) |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf87]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[PAPOLG]] | +0.63 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[MACIR]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[TLK2]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[RBM27]] | +0.57 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[MARCHF5]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MRPL32]] | +0.56 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[FHIP2A]] | +0.56 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[RNF135]] | +0.55 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ZC2HC1A]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.55 | +0.35 / +0.61 | both halves | 1e-04 | pathway: Asparagine N-linked glycosylation |
| [[ARL8A]] | +0.55 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAP]] | -0.58 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[LINC00641]] | -0.52 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[SCART1]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SEC16A]] | -0.50 | -0.57 / -0.48 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[ARL5B]] | -0.48 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[SYS1-DBNDD2]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[AP1B1]] | -0.47 | -0.36 / -0.33 | both halves | 1e-04 | pathway: MHC class II antigen presentation |
| [[ENSA]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[EPN1]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[CALU]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ETF1]] | -0.45 | -0.29 / -0.53 | both halves | 3e-04 |  |
| [[CLTC]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 | pathway: MHC class II antigen presentation |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.6, -7.5); signed map (-22.6, -8.0). **Vector** length 77.0, 19.2% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.4 | +12.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +11.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +2.7 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.5 | +6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | +6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +6.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | +1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | +0.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | dynein cytoplasmic 1 light intermediate chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:32,525,974-32,570,858 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DNCLI1 |
| Gene groups (HGNC) | Dynein 1 complex subunits; Dynein light intermediate chains |
| Reactome | 43 pathways, smallest: Aggrephagy; COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6G9](https://www.uniprot.org/uniprotkb/Q9Y6G9) (Cytoplasmic dynein 1 light intermediate chain 1):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function. Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and organelles along microtubules. May play a role in binding dynein to membranous organelles or chromosomes. Probably involved in the microtubule-dependent transport of pericentrin. Is required for …

**Summary**, from NCBI Gene [51143](https://www.ncbi.nlm.nih.gov/gene/51143):

> The protein encoded by this gene belongs to light intermediate subunit family, whose members are components of the multiprotein cytoplasmic dynein complex, which is involved in intracellular trafficking and chromosome segregation during mitosis. The protein plays a role in moving the spindle assembly checkpoint (SAC) from kinetochores to spindle poles. The protein may also mediate binding to other cargo molecules to facilitate intracellular vesicle trafficking. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:18745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18745) · Entrez [51143](https://www.ncbi.nlm.nih.gov/gene/51143) · UniProt [Q9Y6G9](https://www.uniprot.org/uniprotkb/Q9Y6G9) · Ensembl [ENSG00000144635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144635)

## Data

Gene col 6905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6905); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6905]; `tensor/DDL_lfc|DDL_z.npy` [6905]; `embed/gene_vectors.npy` [6905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6905 or target_col == 6905). Every well: [[DYNC1LI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC1LI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
