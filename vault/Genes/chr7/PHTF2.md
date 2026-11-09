---
symbol: "PHTF2"
type: "gene"
col: 117
ensembl_id: "ENSG00000006576"
name: "putative homeodomain transcription factor 2"
location: "7q11.23-q21.11"
module: 67
arm: "+"
pooled_cpm: 95.52
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# PHTF2

*putative homeodomain transcription factor 2* — 7q11.23-q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.71× (z +16.4, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.50× (z +12.4, q 3e-33, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.719× (z -10.1, q 3e-21, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPC25]] (+0.65, fdr 9e-06), [[PBK]] (+0.64, fdr 1e-05), [[PCLAF]] (+0.63, fdr 9e-06); moves opposite to [[ARL14EP]] (-0.61, fdr 3e-05), [[ZNF23]] (-0.60, fdr 1e-05), [[CIDECP1]] (-0.60, fdr 1e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PBK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 19 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.71×** | +16.4 | 0e+00 | 43/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.67×** | +15.6 | 0e+00 | 43/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.64×** | +15.0 | 0e+00 | 43/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.57×** | +13.2 | 2e-37 | 37/44 (SK-MEL-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.53×** | +13.0 | 2e-36 | 36/49 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +12.4 | 3e-33 | 38/48 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.42×** | +10.3 | 7e-23 | 30/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +9.5 | 2e-19 | 38/48 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +8.8 | 6e-17 | 37/49 (AsPC-1, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +7.5 | 4e-12 | 23/48 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.18× | +7.1 | 7e-11 | 23/49 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.23×** | +5.9 | 1e-07 | 24/45 (HOP62, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.21×** | +5.9 | 2e-07 | 23/48 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.22×** | +5.8 | 2e-07 | 24/50 (RKO, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.2 | 8e-06 | 22/49 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.35×** | +4.7 | 7e-05 | 24/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.07× | +3.0 | 0.055 | 1/48 (H4) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -10.1 | 3e-21 | 38/48 (A-427, A-172, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.723×** | -9.9 | 8e-21 | 29/48 (A498, A-427, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -9.9 | 9e-21 | 38/48 (A498, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.822×** | -6.0 | 2e-07 | 22/48 (hTERT-HPNE, SNU-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.818×** | -5.9 | 4e-07 | 24/48 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.825×** | -5.9 | 4e-07 | 22/48 (SW480, A-172, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -5.6 | 1e-06 | 16/49 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.888× | -5.2 | 2e-05 | 11/48 (A-172, NCI-H460, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.833× | -5.2 | 2e-05 | 21/47 (C-33 A, NCI-H1573, …) | all doses, flat | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.725×** | -5.1 | 2e-05 | 22/48 (RPMI-7951, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.879× | -3.8 | 0.007 | 10/48 (A498, KATO III, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.793×** | -3.7 | 0.009 | 17/49 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.888× | -3.7 | 0.011 | 14/48 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.922× | -3.6 | 0.014 | 8/48 (SW48, A498, …) | top dose only |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 0.882× | -3.6 | 0.014 | 14/47 (hTERT-HPNE, HCT15, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.036 | 18/48 (NCI-H1792, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.902× | -3.2 | 0.045 | 8/47 (hTERT-HPNE, COLO 205, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 0.905× | -3.1 | 0.058 | 10/48 (C-33 A, NCI-H460, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.905× | -3.1 | 0.058 | 9/48 (LOX-IMVI, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 96.8 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.79× (z +10.5) | — |
| [[J82 (line)]] | alt | 95.7 | 8 (8 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.21× (z +11.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 8 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +14.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 118 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.87× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.3) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.398× (z -11.2) |
| [[A498 (line)]] | wt | 96.5 | 2 (2 ⚠) | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +10.5) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 87.5 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.44× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 74.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 76.5 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.453× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 72.3 | 3 (3 ⚠) | 2 | [[Belinostat (drug)]] 5 µM 2.43× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.477× (z -9.3) |
| [[PANC-1 (line)]] | alt | 129 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-427 (line)]] | wt | 173 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -22.1) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.387× (z -14.3) |
| [[A549 (line)]] | wt | 73.3 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.11× (z +10.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.505× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 51.4 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +10.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 129 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.02× (z +10.5) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 147 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.534× (z -9.3) |
| [[LoVo (line)]] | wt | 68.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SHP-77 (line)]] | alt | 110 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.427× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -8.8) |
| [[SW1417 (line)]] | alt | 91.4 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.03× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.89× (z +9.0) | — |
| [[H4 (line)]] | wt | 122 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.52× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.5) ⚠ cell-cycle shift, explains ~11% of this change |
| [[HS-578T (line)]] | alt | 79.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HT-29 (line)]] | alt | 74.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.2) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[LS 180 (line)]] | wt | 63.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 123 | 1 (1 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 1.82× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.547× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 77.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 65.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[Hs 766T (line)]] | wt | 83.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.347× (z -8.6) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 77.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 76.2 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 81.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.415× (z -10.0) |
| [[SW48 (line)]] | wt | 99.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.325× (z -8.7) |
| [[SW480 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.603× (z -9.0) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 151 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 141 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 93.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPC25]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[PBK]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PCLAF]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[CDK2]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PARPBP]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CALM3]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[MSH2]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[GGH]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[RAD51AP1]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NCAPG2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CMC2]] | +0.59 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MPHOSPH9]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL14EP]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ZNF23]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[CIDECP1]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[MRPL58]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SNHG11]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ABRAXAS2]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ZBED9]] | -0.56 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[TIGD6]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[TNIP2]] | -0.56 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[RPP38]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[PPCS]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SURF6]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | C | PBK activity raises PHTF2's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without PBK | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.1, -38.7); signed map (-44.8, -41.2). **Vector** length 120, 35.0% of its response variance represented; |z| ≥ 3 in 1,359 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.51 to 12); *G2/M checkpoint* (hallmark, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +4.7 | +13.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.0 | +13.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.8 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.9 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -10.7 | -10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.5 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.3 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -8.0 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.8 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | putative homeodomain transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23-q21.11 — chr7:77,798,773-77,957,503 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434D166 |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

UniProt [Q8N3S3](https://www.uniprot.org/uniprotkb/Q8N3S3) carries no function annotation.

**Summary**, from NCBI Gene [57157](https://www.ncbi.nlm.nih.gov/gene/57157):

> Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13411) · Entrez [57157](https://www.ncbi.nlm.nih.gov/gene/57157) · UniProt [Q8N3S3](https://www.uniprot.org/uniprotkb/Q8N3S3) · Ensembl [ENSG00000006576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006576)

## Data

Gene col 117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 117); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 117]; `tensor/DDL_lfc|DDL_z.npy` [117]; `embed/gene_vectors.npy` [117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 117 or target_col == 117). Every well: [[PHTF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHTF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
