---
symbol: "TNS3"
type: "gene"
col: 5834
ensembl_id: "ENSG00000136205"
name: "tensin 3"
location: "7p12.3"
module: 34
arm: "+"
pooled_cpm: 237.45
n_lines_expressing: 42
n_dd_up: 16
n_dd_down: 44
n_dd_up_clean: 15
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 11
direction_downstream: 20
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TNS3

*tensin 3* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.71× (z +6.6, q 3e-08, up in 31 of 42 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 1.45× (z +6.4, q 5e-08, up in 34 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (20 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.187× (z -20.5, q 0e+00, down in 40 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH3B1]] (+0.60, fdr 1e-05), [[ZNF608]] (+0.60, fdr 1e-05), [[MYOF]] (+0.57, fdr 1e-05); moves opposite to [[PLEKHG5]] (-0.62, fdr 1e-05), [[S100A16]] (-0.61, fdr 1e-05), [[PLEK2]] (-0.61, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MYOF]] → it (grade B ⚠); 20 go from it, the strongest it → [[PLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.71×** | +6.6 | 3e-08 | 31/42 (AsPC-1, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.45×** | +6.4 | 5e-08 | 34/40 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +6.3 | 5e-08 | 33/39 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.65×** | +5.9 | 4e-07 | 27/40 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.59×** | +5.8 | 8e-07 | 28/41 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 8e-07 | 28/40 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 1e-05 | 27/40 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.54×** | +5.0 | 3e-05 | 30/40 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.62×** | +4.9 | 7e-05 | 30/39 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 8e-05 | 26/41 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.10×** | +4.8 | 9e-05 | 30/42 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.44×** | +4.1 | 0.002 | 29/40 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.026 | 22/41 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.027 | 26/40 (MIA PaCa-2, AsPC-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.4 | 0.027 | 4/42 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.044 | 23/40 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 5 µM |  | **1.63×** | +3.2 | 0.052 | 22/40 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.187×** | -20.5 | 0e+00 | 40/40 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.320×** | -19.7 | 0e+00 | 41/41 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.322×** | -19.6 | 0e+00 | 37/40 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.208×** | -19.2 | 0e+00 | 40/40 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.240×** | -17.5 | 0e+00 | 40/40 (Hs 766T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.401×** | -11.2 | 4e-27 | 35/40 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.422×** | -10.2 | 2e-22 | 35/40 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.444×** | -9.9 | 2e-21 | 39/40 (RPMI-7951, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.446×** | -9.9 | 3e-21 | 36/40 (LoVo, SW48, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.459×** | -9.2 | 3e-18 | 35/39 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.455×** | -9.1 | 5e-18 | 36/40 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.479×** | -9.0 | 1e-17 | 38/40 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.502×** | -8.1 | 3e-14 | 34/40 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.526×** | -7.8 | 2e-13 | 32/40 (PANC-1, H4, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.529×** | -7.8 | 3e-13 | 30/40 (H4, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.548×** | -7.3 | 7e-12 | 36/40 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.569×** | -6.9 | 2e-10 | 34/40 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.601×** | -6.2 | 1e-08 | 33/41 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -5.6 | 6e-07 | 29/41 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.440×** | -5.3 | 3e-06 | 34/40 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.749×** | -5.0 | 1e-05 | 27/41 (MIA PaCa-2, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.71 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 448 | 2 (1 ⚠) | 18 (9 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +20.3) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.05 µM 1.87× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -31.2) |
| [[NCI-H460 (line)]] | wt | 107 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.1) |
| [[SNU-423 (line)]] | alt | 780 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0587× (z -34.9) |
| [[PANC-1 (line)]] | alt | 472 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -34.2) |
| [[H4 (line)]] | wt | 574 | 0 | 15 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.104× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 98.4 | 11 (1 ⚠) | 3 (1 ⚠) | [[Trametinib (drug)]] 0.05 µM 3.28× (z +12.2) | [[Harringtonine (drug)]] 5 µM 0.249× (z -10.0) |
| [[SW 900 (line)]] | alt | 345 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -18.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.128× (z -18.0) |
| [[HepG2_C3A (line)]] | wt | 420 | 0 | 12 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -22.1) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -19.7) |
| [[LoVo (line)]] | wt | 188 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -19.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.282× (z -18.7) |
| [[RPMI-7951 (line)]] | alt | 336 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -21.2) |
| [[COLO 205 (line)]] | alt | 132 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -25.8) |
| [[HEC-1-A (line)]] | alt | 184 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -20.0) |
| [[NCI-H1573 (line)]] | alt | 198 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0812× (z -30.0) |
| [[A498 (line)]] | wt | 422 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -17.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.8) |
| [[HOP62 (line)]] | alt | 202 | 1 (1 ⚠) | 8 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +13.8) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -12.7) |
| [[SW48 (line)]] | wt | 395 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -18.6) |
| [[C32 (line)]] | wt | 153 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -21.8) |
| [[NCI-H1792 (line)]] | alt | 140 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -30.5) |
| [[SW1417 (line)]] | alt | 155 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -14.8) |
| [[SW480 (line)]] | alt | 613 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -14.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.171× (z -13.5) |
| [[A-172 (line)]] | wt | 180 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.100× (z -16.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.135× (z -14.6) |
| [[BT-474 (line)]] | alt | 175 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -14.0) |
| [[Hs 766T (line)]] | wt | 317 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0931× (z -22.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0984× (z -22.1) |
| [[J82 (line)]] | alt | 240 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -16.1) |
| [[NCI-H2030 (line)]] | alt | 148 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 186 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -15.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.173× (z -15.4) |
| [[HS-578T (line)]] | alt | 165 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -14.2) |
| [[HT-29 (line)]] | alt | 190 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -15.6) |
| [[LS 180 (line)]] | wt | 120 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -16.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.234× (z -14.0) |
| [[A549 (line)]] | wt | 413 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0719× (z -20.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0927× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 146 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -14.4) |
| [[KATO III (line)]] | alt | 211 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -16.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.180× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 76.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -14.0) |
| [[AN3 CA (line)]] | alt | 200 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -11.8) |
| [[SW 1088 (line)]] | alt | 523 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -10.6) |
| [[A-427 (line)]] | wt | 22.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 46.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 53.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3B1]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MYOF]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MTUS1]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[BICC1]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SORBS2]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[RARRES1]] | +0.55 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[TGFB2]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SPTLC3]] | +0.52 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[LUM]] | +0.52 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[DPYD]] | +0.51 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[SEC16B]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHG5]] | -0.62 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[S100A16]] | -0.61 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PLEK2]] | -0.61 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[CORO2B]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CSNK1E]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PLAUR]] | -0.55 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[FXYD5]] | -0.54 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TM4SF19]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[KCTD5]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PAQR5]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[MMP1]] | -0.52 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[SHANK1]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOF]] | B | MYOF activity raises TNS3's level | lines that do not express MYOF (6) vs lines expressing it (44) | 3.32× lower at baseline in the lines without MYOF | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[CDCP1]] | B | CDCP1 activity raises TNS3's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without CDCP1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[MAP2K1]] | B | MAP2K1 activity lowers TNS3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GRB10]] | B | GRB10 activity raises TNS3's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 2.80× lower at baseline in the lines without GRB10 | 0.064 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[BICC1]] | B | BICC1 activity raises TNS3's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without BICC1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[ARID5B]] | B | ARID5B activity raises TNS3's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.51× lower at baseline in the lines without ARID5B | 0.078 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[PDLIM1]] | B | PDLIM1 activity raises TNS3's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.70× lower at baseline in the lines without PDLIM1 | 0.084 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[MAP2K2]] | B | MAP2K2 activity lowers TNS3's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[GBX1]] | B | GBX1 activity raises TNS3's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without GBX1 | 0.097 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[ALDH3B1]] | C | ALDH3B1 activity raises TNS3's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 4.76× lower at baseline in the lines without ALDH3B1 | 0.004 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent; co-absent with the target |
| [[LINC00511]] | C | LINC00511 activity raises TNS3's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 3.31× lower at baseline in the lines without LINC00511 | 0.019 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 17, C 3. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLD1]] | B | TNS3 activity raises PLD1's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 3.15× lower at baseline in the lines without TNS3 | 0.002 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[SHANK1]] | B | TNS3 activity lowers SHANK1's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 4.37× higher at baseline in the lines without TNS3 | 0.009 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[MYOF]] | B | TNS3 activity raises MYOF's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.79× lower at baseline in the lines without TNS3 | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[GRB10]] | B | TNS3 activity raises GRB10's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 4.23× lower at baseline in the lines without TNS3 | 0.023 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[CFB]] | B | TNS3 activity raises CFB's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 4.85× lower at baseline in the lines without TNS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[PLAUR]] | B | TNS3 activity raises PLAUR's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.81× lower at baseline in the lines without TNS3 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | TNS3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express TNS3 (8) vs lines expressing it (40) | the lines without TNS3: 0.87× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[TGFB2]] | B | TNS3 activity raises TGFB2's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.75× lower at baseline in the lines without TNS3 | 0.046 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[RBPMS]] | B | TNS3 activity raises RBPMS's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 3.90× lower at baseline in the lines without TNS3 | 0.047 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[PDLIM1]] | B | TNS3 activity raises PDLIM1's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 3.45× lower at baseline in the lines without TNS3 | 0.053 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[SEC16B]] | B | TNS3 activity raises SEC16B's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.51× lower at baseline in the lines without TNS3 | 0.064 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[TMEM154]] | B | TNS3 activity raises TMEM154's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without TNS3 | 0.069 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction -0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, 3.0); signed map (50.2, 13.7). **Vector** length 98.6, 37.7% of its response variance represented; |z| ≥ 3 in 1,957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +5.7 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.6 | +5.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.1 | +5.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.1 | +6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.7 | +5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +6.3 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -9.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -9.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.4 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -9.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | tensin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:47,275,154-47,582,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TEM6, H_NH0549I23.2, FLJ13732; previously TENS1 |
| Gene groups (HGNC) | SH2 domain containing; C2 tensin-type domain containing |
| Reactome | 4 pathways, smallest: MET interacts with TNS proteins; MET promotes cell motility; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68CZ2](https://www.uniprot.org/uniprotkb/Q68CZ2) (Tensin-3):

> May act as a protein phosphatase and/or a lipid phosphatase (Probable). Involved in the dissociation of the integrin-tensin-actin complex. EGF activates TNS4 and down-regulates TNS3 which results in capping the tail of ITGB1. Increases DOCK5 guanine nucleotide exchange activity towards Rac and plays a role in osteoclast podosome organization (By similarity). Enhances RHOA activation in the presence of DLC1. Required for growth factor-induced epithelial cell migration; growth factor stimulation …

**Summary**, from NCBI Gene [64759](https://www.ncbi.nlm.nih.gov/gene/64759):

> Predicted to enable guanyl-nucleotide exchange factor adaptor activity. Predicted to be involved in positive regulation of Rac protein signal transduction. Predicted to act upstream of or within several processes, including bone resorption; negative regulation of Rho protein signal transduction; and podosome assembly. Located in focal adhesion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21616) · Entrez [64759](https://www.ncbi.nlm.nih.gov/gene/64759) · UniProt [Q68CZ2](https://www.uniprot.org/uniprotkb/Q68CZ2) · Ensembl [ENSG00000136205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136205)

## Data

Gene col 5834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5834); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5834]; `tensor/DDL_lfc|DDL_z.npy` [5834]; `embed/gene_vectors.npy` [5834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5834 or target_col == 5834). Every well: [[TNS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
