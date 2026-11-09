---
symbol: "APOL2"
type: "gene"
col: 4877
ensembl_id: "ENSG00000128335"
name: "apolipoprotein L2"
location: "22q12.3"
module: 32
arm: "+"
pooled_cpm: 57.48
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 23
n_dd_up_clean: 18
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 27
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# APOL2

*apolipoprotein L2* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.55× (z +6.0, q 8e-07, up in 27 of 46 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.51× (z +5.8, q 1e-06, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.506× (z -14.1, q 3e-42, down in 32 of 45 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.508× (z -9.9, q 7e-21, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOBEC3F]] (+0.73, fdr 7e-06), [[APOL1]] (+0.71, fdr 7e-06, ⚠ same locus), [[GBP3]] (+0.71, fdr 7e-06), [[PSMB10]] (+0.70, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[APOL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.55×** | +6.0 | 8e-07 | 27/46 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +5.8 | 1e-06 | 32/46 (AsPC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +5.8 | 1e-06 | 29/45 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +5.7 | 2e-06 | 29/46 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +5.6 | 3e-06 | 30/47 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 1e-05 | 25/46 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.40×** | +5.2 | 2e-05 | 30/47 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.0 | 4e-05 | 26/46 (COLO 205, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 8e-05 | 26/46 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 6e-04 | 20/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 8e-04 | 24/46 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 9e-04 | 22/47 (AsPC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 25/46 (NCI-H2347, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +3.8 | 0.005 | 23/46 (RKO, LoVo, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.006 | 18/45 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.8 | 0.006 | 18/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.011 | 19/45 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.021 | 13/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.506×** | -14.1 | 3e-42 | 32/45 (COLO 205, A498, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.508×** | -9.9 | 7e-21 | 37/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.495×** | -9.9 | 7e-21 | 26/33 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.509×** | -9.9 | 7e-21 | 37/46 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.512×** | -9.8 | 2e-20 | 37/46 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.519×** | -8.9 | 7e-17 | 26/37 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.563×** | -8.4 | 3e-15 | 31/45 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.591×** | -7.4 | 1e-11 | 30/45 (COLO 205, A498, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -5.7 | 6e-07 | 32/47 (SNU-423, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.782×** | -5.1 | 2e-05 | 29/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.786×** | -5.0 | 3e-05 | 25/47 (A549, LoVo, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.732×** | -4.6 | 2e-04 | 27/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.735×** | -4.5 | 3e-04 | 24/46 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.735×** | -4.5 | 3e-04 | 24/46 (HEC-1-A, A549, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.558×** | -4.5 | 3e-04 | 23/45 (BT-474, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.627×** | -3.6 | 0.011 | 16/47 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.055 | 22/47 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.058 | 17/47 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.807×** | -3.0 | 0.077 | 15/46 (Hs 766T, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 171 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -33.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.259× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 304 | 2 | 8 (6 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.27× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.309× (z -12.8) |
| [[A498 (line)]] | wt | 138 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -27.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -11.6) |
| [[A549 (line)]] | wt | 81.5 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -23.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.275× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 86.0 | 4 (1 ⚠) | 3 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.60× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -15.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 78.1 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -15.8) |
| [[HS-578T (line)]] | alt | 89.8 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.53× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -12.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 74.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.451× (z -9.8) |
| [[SNU-423 (line)]] | alt | 90.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -16.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.153× (z -8.7) |
| [[A-172 (line)]] | wt | 46.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -13.9) |
| [[Hs 766T (line)]] | wt | 118 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1573 (line)]] | alt | 47.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.228× (z -10.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H2030 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 36.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.55× (z +10.3) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 38.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.1) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 20.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -10.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[C-33 A (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[C32 (line)]] | wt | 35.6 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.261× (z -9.7) |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0586× (z -10.2) |
| [[H4 (line)]] | wt | 76.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.256× (z -9.1) |
| [[HCT15 (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 66.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 43.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LS 180 (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +11.1) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.155× (z -13.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[PANC-1 (line)]] | alt | 32.3 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.54× (z +12.4) | — |
| [[RKO (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -16.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[RPMI-7951 (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW 1088 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0781× (z -9.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOBEC3F]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[APOL1]] | +0.71 | +0.59 / +0.78 | both halves | 7e-06 | same gene group; STRING 507; ⚠ same locus (13.1 kb: neighbours can correlate without regulation) |
| [[GBP3]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PSMB10]] | +0.70 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[CASP7]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SLC15A3]] | +0.70 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[TMEM140]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PHF11]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[PARP14]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[APOL6]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 | same gene group; STRING 400 |
| [[PARP10]] | +0.68 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[NMI]] | +0.68 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[IFI35]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 22, C 5. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOL3]] | B | APOL3 activity raises APOL2's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without APOL3 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[APOL1]] | B | APOL1 activity raises APOL2's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.25× lower at baseline in the lines without APOL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[RSAD2]] | B | RSAD2 activity raises APOL2's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without RSAD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[GBP4]] | B | GBP4 activity raises APOL2's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without GBP4 | 0.011 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IFI44]] | B | IFI44 activity raises APOL2's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.89× lower at baseline in the lines without IFI44 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[SPINK1]] | B | SPINK1 activity raises APOL2's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without SPINK1 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[SAMD9]] | B | SAMD9 activity raises APOL2's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without SAMD9 | 0.015 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[HERC6]] | B | HERC6 activity raises APOL2's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without HERC6 | 0.019 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises APOL2's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.98× lower at baseline in the lines without GBP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CASP10]] | B | CASP10 activity raises APOL2's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.84× lower at baseline in the lines without CASP10 | 0.027 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[APOL6]] | B | APOL6 activity raises APOL2's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without APOL6 | 0.030 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[CD5L]] | B | CD5L activity raises APOL2's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without CD5L | 0.030 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 53.0); signed map (61.4, 31.2). **Vector** length 131, 39.1% of its response variance represented; |z| ≥ 3 in 1,359 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.56 to 56); *interferon gamma response* (hallmark, mean cos +0.56 to 60); *interferon* (control, mean cos +0.57 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.0 | +4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.9 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.8 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +5.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.7 | -5.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.0 | -4.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.8 | -5.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.6 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.4 | -5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein L2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,226,209-36,239,954 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APOL-II |
| Gene groups (HGNC) | Apolipoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQE5](https://www.uniprot.org/uniprotkb/Q9BQE5) (Apolipoprotein L2):

> May affect the movement of lipids in the cytoplasm or allow the binding of lipids to organelles.

**Summary**, from NCBI Gene [23780](https://www.ncbi.nlm.nih.gov/gene/23780):

> This gene is a member of the apolipoprotein L gene family. The encoded protein is found in the cytoplasm, where it may affect the movement of lipids or allow the binding of lipids to organelles. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:619) · Entrez [23780](https://www.ncbi.nlm.nih.gov/gene/23780) · UniProt [Q9BQE5](https://www.uniprot.org/uniprotkb/Q9BQE5) · Ensembl [ENSG00000128335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128335)

## Data

Gene col 4877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4877); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4877]; `tensor/DDL_lfc|DDL_z.npy` [4877]; `embed/gene_vectors.npy` [4877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4877 or target_col == 4877). Every well: [[APOL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
