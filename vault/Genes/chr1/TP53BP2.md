---
symbol: "TP53BP2"
type: "gene"
col: 6762
ensembl_id: "ENSG00000143514"
name: "tumor protein p53 binding protein 2"
location: "1q41"
module: 14
arm: "+"
pooled_cpm: 105.07
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TP53BP2

*tumor protein p53 binding protein 2* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +18.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.584× (z -8.5, q 1e-14, down in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.777× (z -4.0, q 0.009, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H2347 0.199×, CFPAC-1 0.167×, MIA PaCa-2 0.213×, LOX-IMVI 0.251×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.162×, NCI-H2347 0.209×, CFPAC-1 0.193×, A549 0.376×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.490×; ⚠ cell-cycle shift, explains ~31% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.424×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP3]] (+0.54, fdr 4e-05), [[MYO1B]] (+0.53, fdr 6e-05), [[OGFRL1]] (+0.51, fdr 3e-05); moves opposite to [[LIN52]] (-0.55, fdr 1e-05), [[SLC30A5]] (-0.54, fdr 2e-05), [[NUP88]] (-0.49, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ETS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +18.7 | 0e+00 | 46/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.83×** | +16.9 | 0e+00 | 48/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +9.5 | 5e-19 | 41/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +9.1 | 1e-17 | 40/48 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +8.7 | 3e-16 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.68×** | +8.1 | 5e-14 | 43/48 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +6.8 | 7e-10 | 34/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +6.1 | 7e-08 | 29/48 (KATO III, HT-29, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.1 | 8e-08 | 30/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.1 | 8e-08 | 35/48 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.0 | 8e-08 | 31/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +5.6 | 1e-06 | 31/49 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +5.3 | 5e-06 | 34/48 (HT-29, Hs 766T, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +4.9 | 4e-05 | 29/48 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.7 | 1e-04 | 30/48 (KATO III, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 1e-04 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.4 | 3e-04 | 24/48 (HS-578T, C32, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.005 | 23/48 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.011 | 25/48 (HT-29, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6762.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H2347 0.199×, CFPAC-1 0.167×, MIA PaCa-2 0.213×, LOX-IMVI 0.251×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.162×, NCI-H2347 0.209×, CFPAC-1 0.193×, A549 0.376×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.490×; ⚠ cell-cycle shift, explains ~31% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.424×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.584×** | -8.5 | 1e-14 | 36/49 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -8.1 | 2e-13 | 30/43 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.749×** | -4.4 | 0.002 | 25/47 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.777×** | -4.0 | 0.009 | 24/48 (A549, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.849× | -3.7 | 0.026 | 18/48 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.062 | 21/49 (J82, RKO, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.816× | -3.2 | 0.10 | 23/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.822× | -3.1 | 0.13 | 22/48 (NCI-H23, MIA PaCa-2, …) | two highest doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.873× | -3.1 | 0.13 | 12/49 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.873× | -3.1 | 0.13 | 20/49 (MIA PaCa-2, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 91.9 | 12 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 28.7× (z +20.9) | — |
| [[NCI-H460 (line)]] | wt | 89.6 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.6) | — |
| [[A549 (line)]] | wt | 131 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 61.7 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.3) | — |
| [[LoVo (line)]] | wt | 52.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.0) | — |
| [[SW480 (line)]] | alt | 48.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +15.8) | — |
| [[A498 (line)]] | wt | 192 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +21.4) | — |
| [[CFPAC-1 (line)]] | alt | 247 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 80.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +19.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 171 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 23.3× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -13.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 140 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 54.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 119 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -10.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 192 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +14.5) | — |
| [[Hs 766T (line)]] | wt | 71.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 54.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +14.7) | — |
| [[J82 (line)]] | alt | 155 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.490× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 54.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.18× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 104 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 133 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.6× (z +14.8) | [[Auranofin (drug)]] 5 µM 0.424× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 270 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.96× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -15.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.3) | — |
| [[A-172 (line)]] | wt | 156 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.0) | — |
| [[C32 (line)]] | wt | 49.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 20.9× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 61.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 162 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.4) | — |
| [[RKO (line)]] | wt | 170 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.36× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -16.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 82.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 66.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 65.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 98.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.50× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 74.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 39.7× (z +17.3) | — |
| [[NCI-H2030 (line)]] | alt | 45.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.29× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 62.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP3]] | +0.54 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[MYO1B]] | +0.53 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[OGFRL1]] | +0.51 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ETS1]] | +0.51 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[PALM2AKAP2]] | +0.49 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[AMPD3]] | +0.49 | +0.57 / +0.32 | both halves | 2e-04 |  |
| [[LACC1]] | +0.49 | +0.37 / +0.46 | both halves | 9e-05 |  |
| [[ERC2]] | +0.48 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[OTUD4]] | +0.47 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[FTCDNL1]] | +0.47 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[PAM]] | +0.47 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[TBC1D9]] | +0.47 | +0.36 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN52]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SLC30A5]] | -0.54 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[NUP88]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[XPNPEP3]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[TYW1]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ELP4]] | -0.46 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[UBE2M]] | -0.46 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[LSM7]] | -0.46 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[GLYR1]] | -0.46 | -0.51 / -0.43 | both halves | 4e-05 |  |
| [[PDXDC2P-NPIPB14P]] | -0.45 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[NUP160]] | -0.45 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[GON4L]] | -0.45 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS1]] | B | ETS1 activity raises TP53BP2's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without ETS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.363). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.7, 9.2); signed map (16.7, 37.3). **Vector** length 89.3, 27.3% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +3.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.8 | +4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | +6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.4 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | +6.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | tumor protein p53 binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:223,779,893-223,845,954 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R13A, ASPP2, 53BP2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits; SH3 domain containing |
| Reactome | 12 pathways, smallest: Activation of PUMA and translocation to mitochondria; Regulation of TP53 Activity through Association with Co-factors; TP53 Regulates Transcription of Death Receptors and Ligands |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13625](https://www.uniprot.org/uniprotkb/Q13625) (Apoptosis-stimulating of p53 protein 2):

> Regulator that plays a central role in regulation of apoptosis and cell growth via its interactions with proteins such as TP53. Regulates TP53 by enhancing the DNA binding and transactivation function of TP53 on the promoters of pro-apoptotic genes in vivo. Inhibits the ability of NAE1 to conjugate NEDD8 to CUL1, and thereby decreases NAE1 ability to induce apoptosis. Impedes cell cycle progression at G2/M. Its apoptosis-stimulating activity is inhibited by its interaction with DDX42.

**Summary**, from NCBI Gene [7159](https://www.ncbi.nlm.nih.gov/gene/7159):

> This gene encodes a member of the ASPP (apoptosis-stimulating protein of p53) family of p53 interacting proteins. The protein contains four ankyrin repeats and an SH3 domain involved in protein-protein interactions. It is localized to the perinuclear region of the cytoplasm, and regulates apoptosis and cell growth through interactions with other regulatory molecules including members of the p53 family. Multiple transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:12000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12000) · Entrez [7159](https://www.ncbi.nlm.nih.gov/gene/7159) · UniProt [Q13625](https://www.uniprot.org/uniprotkb/Q13625) · Ensembl [ENSG00000143514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143514)

## Data

Gene col 6762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6762); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6762]; `tensor/DDL_lfc|DDL_z.npy` [6762]; `embed/gene_vectors.npy` [6762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6762 or target_col == 6762). Every well: [[TP53BP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TP53BP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
