---
symbol: "FOXM1"
type: "gene"
col: 3201
ensembl_id: "ENSG00000111206"
name: "forkhead box M1"
location: "12p13.33"
module: 22
arm: "+"
pooled_cpm: 32.59
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 33
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# FOXM1

*forkhead box M1* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.90× (z +19.1, q 0e+00, up in 37 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.40× (z +3.8, q 0.008, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.515× (z -8.3, q 6e-14, down in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~73% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.550× (z -7.5, q 1e-11, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPO]] (+0.86, fdr 7e-06), [[PLK4]] (+0.86, fdr 7e-06), [[KIF11]] (+0.84, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[DZIP1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 19 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.90×** | +19.1 | 0e+00 | 37/37 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **4.27×** | +18.2 | 0e+00 | 41/42 (A498, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.06×** | +12.9 | 5e-36 | 36/40 (HEC-1-A, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.81×** | +7.1 | 2e-10 | 30/45 (Panc 03.27, C32, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.45×** | +6.5 | 1e-08 | 38/46 (LoVo, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **1.71×** | +6.0 | 2e-07 | 31/44 (SW 900, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.54×** | +5.4 | 6e-06 | 26/45 (KATO III, HOP62, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.50×** | +5.1 | 3e-05 | 27/46 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.08×** | +4.8 | 1e-04 | 27/46 (HT-29, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +4.2 | 0.002 | 21/46 (HOP62, NCI-H23, …) | rises with dose | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.008 | 21/46 (HOP62, A498, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.39×** | +3.7 | 0.011 | 21/46 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +3.5 | 0.021 | 15/46 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.21×** | +3.4 | 0.026 | 15/45 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.65×** | +3.3 | 0.040 | 15/44 (J82, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 1.20× | +3.1 | 0.055 | 12/46 (HT-29, SW 900, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.30×** | +2.9 | 0.095 | 16/46 (HT-29, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.515×** | -8.3 | 6e-14 | 35/46 (A498, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.469×** | -7.7 | 3e-12 | 30/46 (H4, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -7.5 | 1e-11 | 27/46 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.686×** | -6.5 | 9e-09 | 31/46 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.594×** | -6.5 | 9e-09 | 31/46 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.612×** | -6.1 | 9e-08 | 26/46 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.517×** | -5.9 | 3e-07 | 32/46 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.723×** | -5.7 | 9e-07 | 27/46 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.726×** | -5.7 | 9e-07 | 29/46 (NCI-H460, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -5.1 | 2e-05 | 25/46 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.650×** | -4.8 | 8e-05 | 34/46 (NCI-H661, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.732×** | -3.9 | 0.005 | 19/46 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.707×** | -3.9 | 0.005 | 22/46 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.744×** | -3.7 | 0.009 | 24/46 (C32, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.011 | 19/46 (NCI-H23, NCI-H2030, …) | rises with dose | position effect removed |
| [[palbociclib (drug)]] 5 µM |  | **0.581×** | -3.5 | 0.012 | 19/45 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.581×** | -3.5 | 0.012 | 18/46 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.582×** | -3.5 | 0.012 | 18/45 (C32, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.724×** | -3.3 | 0.024 | 15/46 (RKO, AN3 CA, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.777×** | -3.1 | 0.040 | 10/45 (NCI-H1573, SW48, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.836× | -3.1 | 0.047 | 16/46 (HCT15, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 37.5 | 3 (3 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Selinexor (drug)]] 5 µM 0.217× (z -17.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.452× (z -9.0) |
| [[H4 (line)]] | wt | 45.3 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0370× (z -16.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.157× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 30.7 | 1 (1 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.115× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.269× (z -10.4) |
| [[A-427 (line)]] | wt | 122 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.190× (z -19.9) |
| [[MIA PaCa-2 (line)]] | alt | 39.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0628× (z -21.3) |
| [[SW480 (line)]] | alt | 45.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -12.8) |
| [[KATO III (line)]] | alt | 37.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.128× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.4) |
| [[A-172 (line)]] | wt | 26.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.51× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Selinexor (drug)]] 5 µM 0.291× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 64.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HOP62 (line)]] | alt | 38.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.89× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HT-29 (line)]] | alt | 28.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.5) |
| [[J82 (line)]] | alt | 54.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 26.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.25× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Selinexor (drug)]] 5 µM 0.285× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 39.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW48 (line)]] | wt | 33.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.87× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -9.9) |
| [[A549 (line)]] | wt | 20.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.47× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 24.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.210× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 20.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.4× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H23 (line)]] | alt | 79.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 19.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.56× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.246× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 21.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0186× (z -18.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SNU-423 (line)]] | alt | 17.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW 900 (line)]] | alt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW1417 (line)]] | alt | 45.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0505× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -9.2) |
| [[AN3 CA (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPO]] | +0.86 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[PLK4]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 | pathway: G2/M Transition; STRING 634 |
| [[KIF11]] | +0.84 | +0.83 / +0.85 | both halves | 7e-06 | STRING 934 |
| [[PRC1]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | STRING 870 |
| [[SPC25]] | +0.83 | +0.84 / +0.81 | both halves | 7e-06 | STRING 586 |
| [[MAD2L1]] | +0.83 | +0.83 / +0.86 | both halves | 7e-06 | STRING 710 |
| [[LMNB1]] | +0.82 | +0.81 / +0.83 | both halves | 7e-06 | STRING 429 |
| [[NCAPG]] | +0.82 | +0.80 / +0.84 | both halves | 7e-06 | STRING 860 |
| [[KIF22]] | +0.82 | +0.85 / +0.82 | both halves | 7e-06 | STRING 432 |
| [[BIRC5]] | +0.81 | +0.79 / +0.83 | both halves | 7e-06 | STRING 958 |
| [[PBK]] | +0.81 | +0.84 / +0.85 | both halves | 7e-06 | STRING 845 |
| [[BUB1B]] | +0.80 | +0.81 / +0.82 | both halves | 7e-06 | STRING 944 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DZIP1L]] | B | DZIP1L activity raises FOXM1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without DZIP1L | 0.015 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises FOXM1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.30× lower at baseline in the lines without E2F8 | 0.036 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises FOXM1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without MYBL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises FOXM1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.36× lower at baseline in the lines without NDC80 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises FOXM1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.97× lower at baseline in the lines without AURKB | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises FOXM1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.81× lower at baseline in the lines without PBK | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises FOXM1's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.66× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[MCM2]] | C | MCM2 activity raises FOXM1's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.42× lower at baseline in the lines without MCM2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises FOXM1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MCM3]] | C | MCM3 activity raises FOXM1's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 2.64× lower at baseline in the lines without MCM3 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.3, -52.7); signed map (-46.2, -44.0). **Vector** length 137, 47.6% of its response variance represented; |z| ≥ 3 in 1,273 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.63 to 60); *DREAM G2/M down* (control, mean cos +0.65 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.60 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +7.2 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +6.6 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +6.1 | +18.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.7 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | +4.7 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.8 | +1.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.6 | +0.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.5 | -7.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -6.3 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.8 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.2 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box M1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:2,857,680-2,877,174 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HFH-11, trident, HNF-3, INS-1, MPP2, MPHOSPH2, TGT3; previously FKHL16 |
| Gene groups (HGNC) | Forkhead boxes; FOXM1-MMB complex subunits |
| Reactome | 10 pathways, smallest: Polo-like kinase mediated events; Nuclear events stimulated by ALK signaling in cancer; Cyclin A/B1/B2 associated events during G2/M transition |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08050](https://www.uniprot.org/uniprotkb/Q08050) (Forkhead box protein M1):

> Transcription factor regulating the expression of cell cycle genes essential for DNA replication and mitosis. Plays a role in the control of cell proliferation. Also plays a role in DNA break repair, participating in the DNA damage checkpoint response. Promotes transcription of PHB2.; [Isoform 5]: Required for the activation of Rho-associated protein kinases ROCK1 and ROCK2 and promotes epithelial-mesenchymal transition. Enhances the activation of phosphatidylinositol 4,5-bisphosphate 3-kinase …

**Summary**, from NCBI Gene [2305](https://www.ncbi.nlm.nih.gov/gene/2305):

> The protein encoded by this gene is a transcriptional activator involved in cell proliferation. The encoded protein is phosphorylated in M phase and regulates the expression of several cell cycle genes, such as cyclin B1 and cyclin D1. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:3818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3818) · Entrez [2305](https://www.ncbi.nlm.nih.gov/gene/2305) · UniProt [Q08050](https://www.uniprot.org/uniprotkb/Q08050) · Ensembl [ENSG00000111206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111206)

## Data

Gene col 3201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3201); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3201]; `tensor/DDL_lfc|DDL_z.npy` [3201]; `embed/gene_vectors.npy` [3201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3201 or target_col == 3201). Every well: [[FOXM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
