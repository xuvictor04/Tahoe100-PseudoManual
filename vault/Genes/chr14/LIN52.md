---
symbol: "LIN52"
type: "gene"
col: 13000
ensembl_id: "ENSG00000205659"
name: "lin-52 DREAM MuvB core complex component"
location: "14q24.3"
module: 71
arm: "+"
pooled_cpm: 54.23
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# LIN52

*lin-52 DREAM MuvB core complex component* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.85× (z +23.8, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +17.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.682× (z -12.3, q 4e-32, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAUS8]] (+0.68, fdr 7e-06), [[SENP5]] (+0.66, fdr 2e-05), [[HIRA]] (+0.66, fdr 1e-05); moves opposite to [[RYBP]] (-0.59, fdr 7e-06), [[TP53BP2]] (-0.55, fdr 1e-05), [[BHLHE40]] (-0.55, fdr 5e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.85×** | +23.8 | 0e+00 | 47/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.45×** | +20.3 | 0e+00 | 46/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.44×** | +20.2 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +17.7 | 0e+00 | 44/48 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +14.3 | 1e-44 | 37/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +13.8 | 3e-41 | 42/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +12.5 | 7e-34 | 43/48 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +12.3 | 5e-33 | 36/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +12.3 | 6e-33 | 35/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +11.0 | 2e-26 | 31/47 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +10.9 | 8e-26 | 32/48 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.63×** | +10.7 | 5e-25 | 31/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +9.1 | 3e-18 | 34/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +8.9 | 3e-17 | 33/48 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +8.1 | 2e-14 | 33/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +7.1 | 5e-11 | 29/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.9 | 1e-07 | 23/48 (HOP62, SW1417, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +5.2 | 5e-06 | 22/49 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 3e-05 | 18/48 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.8 | 3e-05 | 21/48 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -12.3 | 4e-32 | 40/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.667×** | -9.2 | 5e-18 | 34/49 (A-427, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -9.2 | 5e-18 | 30/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.679×** | -8.8 | 2e-16 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.682×** | -8.7 | 3e-16 | 36/48 (CFPAC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -8.3 | 1e-14 | 27/42 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.762×** | -6.0 | 2e-07 | 26/48 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -5.9 | 2e-07 | 24/44 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -4.4 | 6e-04 | 18/48 (A498, A-427, …) | all doses, flat | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.828×** | -4.3 | 9e-04 | 18/48 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.839× | -4.0 | 0.003 | 19/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.842× | -3.9 | 0.004 | 14/48 (MIA PaCa-2, A-427, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.865× | -3.3 | 0.036 | 12/48 (CHP-212, SW48, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.757×** | -3.3 | 0.036 | 13/37 (HepG2/C3A, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Bexarotene (drug)]] 5 µM |  | 0.869× | -3.2 | 0.049 | 8/48 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.873× | -3.1 | 0.064 | 8/48 (RKO, NCI-H661, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.865× | -3.1 | 0.064 | 18/47 (A549, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 66.5 | 7 (5 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.88× (z +15.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.1) | [[Tucidinostat (drug)]] 5 µM 0.568× (z -11.4) |
| [[PANC-1 (line)]] | alt | 51.8 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.4 | 3 (3 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 3.74× (z +12.5) ⚠ cell-cycle shift, explains ~27% of this change | [[Harringtonine (drug)]] 0.5 µM 0.359× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 107 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 48.6 | 5 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +16.1) | [[Tucidinostat (drug)]] 0.5 µM 0.428× (z -9.5) |
| [[LS 180 (line)]] | wt | 36.6 | 3 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.20× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.3) | [[Tucidinostat (drug)]] 5 µM 0.432× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 55.1 | 5 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.11× (z +11.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 97.8 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.365× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 50.7 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -18.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 63.4 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.2 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.9) | — |
| [[A-427 (line)]] | wt | 97.6 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0623× (z -29.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.360× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 38.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +15.3) | — |
| [[COLO 205 (line)]] | alt | 48.9 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 42.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +8.5) | — |
| [[KATO III (line)]] | alt | 36.0 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 46.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.26× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 49.5 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.7) | [[Harringtonine (drug)]] 0.5 µM 0.314× (z -10.2) |
| [[A498 (line)]] | wt | 50.1 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.323× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 37.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[BT-474 (line)]] | alt | 57.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 50.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.80× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 32.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.294× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 44.2 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.43× (z +11.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Tucidinostat (drug)]] 5 µM 0.539× (z -8.5) |
| [[RKO (line)]] | wt | 65.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 41.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 44.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -13.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 75.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 86.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.0853× (z -21.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 49.6 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | [[Tucidinostat (drug)]] 0.5 µM 0.405× (z -9.0) |
| [[SHP-77 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0900× (z -27.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 56.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.415× (z -8.8) |
| [[SW48 (line)]] | wt | 73.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.31× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.200× (z -11.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -13.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -13.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 32.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.111× (z -8.8) |
| [[HCT15 (line)]] | alt | 54.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HepG2_C3A (line)]] | wt | 56.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS8]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 | pathway: G2/M Transition |
| [[SENP5]] | +0.66 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[HIRA]] | +0.66 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.63 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[MEF2B]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[NFATC2IP]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[DTYMK]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NUP88]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[DHRS7B]] | +0.61 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[CMC2]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[FBXO36]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PHF5A]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | -0.59 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[TP53BP2]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[BHLHE40]] | -0.55 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[UROS]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[AMOT]] | -0.54 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ZBED9]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[COMMD8]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PCLO]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[CDC73]] | -0.53 | -0.37 / -0.57 | both halves | 7e-05 |  |
| [[C12orf29]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[DUSP19]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TAB2]] | -0.51 | -0.31 / -0.59 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LIN52's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPTXR]] | B | NPTXR activity raises LIN52's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without NPTXR | 0.067 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.4, -1.1); signed map (-47.1, -0.2). **Vector** length 119, 37.2% of its response variance represented; |z| ≥ 3 in 1,421 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.7 | +12.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.7 | +12.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +13.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.7 | +14.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +9.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.6 | +4.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.6 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -14.0 | -12.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -11.3 | -8.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.1 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.4 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.3 | -4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | lin-52 DREAM MuvB core complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,084,956-74,201,493 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf46 |
| Gene groups (HGNC) | MuvB complex subunits |
| Reactome | 14 pathways, smallest: Polo-like kinase mediated events; Transcription of E2F targets under negative control by p107 (RBL1) and p130 (RBL2) in complex with HDAC1; Transcription of E2F targets under negative control by DREAM complex |
| Matched by | ensembl_id |

UniProt [Q52LA3](https://www.uniprot.org/uniprotkb/Q52LA3) carries no function annotation.

**Summary**, from NCBI Gene [91750](https://www.ncbi.nlm.nih.gov/gene/91750):

> Predicted to be involved in negative regulation of DNA-templated transcription and positive regulation of transcription by RNA polymerase II. Predicted to be located in nucleoplasm. Predicted to be part of DRM complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19856) · Entrez [91750](https://www.ncbi.nlm.nih.gov/gene/91750) · UniProt [Q52LA3](https://www.uniprot.org/uniprotkb/Q52LA3) · Ensembl [ENSG00000205659](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205659)

## Data

Gene col 13000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13000); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13000]; `tensor/DDL_lfc|DDL_z.npy` [13000]; `embed/gene_vectors.npy` [13000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13000 or target_col == 13000). Every well: [[LIN52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIN52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
