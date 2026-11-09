---
symbol: "SUPT20H"
type: "gene"
col: 2263
ensembl_id: "ENSG00000102710"
name: "SPT20 homolog, SAGA complex component"
location: "13q13.3"
module: 28
arm: "+"
pooled_cpm: 64.58
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SUPT20H

*SPT20 homolog, SAGA complex component* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +21.1, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.513× (z -17.0, q 0e+00, down in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.520× (z -16.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.77, fdr 7e-06), [[FAM114A2]] (+0.73, fdr 7e-06), [[MRPS31]] (+0.70, fdr 1e-05); moves opposite to [[SLC6A16]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +21.1 | 0e+00 | 40/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +14.7 | 0e+00 | 41/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +13.2 | 2e-37 | 41/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +10.0 | 3e-21 | 39/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +8.6 | 9e-16 | 35/49 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +5.7 | 9e-07 | 26/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +4.7 | 2e-04 | 23/48 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.6 | 3e-04 | 17/48 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 3e-04 | 22/48 (RKO, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.4 | 6e-04 | 21/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.022 | 10/48 (J82, NCI-H23, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.10× | +3.3 | 0.053 | 1/48 (HEC-1-A) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.069 | 7/49 (SW480, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -17.0 | 0e+00 | 40/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.520×** | -16.6 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -13.6 | 7e-40 | 45/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -12.4 | 4e-33 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.593×** | -10.1 | 4e-22 | 30/44 (RPMI-7951, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.745×** | -7.5 | 6e-12 | 32/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.790×** | -5.8 | 7e-07 | 24/47 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | **0.807×** | -5.5 | 3e-06 | 25/49 (COLO 205, LoVo, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.821×** | -5.0 | 3e-05 | 22/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | 0.839× | -4.3 | 9e-04 | 18/41 (SHP-77, C-33 A, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.853× | -3.9 | 0.005 | 18/47 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.867× | -3.7 | 0.012 | 13/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | 0.879× | -3.3 | 0.042 | 10/49 (NCI-H23, Panc 03.27, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.882× | -3.2 | 0.054 | 16/48 (MIA PaCa-2, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 64.5 | 4 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +17.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -20.0) |
| [[HT-29 (line)]] | alt | 90.5 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.476× (z -9.0) |
| [[LS 180 (line)]] | wt | 54.8 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 56.1 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.196× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.374× (z -12.7) |
| [[RKO (line)]] | wt | 70.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[A-427 (line)]] | wt | 54.9 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.00× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 70.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +17.1) | — |
| [[KATO III (line)]] | alt | 82.0 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.220× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.9) | [[Auranofin (drug)]] 5 µM 0.459× (z -8.5) |
| [[PANC-1 (line)]] | alt | 55.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 101 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 43.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.399× (z -9.1) |
| [[BT-474 (line)]] | alt | 62.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.231× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -10.8) |
| [[COLO 205 (line)]] | alt | 150 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -12.9) |
| [[HCT15 (line)]] | alt | 84.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 61.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -12.5) |
| [[J82 (line)]] | alt | 98.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.467× (z -11.3) |
| [[SW 900 (line)]] | alt | 62.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.386× (z -9.7) |
| [[SW1417 (line)]] | alt | 52.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.405× (z -10.0) |
| [[C-33 A (line)]] | alt | 68.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.291× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 53.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -9.6) |
| [[Hs 766T (line)]] | wt | 87.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 48.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.393× (z -9.2) |
| [[LoVo (line)]] | wt | 44.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[LOX-IMVI (line)]] | wt | 69.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.437× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 71.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.8) | — |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.512× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.517× (z -9.3) |
| [[SW 1088 (line)]] | alt | 70.7 | 0 | 2 | — | [[Macitentan (drug)]] 0.5 µM 0.0536× (z -10.0) |
| [[A498 (line)]] | wt | 98.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -10.7) ⚠ cell-cycle shift, explains ~10% of this change |
| [[CFPAC-1 (line)]] | alt | 40.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 54.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 47.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 32.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.497× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.271× (z -10.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 21.2 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.149× (z -8.6) |
| [[A-172 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.77 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[FAM114A2]] | +0.73 | +0.81 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[MRPS31]] | +0.70 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[SUCLG1]] | +0.69 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[CEP63]] | +0.68 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.68 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.67 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[IFT74]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[CETN3]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[PEX12]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A16]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.5, 3.8); signed map (6.7, -24.8). **Vector** length 113, 29.5% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +13.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.4 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +21.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.9 | -17.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -9.8 | -13.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -9.4 | -12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -8.7 | -16.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SPT20 homolog, SAGA complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:37,009,312-37,059,713 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPT20, bA421P11.4, P38IP; previously C13orf19, FAM48A |
| Gene groups (HGNC) | SAGA complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEM7](https://www.uniprot.org/uniprotkb/Q8NEM7) (Transcription factor SPT20 homolog):

> Required for MAP kinase p38 (MAPK11, MAPK12, MAPK13 and/or MAPK14) activation during gastrulation. Required for down-regulation of E-cadherin during gastrulation by regulating E-cadherin protein level downstream from NCK-interacting kinase (NIK) and independently of the regulation of transcription by FGF signaling and Snail (By similarity). Required for starvation-induced ATG9A trafficking during autophagy.

**Summary**, from NCBI Gene [55578](https://www.ncbi.nlm.nih.gov/gene/55578):

> Predicted to enable transcription coregulator activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Part of SAGA-type complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20596) · Entrez [55578](https://www.ncbi.nlm.nih.gov/gene/55578) · UniProt [Q8NEM7](https://www.uniprot.org/uniprotkb/Q8NEM7) · Ensembl [ENSG00000102710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102710)

## Data

Gene col 2263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2263); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2263]; `tensor/DDL_lfc|DDL_z.npy` [2263]; `embed/gene_vectors.npy` [2263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2263 or target_col == 2263). Every well: [[SUPT20H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUPT20H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
