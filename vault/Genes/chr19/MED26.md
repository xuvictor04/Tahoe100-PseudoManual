---
symbol: "MED26"
type: "gene"
col: 2546
ensembl_id: "ENSG00000105085"
name: "mediator complex subunit 26"
location: "19p13.11"
module: 40
arm: "+"
pooled_cpm: 57.05
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# MED26

*mediator complex subunit 26* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.24× (z +11.9, q 4e-30, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.240× (z -16.5, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.594× (z -5.8, q 1e-06, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPM1]] (+0.81, fdr 7e-06), [[TBC1D22A-DT]] (+0.80, fdr 7e-06), [[QPCTL]] (+0.78, fdr 7e-06); moves opposite to [[LIG4]] (-0.73, fdr 7e-06), [[COA7]] (-0.70, fdr 7e-06), [[NHLRC2]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.24×** | +11.9 | 4e-30 | 48/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.50×** | +10.6 | 1e-23 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +10.5 | 1e-23 | 45/49 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.34×** | +9.8 | 2e-20 | 48/48 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.11×** | +8.6 | 9e-16 | 39/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.76×** | +8.0 | 1e-13 | 41/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.95×** | +7.7 | 1e-12 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.60×** | +5.4 | 4e-06 | 30/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +5.2 | 1e-05 | 35/48 (Panc 03.27, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 3e-05 | 33/48 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.32×** | +4.5 | 3e-04 | 38/49 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +4.4 | 5e-04 | 28/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.46×** | +4.2 | 0.001 | 26/50 (NCI-H23, SW48, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.44×** | +4.0 | 0.002 | 28/48 (SW48, RKO, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +4.0 | 0.003 | 29/48 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.004 | 27/48 (SW480, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.012 | 26/49 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.070 | 20/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.240×** | -16.5 | 0e+00 | 47/49 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.241×** | -15.8 | 0e+00 | 40/42 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.594×** | -5.8 | 1e-06 | 40/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.708×** | -3.6 | 0.053 | 26/49 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.724×** | -3.3 | 0.070 | 28/49 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.738×** | -3.3 | 0.070 | 22/45 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | **0.756×** | -3.3 | 0.070 | 24/47 (RPMI-7951, COLO 205, …) | rises with dose | position effect removed |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **0.743×** | -3.2 | 0.070 | 21/49 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.730×** | -3.2 | 0.070 | 22/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.760×** | -3.2 | 0.070 | 24/48 (A-172, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.734×** | -3.2 | 0.070 | 21/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.735×** | -3.2 | 0.070 | 19/49 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.1 | 0.072 | 0/49 | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.829×** | -3.1 | 0.079 | 21/48 (H4, RPMI-7951, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.604×** | -3.1 | 0.085 | 19/48 (NCI-H2347, SNU-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.9 | 8 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.54× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 47.1 | 7 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.33× (z +15.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.1× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -20.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 50.9 | 5 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.39× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -10.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.7 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.48× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 54.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 23.0× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 61.9 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0388× (z -25.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 30.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.93× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0473× (z -21.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 63.6 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 33.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.78× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.67× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.5× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 54.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.86× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 97.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0860× (z -23.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 110 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.4× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -13.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 81.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0644× (z -20.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 78.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0886× (z -17.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 68.9 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 15.4× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 82.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -15.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 61.2 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.263× (z -8.5) |
| [[HS-578T (line)]] | alt | 90.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 31.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 63.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -13.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 46.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -12.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 61.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 67.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 58.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.38× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -13.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 66.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.13× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -17.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 63.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.14× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 66.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -15.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0921× (z -15.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 72.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -9.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 51.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 32.9× (z +11.5) | — |
| [[H4 (line)]] | wt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0536× (z -18.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 66.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -16.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -12.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 48.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H661 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -8.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0390× (z -20.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM1]] | +0.81 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.80 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.78 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.77 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ALKBH5]] | +0.75 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[MGAT1]] | +0.72 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[ABHD17B]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CRLS1]] | +0.70 | +0.70 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIG4]] | -0.73 | -0.69 / -0.71 | both halves | 7e-06 |  |
| [[COA7]] | -0.70 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[NHLRC2]] | -0.70 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[YTHDC2]] | -0.69 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.69 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[GCFC2]] | -0.65 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.65 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ZNF260]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.64 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.64 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.64 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MED26's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SPSB2]] | C | SPSB2's natural level weakens MED26's drug response | SPSB2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.03; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.772). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.7, -19.1); signed map (-42.2, 14.4). **Vector** length 113, 41.0% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +10.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.6 | +9.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.6 | +10.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +0.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -10.5 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.9 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.8 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,574,907-16,629,062 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRSP70; previously CRSP7 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O95402](https://www.uniprot.org/uniprotkb/O95402) (Mediator of RNA polymerase II transcription subunit 26):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9441](https://www.ncbi.nlm.nih.gov/gene/9441):

> The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for efficient activation by SP1. This protein is also a component of other multisubunit complexes e.g. …

**Accessions** — [HGNC:2376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2376) · Entrez [9441](https://www.ncbi.nlm.nih.gov/gene/9441) · UniProt [O95402](https://www.uniprot.org/uniprotkb/O95402) · Ensembl [ENSG00000105085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105085)

## Data

Gene col 2546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2546); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2546]; `tensor/DDL_lfc|DDL_z.npy` [2546]; `embed/gene_vectors.npy` [2546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2546 or target_col == 2546). Every well: [[MED26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
