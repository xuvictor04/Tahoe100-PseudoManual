---
symbol: "LGALS3"
type: "gene"
col: 5264
ensembl_id: "ENSG00000131981"
name: "galectin 3"
location: "14q22.3"
module: 14
arm: "+"
pooled_cpm: 118.43
n_lines_expressing: 39
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 14
direction_downstream: 36
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# LGALS3

*galectin 3* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +12.4, q 1e-32, up in 34 of 37 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.58× (z +5.8, q 6e-07, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.310× (z -14.8, q 0e+00, down in 36 of 37 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.341× (z -13.6, q 1e-39, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LITAF]] (+0.68, fdr 7e-06), [[LMNA]] (+0.67, fdr 7e-06), [[RHOU]] (+0.65, fdr 7e-06); moves opposite to [[RNF4]] (-0.64, fdr 1e-05), [[TRAPPC10]] (-0.62, fdr 1e-05), [[PPM1F]] (-0.62, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TRIM29]] → it (grade B ⚠); 36 go from it, the strongest it → [[RNGTT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.00×** | +12.4 | 1e-32 | 34/37 (SW1417, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.28×** | +10.4 | 5e-23 | 34/37 (SW1417, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.4 | 5e-15 | 32/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.00×** | +8.4 | 5e-15 | 34/37 (SW1417, SW 900, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.7 | 1e-12 | 24/35 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.8 | 6e-07 | 29/37 (SW 900, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.2 | 0.002 | 28/35 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.012 | 25/37 (NCI-H460, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.048 | 23/37 (CFPAC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.087 | 18/37 (NCI-H460, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.100 | 20/38 (HS-578T, AsPC-1, …) | top dose only | position effect removed |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.100 | 20/38 (NCI-H2347, LS 180, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.310×** | -14.8 | 0e+00 | 36/37 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.341×** | -13.6 | 1e-39 | 34/37 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.428×** | -10.7 | 1e-24 | 35/37 (HOP62, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.646×** | -7.8 | 9e-13 | 26/38 (C32, HT-29, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.600×** | -6.4 | 1e-08 | 33/37 (MIA PaCa-2, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.674×** | -5.0 | 6e-05 | 25/37 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -4.5 | 5e-04 | 27/38 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.531×** | -4.2 | 0.002 | 27/37 (NCI-H460, CHP-212, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.010 | 23/37 (AsPC-1, LS 180, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.568×** | -3.7 | 0.011 | 22/36 (LoVo, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.749×** | -3.5 | 0.023 | 20/37 (C32, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.032 | 17/37 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.032 | 18/37 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.775×** | -3.2 | 0.053 | 18/36 (H4, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.778×** | -3.2 | 0.057 | 19/37 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.766×** | -3.2 | 0.057 | 18/37 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.783×** | -3.1 | 0.068 | 19/37 (A498, RPMI-7951, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.787×** | -3.0 | 0.075 | 15/37 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.787×** | -3.0 | 0.075 | 18/37 (NCI-H2347, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 106 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.244× (z -15.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.303× (z -12.9) |
| [[HOP62 (line)]] | alt | 103 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.6) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.165× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.191× (z -12.9) |
| [[LoVo (line)]] | wt | 232 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -15.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.247× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 167 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 118 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 3.24× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 95.7 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +17.3) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.286× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.329× (z -9.3) |
| [[SW1417 (line)]] | alt | 228 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +18.4) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.431× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.467× (z -8.9) |
| [[SW48 (line)]] | wt | 284 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.283× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 204 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.7) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -10.8) |
| [[C32 (line)]] | wt | 311 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -15.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -14.2) |
| [[COLO 205 (line)]] | alt | 132 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.0) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -10.8) |
| [[KATO III (line)]] | alt | 174 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.27× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.310× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.393× (z -10.2) |
| [[LS 180 (line)]] | wt | 280 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.263× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 162 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -15.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.222× (z -12.2) |
| [[A-172 (line)]] | wt | 80.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 5 µM 0.330× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 65.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -9.4) |
| [[J82 (line)]] | alt | 32.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +16.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.341× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 306 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 68.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +11.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[HEC-1-A (line)]] | alt | 39.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 75.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.286× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 86.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 139 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 106 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -9.2) |
| [[SNU-423 (line)]] | alt | 57.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.7) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -10.1) |
| [[SW 1088 (line)]] | alt | 291 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0791× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 92.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 271 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.509× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 203 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 93.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 96.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LITAF]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[LMNA]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[RHOU]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[GATA6]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[BCL3]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[BHLHE41]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SLC6A7]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PIM3]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MARCKS]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CPEB2]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF4]] | -0.64 | -0.60 / -0.53 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[TRAPPC10]] | -0.62 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[PPM1F]] | -0.62 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[STARD3]] | -0.61 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[ARPC5L]] | -0.59 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[THOC5]] | -0.59 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.59 | -0.68 / -0.43 | both halves | 3e-05 | pathway: HALLMARK_APOPTOSIS |
| [[GPR89A]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.59 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.59 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.59 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[PGS1]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 9, C 5. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM29]] | B | TRIM29 activity raises LGALS3's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without TRIM29 | 0.005 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[RASEF]] | B | RASEF activity raises LGALS3's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without RASEF | 0.006 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[NFATC2]] | B | NFATC2 activity raises LGALS3's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 2.60× lower at baseline in the lines without NFATC2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[KMO]] | B | KMO activity raises LGALS3's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without KMO | 0.038 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[CX3CL1]] | B | CX3CL1 activity raises LGALS3's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 2.28× lower at baseline in the lines without CX3CL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[TNFAIP2]] | B | TNFAIP2 activity raises LGALS3's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without TNFAIP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[ABCG2]] | B | ABCG2 activity raises LGALS3's level | lines that do not express ABCG2 (15) vs lines expressing it (35) | 2.34× lower at baseline in the lines without ABCG2 | 0.086 | ⚠ within organs, on part of the lines; also absent: C1R, GBP4, CDK18; maybe low, not absent |
| [[RRAD]] | B | RRAD activity raises LGALS3's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.40× lower at baseline in the lines without RRAD | 0.096 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[SLC6A7]] | B | SLC6A7 activity raises LGALS3's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without SLC6A7 | 0.096 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9 |
| [[STAT5A]] | C | STAT5A activity raises LGALS3's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 5.03× lower at baseline in the lines without STAT5A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2; co-absent with the target |
| [[ADGRG1]] | C | ADGRG1 activity raises LGALS3's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 3.46× lower at baseline in the lines without ADGRG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526; co-absent with the target |
| [[ETS2]] | C | ETS2 activity raises LGALS3's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 4.31× lower at baseline in the lines without ETS2 | 0.030 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 32, C 4. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNGTT]] | B | LGALS3 activity lowers RNGTT's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.57× higher at baseline in the lines without LGALS3 | 0.002 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[THOC5]] | B | LGALS3 activity lowers THOC5's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.55× higher at baseline in the lines without LGALS3 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[PRIM2]] | B | LGALS3 activity lowers PRIM2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.72× higher at baseline in the lines without LGALS3 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[SNRNP40]] | B | LGALS3 activity lowers SNRNP40's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.64× higher at baseline in the lines without LGALS3 | 0.008 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[LMNA]] | B | LGALS3 activity raises LMNA's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without LGALS3 | 0.011 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[RASEF]] | B | LGALS3 activity raises RASEF's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 4.29× lower at baseline in the lines without LGALS3 | 0.011 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[TNFAIP2]] | B | LGALS3 activity raises TNFAIP2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 4.05× lower at baseline in the lines without LGALS3 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[LITAF]] | B | LGALS3 activity raises LITAF's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without LGALS3 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[ORC2]] | B | LGALS3 activity lowers ORC2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.38× higher at baseline in the lines without LGALS3 | 0.025 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[THOC5]] | B | LGALS3 activity strengthens THOC5's drug response | lines that do not express LGALS3 (11) vs lines expressing it (37) | the lines without LGALS3 respond 0.51× as strongly (z diff +0.97); strongest at Topotecan (hydrochloride) 5 µM: 0.76x vs 1.44x (z diff +3.2) | 0.033 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1; target measured in part of the lines; artifact flags |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | LGALS3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express LGALS3 (11) vs lines expressing it (37) | the lines without LGALS3: 0.88× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[KLF4]] | B | LGALS3 activity raises KLF4's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without LGALS3 | 0.035 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 1.4); signed map (47.5, 11.2). **Vector** length 128, 41.8% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +13.4 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +10.6 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +10.4 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.2 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -6.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -4.0 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | galectin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:55,124,110-55,145,423 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAC-2, GALIG; previously LGALS2 |
| Gene groups (HGNC) | Receptor ligands; Galectins |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, APOPTOSIS, COMPLEMENT |
| Reactome | 7 pathways, smallest: RUNX2 regulates genes involved in differentiation of myeloid cells; RUNX1 regulates transcription of genes involved in differentiation of myeloid cells; Advanced glycosylation endproduct receptor signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P17931](https://www.uniprot.org/uniprotkb/P17931) (Galectin-3):

> Galactose-specific lectin which binds IgE. May mediate with the alpha-3, beta-1 integrin the stimulation by CSPG4 of endothelial cells migration. Together with DMBT1, required for terminal differentiation of columnar epithelial cells during early embryogenesis (By similarity). In the nucleus: acts as a pre-mRNA splicing factor. Involved in acute inflammatory responses including neutrophil activation and adhesion, chemoattraction of monocytes macrophages, opsonization of apoptotic neutrophils, …

**Summary**, from NCBI Gene [3958](https://www.ncbi.nlm.nih.gov/gene/3958):

> This gene encodes a member of the galectin family of carbohydrate binding proteins. Members of this protein family have an affinity for beta-galactosides. The encoded protein is characterized by an N-terminal proline-rich tandem repeat domain and a single C-terminal carbohydrate recognition domain. This protein can self-associate through the N-terminal domain allowing it to bind to multivalent saccharide ligands. This protein localizes to the extracellular matrix, the cytoplasm and the nucleus. …

**Accessions** — [HGNC:6563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6563) · Entrez [3958](https://www.ncbi.nlm.nih.gov/gene/3958) · UniProt [P17931](https://www.uniprot.org/uniprotkb/P17931) · Ensembl [ENSG00000131981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131981)

## Data

Gene col 5264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5264); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5264]; `tensor/DDL_lfc|DDL_z.npy` [5264]; `embed/gene_vectors.npy` [5264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5264 or target_col == 5264). Every well: [[LGALS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGALS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
