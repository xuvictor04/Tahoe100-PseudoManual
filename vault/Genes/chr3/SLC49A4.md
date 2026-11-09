---
symbol: "SLC49A4"
type: "gene"
col: 6182
ensembl_id: "ENSG00000138463"
name: "solute carrier family 49 member 4"
location: "3q21.1"
module: 232
arm: "+"
pooled_cpm: 44.45
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 24
n_dd_up_clean: 17
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/232"]
generated_by: "tahoemap"
---

# SLC49A4

*solute carrier family 49 member 4* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +20.4, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.560× (z -10.4, q 1e-22, down in 37 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.451× (z -7.5, q 9e-12, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPBAP1]] (+0.67, fdr 8e-06, ⚠ same locus), [[TLCD5]] (+0.62, fdr 1e-05), [[ZBTB44]] (+0.60, fdr 1e-05), [[GARRE1]] (+0.59, fdr 4e-05); moves opposite to [[ATP8B3]] (-0.55, fdr 9e-05), [[BMS1]] (-0.54, fdr 2e-05), [[SLC25A10]] (-0.53, fdr 3e-05).
> It is in [[Module 232]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FOXC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +20.4 | 0e+00 | 45/48 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.41×** | +8.7 | 1e-15 | 36/48 (SW1417, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.4 | 1e-14 | 34/47 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.52×** | +7.5 | 7e-12 | 38/48 (SW1417, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.8 | 6e-07 | 24/46 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.5 | 3e-06 | 26/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.3 | 7e-06 | 22/49 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.3 | 8e-06 | 23/47 (BT-474, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +4.9 | 7e-05 | 21/49 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.59×** | +4.4 | 7e-04 | 22/48 (AsPC-1, BT-474, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 23/47 (KATO III, LoVo, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 1e-03 | 20/47 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.002 | 20/48 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +4.0 | 0.003 | 13/48 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.004 | 18/48 (AsPC-1, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.005 | 21/47 (BT-474, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.16× | +3.8 | 0.005 | 13/48 (A498, A549, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.006 | 18/49 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.012 | 13/47 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.013 | 9/49 (NCI-H460, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.560×** | -10.4 | 1e-22 | 37/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.583×** | -9.0 | 9e-17 | 31/43 (LoVo, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.604×** | -8.7 | 7e-16 | 34/47 (PANC-1, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.631×** | -8.3 | 2e-14 | 30/47 (NCI-H460, A-427, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.451×** | -7.5 | 9e-12 | 35/48 (SW48, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.455×** | -7.4 | 1e-11 | 31/49 (A549, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.686×** | -6.5 | 6e-09 | 22/41 (SK-MEL-2, Panc 03.27, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -6.2 | 5e-08 | 31/47 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.642×** | -5.7 | 9e-07 | 27/48 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.551×** | -5.6 | 1e-06 | 29/47 (Panc 03.27, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.564×** | -5.4 | 4e-06 | 26/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.578×** | -5.1 | 1e-05 | 24/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -5.1 | 1e-05 | 24/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.744×** | -5.1 | 1e-05 | 22/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.767×** | -4.7 | 8e-05 | 25/47 (C-33 A, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.770×** | -4.7 | 1e-04 | 25/48 (PANC-1, SW48, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.773×** | -4.3 | 5e-04 | 19/48 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.657×** | -3.9 | 0.002 | 20/46 (NCI-H460, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.003 | 17/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.752×** | -3.6 | 0.007 | 17/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.866× | -3.6 | 0.008 | 10/48 (LS 180, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.8 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -19.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.444× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 39.5 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H1573 (line)]] | alt | 58.7 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -15.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 60.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.178× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 107 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +13.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.291× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 27.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +12.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.289× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 65.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +19.8) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 54.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 27.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 58.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.384× (z -8.6) |
| [[LS 180 (line)]] | wt | 24.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.287× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 45.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.9) | [[PH-797804 (drug)]] 5 µM 0.0258× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 37.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[BT-474 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 64.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.333× (z -8.6) |
| [[C32 (line)]] | wt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.67× (z +16.9) | — |
| [[H4 (line)]] | wt | 47.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +15.5) | — |
| [[Hs 766T (line)]] | wt | 30.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +12.2) | — |
| [[J82 (line)]] | alt | 39.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.5) | — |
| [[KATO III (line)]] | alt | 42.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -8.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H2030 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -10.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SNU-423 (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SW 900 (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 74.3 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.88× (z +9.0) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[A-172 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPBAP1]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 | STRING 746; ⚠ same locus (1.2 kb: neighbours can correlate without regulation) |
| [[TLCD5]] | +0.62 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ZBTB44]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[GARRE1]] | +0.59 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[AGO4]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[CREBRF]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[DPY19L2P3]] | +0.58 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ZNRF2P2]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CAB39L]] | +0.57 | +0.62 / +0.27 | both halves | 3e-04 |  |
| [[ISCU]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[FOXC1]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ORMDL1]] | +0.56 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[C14orf28]] | +0.56 | +0.35 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP8B3]] | -0.55 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[BMS1]] | -0.54 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[SLC25A10]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[RPGRIP1L]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SF3A3]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[LRRC59]] | -0.50 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[SCART1]] | -0.50 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[PDHA1]] | -0.50 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SCFD2]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[CS]] | -0.49 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[FAM98A]] | -0.49 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[DLAT]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXC1]] | C | FOXC1 activity lowers SLC49A4's level | lines that do not express FOXC1 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without FOXC1 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 232]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.4, -43.1); signed map (-13.4, 12.4). **Vector** length 112, 31.4% of its response variance represented; |z| ≥ 3 in 1,299 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +20.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +8.8 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.2 | +3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +5.8 | +7.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -10.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.0 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 49 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,795,069-122,881,139 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14784, RCC4; previously DIRC2 |
| Gene groups (HGNC) | Solute carrier family 49 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SL1](https://www.uniprot.org/uniprotkb/Q96SL1) (Solute carrier family 49 member 4):

> Mediates H(+)-dependent pyridoxine transport.

**Summary**, from NCBI Gene [84925](https://www.ncbi.nlm.nih.gov/gene/84925):

> This gene encodes a membrane-bound protein from the major facilitator superfamily of transporters. Disruption of this gene by translocation has been associated with haplo-insufficiency and renal cell carcinomas. Alternatively spliced transcript variants have been described, but their biological validity has not yet been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16628) · Entrez [84925](https://www.ncbi.nlm.nih.gov/gene/84925) · UniProt [Q96SL1](https://www.uniprot.org/uniprotkb/Q96SL1) · Ensembl [ENSG00000138463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138463)

## Data

Gene col 6182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6182); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6182]; `tensor/DDL_lfc|DDL_z.npy` [6182]; `embed/gene_vectors.npy` [6182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6182 or target_col == 6182). Every well: [[SLC49A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC49A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
