---
symbol: "DUSP16"
type: "gene"
col: 3211
ensembl_id: "ENSG00000111266"
name: "dual specificity phosphatase 16"
location: "12p13.2"
module: 68
arm: "+"
pooled_cpm: 94.65
n_lines_expressing: 48
n_dd_up: 35
n_dd_down: 17
n_dd_up_clean: 33
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# DUSP16

*dual specificity phosphatase 16* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +18.1, q 0e+00, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.262× (z -29.6, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMO]] (+0.70, fdr 1e-05), [[KRTAP5-AS1]] (+0.68, fdr 7e-06), [[RIPK2-DT]] (+0.65, fdr 2e-05); moves opposite to [[SKP2]] (-0.61, fdr 1e-05), [[WASF3]] (-0.60, fdr 2e-05), [[SMYD2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HDAC9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +18.1 | 0e+00 | 32/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +12.6 | 6e-34 | 39/47 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.78×** | +12.2 | 5e-32 | 42/45 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.68×** | +11.5 | 2e-28 | 40/45 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +9.7 | 4e-20 | 32/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.52×** | +9.1 | 9e-18 | 35/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.9 | 6e-17 | 29/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.44×** | +8.1 | 5e-14 | 33/46 (PANC-1, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.0 | 8e-14 | 31/46 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.43×** | +7.8 | 3e-13 | 33/46 (Panc 03.27, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +6.9 | 2e-10 | 35/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +6.9 | 3e-10 | 26/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +6.9 | 3e-10 | 26/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.33×** | +6.1 | 4e-08 | 26/45 (Panc 03.27, C32, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.68×** | +6.0 | 7e-08 | 34/46 (LoVo, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.65×** | +5.8 | 2e-07 | 31/48 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 2e-07 | 23/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.262×** | -29.6 | 0e+00 | 46/46 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.289×** | -27.4 | 0e+00 | 46/46 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.312×** | -25.8 | 0e+00 | 46/46 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.566×** | -11.7 | 3e-29 | 34/43 (CHP-212, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.608×** | -11.0 | 4e-26 | 35/47 (COLO 205, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.602×** | -10.8 | 4e-25 | 28/42 (SNU-423, LoVo, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.693×** | -8.1 | 4e-14 | 32/46 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -7.1 | 7e-11 | 29/46 (BT-474, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.759×** | -6.1 | 6e-08 | 31/46 (CHP-212, SW 900, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.794×** | -4.9 | 5e-05 | 25/48 (A-427, SNU-423, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.668×** | -4.7 | 2e-04 | 23/45 (NCI-H1792, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.816×** | -4.5 | 3e-04 | 23/46 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.687×** | -4.3 | 6e-04 | 16/46 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **0.816×** | -4.3 | 8e-04 | 21/46 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.001 | 19/46 (HepG2/C3A, SNU-423, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.713×** | -3.9 | 0.003 | 16/47 (HepG2/C3A, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.835× | -3.8 | 0.004 | 16/46 (A549, NCI-H2030, …) | top dose only |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 0.864× | -3.2 | 0.032 | 12/46 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.905× | -3.2 | 0.041 | 12/46 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.908× | -3.0 | 0.060 | 12/46 (CHP-212, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 153 | 3 | 19 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.167× (z -20.6) |
| [[LoVo (line)]] | wt | 185 | 9 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.3× (z +17.7) | [[Panobinostat (drug)]] 5 µM 0.181× (z -21.3) |
| [[COLO 205 (line)]] | alt | 260 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0371× (z -28.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0908× (z -20.5) |
| [[NCI-H460 (line)]] | wt | 62.4 | 10 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +23.3) | [[Panobinostat (drug)]] 5 µM 0.271× (z -15.4) |
| [[BT-474 (line)]] | alt | 387 | 2 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.1× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -19.4) |
| [[MIA PaCa-2 (line)]] | alt | 74.1 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.264× (z -13.4) |
| [[A549 (line)]] | wt | 323 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0664× (z -20.8) |
| [[HepG2_C3A (line)]] | wt | 254 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -20.5) |
| [[HT-29 (line)]] | alt | 212 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -21.0) |
| [[PANC-1 (line)]] | alt | 44.3 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +19.5) | [[Panobinostat (drug)]] 5 µM 0.392× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 191 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0623× (z -25.2) |
| [[A-427 (line)]] | wt | 115 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.238× (z -16.8) |
| [[HS-578T (line)]] | alt | 34.9 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 127 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +18.7) | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -16.5) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -16.3) |
| [[A-172 (line)]] | wt | 41.1 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.251× (z -11.8) |
| [[A498 (line)]] | wt | 48.4 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +29.0) | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -10.2) |
| [[CHP-212 (line)]] | wt | 142 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0900× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.116× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 50.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -13.7) |
| [[LS 180 (line)]] | wt | 145 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 89.2 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 6.16× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.303× (z -12.7) |
| [[SW 900 (line)]] | alt | 174 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -14.1) |
| [[SW480 (line)]] | alt | 53.6 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.325× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 40.2 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -10.0) |
| [[C-33 A (line)]] | alt | 131 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -19.0) |
| [[C32 (line)]] | wt | 47.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 82.4 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -12.2) |
| [[HOP62 (line)]] | alt | 77.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -12.7) |
| [[KATO III (line)]] | alt | 104 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 76.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.169× (z -18.7) |
| [[RPMI-7951 (line)]] | alt | 53.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.252× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 54.8 | 3 | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.69× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -9.7) |
| [[J82 (line)]] | alt | 44.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.315× (z -10.0) |
| [[RKO (line)]] | wt | 83.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -11.6) |
| [[SNU-1 (line)]] | wt | 90.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.256× (z -9.9) |
| [[SW1417 (line)]] | alt | 52.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 39.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -10.6) |
| [[HCT15 (line)]] | alt | 85.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 56.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -11.1) |
| [[AN3 CA (line)]] | alt | 91.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[hTERT-HPNE (line)]] | wt | 42.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 60.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -8.8) |
| [[Hs 766T (line)]] | wt | 21.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMO]] | +0.70 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[KRTAP5-AS1]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.65 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MVP-DT]] | +0.65 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[KANSL1L]] | +0.65 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[PATL2]] | +0.64 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TMEM217]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | +0.64 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CTSS]] | +0.63 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[TBC1D22B]] | +0.63 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TRIM69]] | +0.63 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[ZNF764]] | +0.63 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKP2]] | -0.61 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[WASF3]] | -0.60 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SMYD2]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.60 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ETV5]] | -0.59 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[HPCAL1]] | -0.59 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RNF216P1]] | -0.57 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.56 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[IMPDH1]] | -0.56 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[NBPF3]] | -0.56 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[PAPSS1]] | -0.55 | -0.37 / -0.46 | both halves | 7e-05 | pathway: Oncogenic MAPK signaling |
| [[NUDT21]] | -0.55 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC9]] | B | HDAC9 activity lowers DUSP16's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 2.36× higher at baseline in the lines without HDAC9 | 0.068 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |
| [[TTC6]] | B | TTC6 activity raises DUSP16's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without TTC6 | 0.085 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[RNF103-CHMP3]] | B | RNF103-CHMP3 activity raises DUSP16's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 2.62× lower at baseline in the lines without RNF103-CHMP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[CXCL2]] | B | CXCL2 activity raises DUSP16's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without CXCL2 | 0.090 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[SERPINB7]] | B | SERPINB7 activity raises DUSP16's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.35× lower at baseline in the lines without SERPINB7 | 0.098 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[DUSP8]] | C | DUSP8 activity raises DUSP16's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 2.81× lower at baseline in the lines without DUSP8 | 0.026 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (19.5, 9.8); signed map (42.5, -3.7). **Vector** length 130, 41.4% of its response variance represented; |z| ≥ 3 in 1,721 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.6 | +18.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.8 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +7.3 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.3 | +0.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +7.1 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.1 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +6.1 | +4.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.6 | -25.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.3 | -29.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -27.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -4.6 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -1.7 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:12,473,282-12,562,863 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MKP-7, KIAA1700, MKP7 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Reactome | 11 pathways, smallest: Signaling by MAPK mutants; Response of Mtb to phagocytosis; Infection with Mycobacterium tuberculosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY84](https://www.uniprot.org/uniprotkb/Q9BY84) (Dual specificity protein phosphatase 16):

> Dual specificity protein phosphatase involved in the inactivation of MAP kinases. Dephosphorylates MAPK10 bound to ARRB2.

**Summary**, from NCBI Gene [80824](https://www.ncbi.nlm.nih.gov/gene/80824):

> This gene encodes a mitogen-activated protein kinase phosphatase that is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. The encoded protein specifically regulates the c-Jun amino-terminal kinase (JNK) and extracellular signal-regulated kinase (ERK) pathways.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:17909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17909) · Entrez [80824](https://www.ncbi.nlm.nih.gov/gene/80824) · UniProt [Q9BY84](https://www.uniprot.org/uniprotkb/Q9BY84) · Ensembl [ENSG00000111266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111266)

## Data

Gene col 3211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3211); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3211]; `tensor/DDL_lfc|DDL_z.npy` [3211]; `embed/gene_vectors.npy` [3211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3211 or target_col == 3211). Every well: [[DUSP16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
