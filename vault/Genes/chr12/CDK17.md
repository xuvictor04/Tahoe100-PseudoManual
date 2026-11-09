---
symbol: "CDK17"
type: "gene"
col: 678
ensembl_id: "ENSG00000059758"
name: "cyclin dependent kinase 17"
location: "12q23.1"
module: 147
arm: "+"
pooled_cpm: 175.2
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# CDK17

*cyclin dependent kinase 17* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +14.0, q 5e-42, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.344× (z -16.9, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.582× (z -8.9, q 8e-17, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP4K4]] (+0.60, fdr 1e-05), [[SMURF2]] (+0.59, fdr 7e-06), [[ROBO4]] (+0.57, fdr 3e-05); moves opposite to [[DHDDS]] (-0.47, fdr 2e-04), [[TARS3]] (-0.46, fdr 1e-04), [[TMPRSS5]] (-0.46, fdr 3e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FRMD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +14.0 | 5e-42 | 37/48 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.85×** | +11.6 | 9e-29 | 46/49 (SW480, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +11.0 | 1e-25 | 45/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +10.1 | 9e-22 | 42/48 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +8.7 | 3e-16 | 42/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +8.0 | 1e-13 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +7.8 | 3e-13 | 44/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 1e-08 | 37/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 0.001 | 24/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.012 | 25/47 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.015 | 20/48 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.047 | 9/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.42× | +3.0 | 0.10 | 19/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.21× | +3.0 | 0.10 | 20/47 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.344×** | -16.9 | 0e+00 | 44/44 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.380×** | -16.0 | 0e+00 | 44/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.582×** | -8.9 | 8e-17 | 40/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.593×** | -8.6 | 1e-15 | 42/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -5.7 | 1e-06 | 34/47 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.712×** | -5.6 | 2e-06 | 33/48 (A-427, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.766×** | -4.4 | 9e-04 | 29/48 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.007 | 24/49 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.807×** | -3.9 | 0.007 | 24/48 (NCI-H23, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.700×** | -3.8 | 0.007 | 26/47 (SK-MEL-2, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.713×** | -3.6 | 0.015 | 27/48 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.795×** | -3.5 | 0.022 | 24/45 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.863× | -3.4 | 0.026 | 14/48 (SW480, SW48, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.826×** | -3.1 | 0.067 | 23/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.832×** | -3.0 | 0.090 | 20/48 (NCI-H23, J82, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.833×** | -3.0 | 0.090 | 21/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.852× | -3.0 | 0.094 | 16/48 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 379 | 0 | 15 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.518× (z -17.5) ⚠ position not correctable · without an alert: [[Auranofin (drug)]] 5 µM 0.246× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 223 | 4 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.73× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.397× (z -10.4) |
| [[SW480 (line)]] | alt | 143 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.479× (z -10.0) |
| [[A549 (line)]] | wt | 183 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.410× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 250 | 2 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.396× (z -10.4) |
| [[HOP62 (line)]] | alt | 181 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.457× (z -8.9) |
| [[A-427 (line)]] | wt | 348 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.91× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.272× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 124 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.462× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 315 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.370× (z -11.4) |
| [[PANC-1 (line)]] | alt | 153 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 127 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 237 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -19.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 117 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -14.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 70.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.05× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 138 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 106 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[RKO (line)]] | wt | 317 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 155 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 218 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.23× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.377× (z -9.1) |
| [[HT-29 (line)]] | alt | 66.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -10.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 218 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.363× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 390 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -15.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[RPMI-7951 (line)]] | alt | 137 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -10.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 134 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.59× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -15.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 115 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +10.7) | — |
| [[A-172 (line)]] | wt | 145 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -11.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 117 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 94.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.22× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.336× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 240 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 161 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 220 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 173 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -11.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 87.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.48× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -15.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 144 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +13.6) | — |
| [[C-33 A (line)]] | alt | 92.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -18.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 83.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[H4 (line)]] | wt | 137 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 201 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP4K4]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[SMURF2]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ROBO4]] | +0.57 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[PRDM8]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LTBP2]] | +0.56 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[SPRED1]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[B4GALT6]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[LINC02454]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NUAK2]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[FJX1]] | +0.53 | +0.28 / +0.55 | both halves | 3e-04 |  |
| [[TOMM34]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ARHGAP31]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHDDS]] | -0.47 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[TARS3]] | -0.46 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[TMPRSS5]] | -0.46 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TOM1]] | -0.45 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[SLC17A5]] | -0.45 | -0.24 / -0.50 | both halves | 5e-04 |  |
| [[LONP1]] | -0.45 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[OSBPL2]] | -0.45 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[HDLBP]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[UBE4B]] | -0.45 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[SEL1L]] | -0.44 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[GMPPA]] | -0.44 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[SCARB1]] | -0.44 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6]] | B | FRMD6 activity raises CDK17's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 1.55× lower at baseline in the lines without FRMD6 | 0.017 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[LINC02454]] | B | LINC02454 activity raises CDK17's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without LINC02454 | 0.049 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[AMOTL1]] | B | AMOTL1 activity raises CDK17's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without AMOTL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[FJX1]] | B | FJX1 activity raises CDK17's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without FJX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, 9.1); signed map (9.7, 45.8). **Vector** length 93.0, 31.4% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.1 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.3 | +0.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.9 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | -1.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.6 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +0.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:96,278,261-96,400,480 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCTAIRE2; previously PCTK2 |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00537](https://www.uniprot.org/uniprotkb/Q00537) (Cyclin-dependent kinase 17):

> May play a role in terminally differentiated neurons. Has a Ser/Thr-phosphorylating activity for histone H1 (By similarity).

**Summary**, from NCBI Gene [5128](https://www.ncbi.nlm.nih.gov/gene/5128):

> The protein encoded by this gene belongs to the cdc2/cdkx subfamily of the ser/thr family of protein kinases. It has similarity to a rat protein that is thought to play a role in terminally differentiated neurons. Alternatively spliced transcript variants encoding different isoforms have been found. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:8750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8750) · Entrez [5128](https://www.ncbi.nlm.nih.gov/gene/5128) · UniProt [Q00537](https://www.uniprot.org/uniprotkb/Q00537) · Ensembl [ENSG00000059758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059758)

## Data

Gene col 678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 678); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 678]; `tensor/DDL_lfc|DDL_z.npy` [678]; `embed/gene_vectors.npy` [678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 678 or target_col == 678). Every well: [[CDK17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
