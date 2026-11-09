---
symbol: "GAB1"
type: "gene"
col: 3052
ensembl_id: "ENSG00000109458"
name: "GRB2 associated binding protein 1"
location: "4q31.21"
module: 145
arm: "+"
pooled_cpm: 94.52
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 49
n_dd_up_clean: 0
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# GAB1

*GRB2 associated binding protein 1* — 4q31.21

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.41×, LoVo 1.68×; ⚠ cell-cycle shift, explains ~39% of this change).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (25 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.385× (z -22.1, q 0e+00, down in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.303× (z -19.6, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC16]] (+0.60, fdr 3e-05), [[FOXO3]] (+0.58, fdr 3e-05), [[MXI1]] (+0.57, fdr 1e-05); moves opposite to [[ANAPC1P4]] (-0.52, fdr 3e-05), [[FARSB]] (-0.52, fdr 1e-05), [[DNAJA3]] (-0.51, fdr 5e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3052.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.41×, LoVo 1.68×; ⚠ cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.25× | +3.5 | 0.15 | 20/45 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.50× | +3.5 | 0.15 | 22/48 (LoVo, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.21× | +3.1 | 0.31 | 14/46 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.21× | +3.1 | 0.31 | 20/48 (SK-MEL-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 26 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.385×** | -22.1 | 0e+00 | 39/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.277×** | -20.3 | 0e+00 | 37/40 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.303×** | -19.6 | 0e+00 | 43/46 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.339×** | -17.8 | 0e+00 | 42/47 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.366×** | -16.5 | 0e+00 | 43/46 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.358×** | -16.2 | 0e+00 | 42/46 (NCI-H460, SW48, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.349×** | -16.0 | 0e+00 | 39/42 (H4, C32, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.401×** | -15.0 | 0e+00 | 40/46 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.448×** | -13.2 | 9e-38 | 35/46 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.485×** | -11.9 | 1e-30 | 41/46 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.492×** | -11.6 | 2e-29 | 41/46 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.503×** | -11.3 | 1e-27 | 41/46 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.512×** | -11.0 | 2e-26 | 38/46 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.278×** | -11.0 | 2e-26 | 42/47 (H4, HCT15, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.530×** | -10.4 | 1e-23 | 37/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.658×** | -6.9 | 2e-10 | 36/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.463×** | -6.6 | 1e-09 | 30/46 (C-33 A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.619×** | -6.3 | 5e-09 | 36/46 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.562×** | -4.9 | 2e-05 | 32/46 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.572×** | -4.8 | 3e-05 | 32/46 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.748×** | -4.6 | 8e-05 | 28/46 (SW 900, NCI-H2030, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.589×** | -4.5 | 1e-04 | 30/46 (SW1417, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.760×** | -4.5 | 1e-04 | 26/45 (HOP62, MIA PaCa-2, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.614×** | -4.2 | 5e-04 | 24/46 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.5 | 0 | 20 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -19.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.171× (z -19.1) |
| [[MIA PaCa-2 (line)]] | alt | 66.6 | 0 | 18 (12 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -15.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.218× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 193 | 0 | 17 (13 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -17.6) |
| [[SNU-1 (line)]] | wt | 139 | 0 | 16 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -15.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.276× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 301 | 0 | 15 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.227× (z -15.3) |
| [[A-172 (line)]] | wt | 82.3 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -21.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -16.4) |
| [[HT-29 (line)]] | alt | 341 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -16.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.186× (z -15.0) |
| [[SNU-423 (line)]] | alt | 81.4 | 0 | 13 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -19.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 106 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -17.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 169 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0608× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -17.0) |
| [[SW1417 (line)]] | alt | 127 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -10.5) |
| [[A-427 (line)]] | wt | 125 | 0 | 10 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.195× (z -16.1) |
| [[C32 (line)]] | wt | 152 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.252× (z -15.0) |
| [[HOP62 (line)]] | alt | 74.9 | 0 | 10 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 53.1 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -17.8) |
| [[Panc 03.27 (line)]] | alt | 154 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0389× (z -29.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -11.5) |
| [[PANC-1 (line)]] | alt | 27.4 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -17.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.251× (z -11.7) |
| [[A549 (line)]] | wt | 62.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -18.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -18.0) |
| [[COLO 205 (line)]] | alt | 84.5 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -14.0) |
| [[HCT15 (line)]] | alt | 109 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -18.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 131 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -14.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -14.5) |
| [[HS-578T (line)]] | alt | 61.6 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -12.4) |
| [[SW48 (line)]] | wt | 87.2 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -18.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -15.0) |
| [[SW480 (line)]] | alt | 32.9 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -12.6) |
| [[C-33 A (line)]] | alt | 173 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -11.1) |
| [[LoVo (line)]] | wt | 99.6 | 1 (1 ⚠) | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 131 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -11.7) |
| [[BT-474 (line)]] | alt | 94.3 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -12.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 96.4 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -9.8) |
| [[Hs 766T (line)]] | wt | 64.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -14.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 43.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0895× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.174× (z -19.3) |
| [[AN3 CA (line)]] | alt | 141 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0655× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.204× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 59.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -10.5) |
| [[SW 900 (line)]] | alt | 59.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -9.6) |
| [[A498 (line)]] | wt | 81.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -9.7) |
| [[H4 (line)]] | wt | 96.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0505× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.279× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 96.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.366× (z -9.2) |
| [[CHP-212 (line)]] | wt | 152 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0771× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[vincristine (drug)]] 5 µM 0.0597× (z -9.0) |
| [[RKO (line)]] | wt | 39.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.2) ⚠ cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -8.8) |
| [[J82 (line)]] | alt | 58.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 7.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | +0.60 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[FOXO3]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[MXI1]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PHLPP1]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 | same gene group; pathway: Intracellular signaling by second messengers |
| [[LNX2]] | +0.55 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[NARF]] | +0.54 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TBC1D12]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PPP2R5A]] | +0.53 | +0.57 / +0.50 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[AAMDC]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PIK3CA]] | +0.53 | +0.57 / +0.48 | both halves | 2e-05 | pathway: Activated NTRK2 signals through PI3K; STRING 920 |
| [[PPM1D]] | +0.53 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[CNOT6L]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC1P4]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[FARSB]] | -0.52 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[DNAJA3]] | -0.51 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[ZNF81]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TIMM23B-AGAP6]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZNF202]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NAV3]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[NAA15]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[FKTN]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[AGAP6]] | -0.49 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MAK16]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SRFBP1]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.444). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.9, -38.9); signed map (-20.0, 15.8). **Vector** length 77.1, 23.9% of its response variance represented; |z| ≥ 3 in 1,681 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.7 | -5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.1 | -13.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.7 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | -0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.6 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -16.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.1 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.0 | -16.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -19.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -11.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | GRB2 associated binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:143,336,876-143,474,565 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNB26 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes |
| Reactome | 59 pathways, smallest: MET activates PTPN11; Activated NTRK2 signals through PI3K; MET activates PI3K/AKT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13480](https://www.uniprot.org/uniprotkb/Q13480) (GRB2-associated-binding protein 1):

> Adapter protein that plays a role in intracellular signaling cascades triggered by activated receptor-type kinases. Plays a role in FGFR1 signaling. Probably involved in signaling by the epidermal growth factor receptor (EGFR) and the insulin receptor (INSR). Involved in the MET/HGF-signaling pathway.

**Summary**, from NCBI Gene [2549](https://www.ncbi.nlm.nih.gov/gene/2549):

> The protein encoded by this gene is a member of the IRS1-like multisubstrate docking protein family. It is an important mediator of branching tubulogenesis and plays a central role in cellular growth response, transformation and apoptosis. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:4066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4066) · Entrez [2549](https://www.ncbi.nlm.nih.gov/gene/2549) · UniProt [Q13480](https://www.uniprot.org/uniprotkb/Q13480) · Ensembl [ENSG00000109458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109458)

## Data

Gene col 3052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3052); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3052]; `tensor/DDL_lfc|DDL_z.npy` [3052]; `embed/gene_vectors.npy` [3052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3052 or target_col == 3052). Every well: [[GAB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
