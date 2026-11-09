---
symbol: "KDM2B"
type: "gene"
col: 1569
ensembl_id: "ENSG00000089094"
name: "lysine demethylase 2B"
location: "12q24.31"
module: 103
arm: "+"
pooled_cpm: 59.34
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 43
n_dd_up_clean: 4
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# KDM2B

*lysine demethylase 2B* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.29× (z +5.7, q 6e-06, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.428× (z -18.9, q 0e+00, down in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.534× (z -14.0, q 2e-42, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM2B-DT]] (+0.60, fdr 7e-06, ⚠ same locus), [[TMEM39B]] (+0.58, fdr 1e-05), [[PRR12]] (+0.56, fdr 1e-05), [[ATP23]] (+0.56, fdr 4e-05); moves opposite to [[ARPP19]] (-0.46, fdr 9e-05), [[DIAPH1]] (-0.46, fdr 7e-05), [[ADAMTSL5]] (-0.45, fdr 1e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SMAD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.7 | 6e-06 | 23/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +5.2 | 7e-05 | 25/48 (NCI-H1573, SW48, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +4.8 | 3e-04 | 18/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.095 | 14/48 (HT-29, PANC-1, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.099 | 8/48 (PANC-1, SW 900, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 5 µM |  | 1.30× | +3.1 | 0.21 | 2/48 (PANC-1, NCI-H1573) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.21 | 10/49 (NCI-H23, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.428×** | -18.9 | 0e+00 | 40/47 (C32, RKO, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.433×** | -17.3 | 0e+00 | 40/45 (C32, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -16.2 | 0e+00 | 34/43 (LOX-IMVI, C32, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.516×** | -14.7 | 0e+00 | 41/48 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.534×** | -14.0 | 2e-42 | 37/48 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.536×** | -13.4 | 9e-39 | 36/47 (J82, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.554×** | -13.2 | 1e-37 | 37/48 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.558×** | -13.0 | 9e-37 | 37/48 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.693×** | -11.5 | 8e-29 | 37/48 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.627×** | -10.4 | 1e-23 | 33/48 (C32, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -10.3 | 5e-23 | 33/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -10.2 | 1e-22 | 34/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.644×** | -9.8 | 6e-21 | 35/48 (C32, PANC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -9.8 | 7e-21 | 34/48 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.686×** | -8.4 | 2e-15 | 31/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.703×** | -7.8 | 2e-13 | 32/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -7.8 | 2e-13 | 25/48 (C32, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -7.5 | 3e-12 | 28/48 (C32, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -7.2 | 1e-11 | 30/48 (C32, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.724×** | -6.9 | 1e-10 | 28/48 (C32, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~14% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 282 | 0 | 27 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0361× (z -36.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0711× (z -30.6) |
| [[LOX-IMVI (line)]] | wt | 159 | 0 | 21 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0120× (z -37.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.122× (z -17.9) |
| [[hTERT-HPNE (line)]] | wt | 92.2 | 0 | 17 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0870× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.189× (z -15.2) |
| [[J82 (line)]] | alt | 119 | 2 (1 ⚠) | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +38.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.69× (z +14.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.196× (z -18.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.234× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 56.3 | 0 | 14 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.288× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -23.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -19.1) |
| [[PANC-1 (line)]] | alt | 57.4 | 2 (1 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +22.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.79× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.415× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 74.4 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.253× (z -13.1) |
| [[HOP62 (line)]] | alt | 71.0 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.344× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 80.9 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -14.7) |
| [[A-172 (line)]] | wt | 71.2 | 4 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +39.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.19× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.0501× (z -32.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.444× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 59.9 | 3 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +25.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.20× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.370× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 63.4 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -11.4) |
| [[SNU-423 (line)]] | alt | 45.3 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.353× (z -9.3) |
| [[A498 (line)]] | wt | 43.6 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 69.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.312× (z -11.7) |
| [[SW 900 (line)]] | alt | 63.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.354× (z -8.9) |
| [[C-33 A (line)]] | alt | 146 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 34.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -11.3) |
| [[A549 (line)]] | wt | 29.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +21.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -13.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0734× (z -16.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -16.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 45.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 31.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 32.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +30.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 51.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -10.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 90.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.316× (z -9.6) |
| [[BT-474 (line)]] | alt | 38.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.326× (z -8.9) |
| [[SW480 (line)]] | alt | 33.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.455× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -15.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +20.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0684× (z -13.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 48.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 73.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -8.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -10.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM2B-DT]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TMEM39B]] | +0.58 | +0.53 / +0.51 | both halves | 1e-05 | same gene group |
| [[PRR12]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ATP23]] | +0.56 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[NR2F2]] | +0.55 | +0.41 / +0.65 | both halves | 4e-05 | same gene group |
| [[SMAD9]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[BCL7A]] | +0.55 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[ZIC2]] | +0.54 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ING2]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 | same gene group |
| [[CCDC34]] | +0.53 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NOG]] | +0.53 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[ABL1]] | +0.52 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[PPFIA3]] | +0.52 | +0.58 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPP19]] | -0.46 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[DIAPH1]] | -0.46 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ADAMTSL5]] | -0.45 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[PDZD8]] | -0.45 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[DSG2]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[LINC02474]] | -0.44 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[PDLIM5]] | -0.44 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[RAB10]] | -0.43 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[TMEM241]] | -0.43 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[C5orf63]] | -0.42 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD9]] | B | SMAD9 activity raises KDM2B's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 2.07× lower at baseline in the lines without SMAD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises KDM2B's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without KDM2B-DT | 0.034 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[TET1]] | B | TET1 activity raises KDM2B's level | lines that do not express TET1 (12) vs lines expressing it (38) | 1.73× lower at baseline in the lines without TET1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[NRN1]] | B | NRN1 activity strengthens KDM2B's drug response | lines that do not express NRN1 (27) vs lines expressing it (22) | the lines without NRN1 respond 0.75× as strongly (z diff +1.38); strongest at Dinaciclib 0.5 µM: 0.43x vs 0.30x (z diff +3.1) | 0.071 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137; target measured in part of the lines; artifact flags |
| [[SMAD9]] | B | SMAD9 activity strengthens KDM2B's drug response | lines that do not express SMAD9 (11) vs lines expressing it (38) | the lines without SMAD9 respond 0.62× as strongly (z diff +2.72); strongest at Dinaciclib 0.5 µM: 0.67x vs 0.31x (z diff +4.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.0, -19.8); signed map (-32.7, 32.5). **Vector** length 112, 33.2% of its response variance represented; |z| ≥ 3 in 1,472 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.7 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.5 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | -6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.7 | +4.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +5.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.0 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.6 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.1 | -7.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -17.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -13.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.2 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,429,096-121,581,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCCX2, CXXC2, Fbl10, JHDM1B; previously FBXL10 |
| Gene groups (HGNC) | PHD finger proteins; Zinc fingers CXXC-type; F-box and leucine rich repeat proteins; MicroRNA protein coding host genes; Lysine demethylase 2 family |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHM5](https://www.uniprot.org/uniprotkb/Q8NHM5) (Lysine-specific demethylase 2B):

> Histone demethylase that demethylates 'Lys-4' and 'Lys-36' of histone H3, thereby playing a central role in histone code. Preferentially demethylates trimethylated H3 'Lys-4' and dimethylated H3 'Lys-36' residue while it has weak or no activity for mono- and tri-methylated H3 'Lys-36'. Preferentially binds the transcribed region of ribosomal RNA and represses the transcription of ribosomal RNA genes which inhibits cell growth and proliferation. May also serve as a substrate-recognition …

**Summary**, from NCBI Gene [84678](https://www.ncbi.nlm.nih.gov/gene/84678):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13610](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13610) · Entrez [84678](https://www.ncbi.nlm.nih.gov/gene/84678) · UniProt [Q8NHM5](https://www.uniprot.org/uniprotkb/Q8NHM5) · Ensembl [ENSG00000089094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089094)

## Data

Gene col 1569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1569); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1569]; `tensor/DDL_lfc|DDL_z.npy` [1569]; `embed/gene_vectors.npy` [1569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1569 or target_col == 1569). Every well: [[KDM2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
