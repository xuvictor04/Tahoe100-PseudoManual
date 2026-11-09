---
symbol: "AFTPH"
type: "gene"
col: 4125
ensembl_id: "ENSG00000119844"
name: "aftiphilin"
location: "2p14"
module: 59
arm: "+"
pooled_cpm: 163.13
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# AFTPH

*aftiphilin* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +17.5, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.390× (z -17.7, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.823× (z -3.7, q 0.025, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 13 lines (AsPC-1 0.155×, SW480 0.227×, NCI-H1792 0.229×, A-427 0.254×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.193×, NCI-H2347 0.338×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL28]] (+0.73, fdr 7e-06), [[CIR1]] (+0.72, fdr 7e-06), [[GOLPH3L]] (+0.71, fdr 7e-06); moves opposite to [[PSME3]] (-0.74, fdr 7e-06), [[ABCF2]] (-0.72, fdr 7e-06), [[HCFC1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +17.5 | 0e+00 | 43/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.28×** | +15.5 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +13.7 | 1e-40 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +11.7 | 1e-29 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +11.5 | 2e-28 | 42/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +11.2 | 6e-27 | 45/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +9.5 | 2e-19 | 41/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +7.3 | 2e-11 | 40/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.6 | 3e-09 | 37/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +6.5 | 6e-09 | 37/48 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +6.1 | 4e-08 | 32/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 2e-07 | 33/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 3e-07 | 31/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 1e-05 | 28/48 (C-33 A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.4 | 4e-04 | 20/38 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.005 | 16/49 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.4 | 0.017 | 9/48 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.037 | 1/49 (J82) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4125.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 13 lines (AsPC-1 0.155×, SW480 0.227×, NCI-H1792 0.229×, A-427 0.254×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.193×, NCI-H2347 0.338×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.390×** | -17.7 | 0e+00 | 42/44 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.527×** | -10.9 | 3e-25 | 48/49 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.695×** | -6.6 | 9e-09 | 29/45 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.815×** | -4.0 | 0.009 | 25/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.823×** | -3.7 | 0.025 | 26/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.830×** | -3.6 | 0.025 | 24/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.836× | -3.5 | 0.038 | 21/49 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -3.4 | 0.047 | 0/50 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.843× | -3.3 | 0.053 | 16/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.849× | -3.2 | 0.077 | 19/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.895× | -3.1 | 0.11 | 4/48 (NCI-H661, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 133 | 13 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +24.6) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -11.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 129 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +31.2) | [[Dinaciclib (drug)]] 5 µM 0.492× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 174 | 6 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.55× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -19.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 182 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 163 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -23.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 127 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.92× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 201 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 201 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -18.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 115 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -13.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 202 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +25.1) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -9.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 124 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +17.1) | — |
| [[HT-29 (line)]] | alt | 209 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.95× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -13.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 132 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -16.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 183 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 248 | 3 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.80× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -19.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 217 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -16.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 156 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 144 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 274 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -24.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 136 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 170 | 4 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.44× (z +12.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.513× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 116 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +20.6) | — |
| [[SW48 (line)]] | wt | 164 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +15.7) | — |
| [[HCT15 (line)]] | alt | 201 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -16.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 218 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -13.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 156 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.52× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 123 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +22.2) | — |
| [[A498 (line)]] | wt | 235 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -12.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 163 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -13.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 163 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 129 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -12.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 169 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -11.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 192 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 82.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -19.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 98.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +19.5) | — |
| [[SW1417 (line)]] | alt | 225 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.459× (z -11.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -13.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 119 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.50× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 193 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.86× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 123 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.73× (z +9.3) | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 98.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL28]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[CIR1]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[GOLPH3L]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[KBTBD3]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | +0.68 | +0.53 / +0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[AKAP1-DT]] | +0.67 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[DBP]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PITPNA-AS1]] | +0.67 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[ACBD3]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[KDM5B]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.74 | -0.64 / -0.75 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.72 | -0.63 / -0.74 | both halves | 7e-06 |  |
| [[HCFC1]] | -0.67 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.67 | -0.53 / -0.71 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.67 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[ARMC6]] | -0.66 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[TTL]] | -0.66 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[NUP188]] | -0.65 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[MCM3AP]] | -0.64 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[RBM19]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[LETM1]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity raises AFTPH's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.33× lower at baseline in the lines without MPZL3 | 0.013 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[GRB7]] | B | GRB7 activity raises AFTPH's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without GRB7 | 0.049 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[FAM229B]] | B | FAM229B activity lowers AFTPH's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.27× higher at baseline in the lines without FAM229B | 0.067 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (5.3, -34.7); signed map (-13.3, 3.8). **Vector** length 99.3, 36.0% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | +6.0 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | +3.6 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | -0.4 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +3.2 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +1.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.6 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.1 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.3 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | aftiphilin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:64,524,299-64,593,005 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33965, FLJ20080, FLJ23793, Nbla10388 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ULP2](https://www.uniprot.org/uniprotkb/Q6ULP2) (Aftiphilin):

> Component of clathrin-coated vesicles. Component of the aftiphilin/p200/gamma-synergin complex, which plays roles in AP1G1/AP-1-mediated protein trafficking including the trafficking of transferrin from early to recycling endosomes, and the membrane trafficking of furin and the lysosomal enzyme cathepsin D between the trans-Golgi network (TGN) and endosomes.

**Summary**, from NCBI Gene [54812](https://www.ncbi.nlm.nih.gov/gene/54812):

> Enables clathrin binding activity. Predicted to be involved in protein transport. Located in Golgi apparatus and cytosol. Part of AP-1 adaptor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25951) · Entrez [54812](https://www.ncbi.nlm.nih.gov/gene/54812) · UniProt [Q6ULP2](https://www.uniprot.org/uniprotkb/Q6ULP2) · Ensembl [ENSG00000119844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119844)

## Data

Gene col 4125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4125); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4125]; `tensor/DDL_lfc|DDL_z.npy` [4125]; `embed/gene_vectors.npy` [4125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4125 or target_col == 4125). Every well: [[AFTPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFTPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
