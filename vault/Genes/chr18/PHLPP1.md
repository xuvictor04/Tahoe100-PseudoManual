---
symbol: "PHLPP1"
type: "gene"
col: 1329
ensembl_id: "ENSG00000081913"
name: "PH domain and leucine rich repeat protein phosphatase 1"
location: "18q21.33"
module: 145
arm: "+"
pooled_cpm: 113.12
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# PHLPP1

*PH domain and leucine rich repeat protein phosphatase 1* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +7.6, q 1e-11, up in 25 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.376× (z -21.9, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.550× (z -13.9, q 1e-41, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNRF2]] (+0.64, fdr 1e-05), [[SAMD1]] (+0.57, fdr 1e-05), [[GAB1]] (+0.56, fdr 2e-05); moves opposite to [[GTF2H3]] (-0.55, fdr 2e-05), [[ZSCAN20]] (-0.55, fdr 6e-05), [[HUS1]] (-0.53, fdr 3e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +7.6 | 1e-11 | 25/49 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +7.2 | 1e-10 | 30/48 (SHP-77, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +6.7 | 3e-09 | 29/49 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +6.3 | 4e-08 | 27/48 (LS 180, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.9 | 5e-07 | 28/48 (LoVo, SW48, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.5 | 4e-06 | 24/48 (NCI-H2030, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.9 | 6e-05 | 25/49 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +4.9 | 6e-05 | 25/48 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 18/48 (H4, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.7 | 0.014 | 18/48 (A498, hTERT-HPNE, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.18× | +3.6 | 0.014 | 14/48 (COLO 205, HEC-1-A, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.016 | 14/48 (RKO, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.029 | 11/48 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +3.0 | 0.10 | 19/48 (PANC-1, NCI-H2030, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.376×** | -21.9 | 0e+00 | 41/44 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.391×** | -20.8 | 0e+00 | 42/49 (C-33 A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.550×** | -13.9 | 1e-41 | 39/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.570×** | -12.1 | 2e-31 | 29/45 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.682×** | -8.9 | 6e-17 | 37/47 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.719×** | -7.7 | 2e-12 | 31/48 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.810×** | -6.9 | 3e-10 | 24/48 (A-172, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.566×** | -6.9 | 3e-10 | 35/46 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.594×** | -6.3 | 1e-08 | 38/48 (C32, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -5.7 | 7e-07 | 26/48 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.785×** | -5.6 | 8e-07 | 27/48 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.629×** | -5.6 | 8e-07 | 31/48 (LoVo, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.635×** | -5.5 | 1e-06 | 28/48 (KATO III, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.661×** | -5.0 | 2e-05 | 25/48 (KATO III, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.803×** | -4.8 | 5e-05 | 25/48 (C32, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.820×** | -4.6 | 1e-04 | 24/48 (C32, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.823×** | -4.4 | 4e-04 | 22/48 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.837× | -4.1 | 0.001 | 17/48 (BT-474, CFPAC-1, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.859× | -3.3 | 0.019 | 16/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 306 | 3 | 14 (7 ⚠) | [[PH-797804 (drug)]] 5 µM 4.77× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.200× (z -19.7) |
| [[KATO III (line)]] | alt | 197 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0586× (z -32.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.351× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 136 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.57× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.508× (z -8.9) |
| [[A498 (line)]] | wt | 59.6 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.368× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 169 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.388× (z -11.4) |
| [[LS 180 (line)]] | wt | 281 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -22.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 162 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -15.5) |
| [[LoVo (line)]] | wt | 303 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.282× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 67.7 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 230 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.430× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 29.8 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +10.1) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.22× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.277× (z -14.5) |
| [[PANC-1 (line)]] | alt | 42.7 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.30× (z +10.5) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 77.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.301× (z -13.3) |
| [[SW1417 (line)]] | alt | 130 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.268× (z -16.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 68.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.502× (z -10.2) |
| [[A-427 (line)]] | wt | 75.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.353× (z -12.6) |
| [[C-33 A (line)]] | alt | 453 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -25.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 90.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.473× (z -8.5) |
| [[HS-578T (line)]] | alt | 81.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 79.5 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.486× (z -8.5) |
| [[J82 (line)]] | alt | 157 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -20.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.555× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 88.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -14.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.331× (z -11.8) |
| [[SHP-77 (line)]] | alt | 196 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.493× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 189 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.218× (z -17.2) |
| [[SNU-1 (line)]] | wt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -14.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 55.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.356× (z -13.7) |
| [[A549 (line)]] | wt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -17.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 37.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -8.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 45.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 70.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.240× (z -10.6) |
| [[CHP-212 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0325× (z -18.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 43.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 42.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 77.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +15.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0793× (z -13.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -23.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -12.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRF2]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[SAMD1]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[GAB1]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 | same gene group; pathway: Intracellular signaling by second messengers |
| [[POU2F1]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[IPMK]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[MAGI1]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[TMTC2]] | +0.53 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[USP6NL]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[MAGI3]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[IMPA2]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FOXN3]] | +0.51 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[GPC4]] | +0.51 | +0.54 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ZSCAN20]] | -0.55 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[HUS1]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[TOP3B]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[TRAK2]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ZNF229]] | -0.51 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[ZNF621]] | -0.49 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[DDX1]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ZSCAN22]] | -0.48 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[HARS1]] | -0.48 | -0.46 / -0.43 | both halves | 4e-05 |  |
| [[BMS1]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[IKBKG]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.2, -52.0); signed map (-19.9, 15.9). **Vector** length 113, 31.8% of its response variance represented; |z| ≥ 3 in 1,406 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +7.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.6 | -13.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.7 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -7.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.9 | -5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -5.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.5 | -6.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | PH domain and leucine rich repeat protein phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:62,715,541-62,980,433 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0606, SCOP, PPM3A; previously PLEKHE1, PHLPP |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Protein phosphatases, Mg2+/Mn2+ dependent |
| Reactome | 3 pathways, smallest: Negative regulation of the PI3K/AKT network; PIP3 activates AKT signaling; Intracellular signaling by second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [O60346](https://www.uniprot.org/uniprotkb/O60346) (PH domain leucine-rich repeat-containing protein phosphatase 1):

> Protein phosphatase involved in regulation of Akt and PKC signaling. Mediates dephosphorylation in the C-terminal domain hydrophobic motif of members of the AGC Ser/Thr protein kinase family; specifically acts on 'Ser-473' of AKT2 and AKT3, 'Ser-660' of PRKCB and 'Ser-657' of PRKCA. Isoform 2 seems to have a major role in regulating Akt signaling in hippocampal neurons (By similarity). Akt regulates the balance between cell survival and apoptosis through a cascade that primarily alters the …

**Summary**, from NCBI Gene [23239](https://www.ncbi.nlm.nih.gov/gene/23239):

> This gene encodes a member of the serine/threonine phosphatase family. The encoded protein promotes apoptosis by dephosphorylating and inactivating the serine/threonine kinase Akt, and functions as a tumor suppressor in multiple types of cancer. Increased expression of this gene may also play a role in obesity and type 2 diabetes by interfering with Akt-mediated insulin signaling. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:20610](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20610) · Entrez [23239](https://www.ncbi.nlm.nih.gov/gene/23239) · UniProt [O60346](https://www.uniprot.org/uniprotkb/O60346) · Ensembl [ENSG00000081913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081913)

## Data

Gene col 1329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1329); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1329]; `tensor/DDL_lfc|DDL_z.npy` [1329]; `embed/gene_vectors.npy` [1329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1329 or target_col == 1329). Every well: [[PHLPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHLPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
