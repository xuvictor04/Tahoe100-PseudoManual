---
symbol: "TJP1"
type: "gene"
col: 2412
ensembl_id: "ENSG00000104067"
name: "tight junction protein 1"
location: "15q13.1"
module: 164
arm: "+"
pooled_cpm: 354.64
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# TJP1

*tight junction protein 1* — 15q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.67× (z +15.2, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.682× (z -16.7, q 0e+00, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EZR]] (+0.58, fdr 1e-05), [[ROCK2]] (+0.56, fdr 2e-05), [[SGMS2]] (+0.56, fdr 1e-05); moves opposite to [[METTL22]] (-0.65, fdr 1e-05), [[TRMU]] (-0.63, fdr 1e-05), [[TRIT1]] (-0.61, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ANXA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +15.2 | 0e+00 | 40/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +14.3 | 8e-44 | 33/48 (HOP62, SNU-423, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +11.7 | 1e-29 | 37/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +11.3 | 2e-27 | 39/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +8.4 | 4e-15 | 31/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +7.8 | 5e-13 | 29/48 (NCI-H460, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +7.8 | 7e-13 | 28/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +7.6 | 3e-12 | 30/48 (LS 180, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +7.0 | 2e-10 | 31/47 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +6.7 | 1e-09 | 24/47 (LS 180, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +6.6 | 2e-09 | 23/48 (NCI-H460, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +6.2 | 2e-08 | 24/47 (LS 180, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +6.2 | 3e-08 | 26/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +5.7 | 4e-07 | 17/49 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +5.3 | 4e-06 | 19/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.30×** | +4.2 | 8e-04 | 23/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.001 | 21/49 (HepG2/C3A, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.14× | +4.1 | 0.002 | 16/48 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.005 | 18/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.08× | +3.5 | 0.014 | 5/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | 1.11× | +3.2 | 0.033 | 14/48 (AsPC-1, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2412.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -16.7 | 0e+00 | 37/49 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.688×** | -16.3 | 0e+00 | 41/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.710×** | -10.2 | 6e-22 | 31/47 (RKO, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.736×** | -9.2 | 8e-18 | 36/48 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.763×** | -8.3 | 8e-15 | 29/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.773×** | -7.9 | 2e-13 | 28/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.777×** | -7.5 | 5e-12 | 30/48 (HT-29, SNU-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.636×** | -7.3 | 2e-11 | 35/47 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.791×** | -7.2 | 3e-11 | 26/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.797×** | -7.0 | 2e-10 | 25/49 (SNU-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.795×** | -6.8 | 6e-10 | 27/44 (SNU-1, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.811×** | -6.4 | 6e-09 | 28/48 (J82, HS-578T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.812×** | -6.2 | 2e-08 | 26/48 (A549, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.818×** | -6.2 | 2e-08 | 26/49 (BT-474, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.819×** | -6.2 | 3e-08 | 28/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.831×** | -5.7 | 4e-07 | 24/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -4.7 | 8e-05 | 20/48 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.868× | -4.4 | 4e-04 | 11/48 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.774×** | -4.1 | 1e-03 | 18/48 (SNU-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.910× | -4.1 | 0.001 | 9/48 (A549, NCI-H2030, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.917× | -3.8 | 0.004 | 9/48 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.925× | -3.4 | 0.017 | 7/48 (SNU-1, SW1417, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.894× | -3.3 | 0.024 | 5/47 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.900× | -3.2 | 0.024 | 3/48 (C-33 A, hTERT-HPNE, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 253 | 12 (6 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +19.3) | [[Selinexor (drug)]] 5 µM 0.648× (z -10.2) |
| [[HT-29 (line)]] | alt | 1,192 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -19.3) |
| [[AsPC-1 (line)]] | alt | 620 | 1 | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -15.8) |
| [[SNU-1 (line)]] | wt | 1,390 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -21.5) |
| [[BT-474 (line)]] | alt | 266 | 6 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +11.0) | [[Selinexor (drug)]] 5 µM 0.621× (z -10.2) |
| [[HOP62 (line)]] | alt | 186 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +19.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.87× (z +14.6) | [[Selinexor (drug)]] 5 µM 0.621× (z -9.7) |
| [[A-427 (line)]] | wt | 278 | 4 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +15.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.86× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -12.4) |
| [[A549 (line)]] | wt | 490 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +16.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.37× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -18.2) |
| [[LoVo (line)]] | wt | 744 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -17.3) |
| [[SW1417 (line)]] | alt | 478 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -19.8) |
| [[C32 (line)]] | wt | 140 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.521× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 424 | 2 (1 ⚠) | 4 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.77× (z +9.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 1.64× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 134 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.28× (z +9.2) | [[Selinexor (drug)]] 5 µM 0.535× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 550 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -15.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.541× (z -14.7) |
| [[SW 900 (line)]] | alt | 237 | 4 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.568× (z -11.7) |
| [[HCT15 (line)]] | alt | 308 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 429 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.83× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 634 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -14.0) |
| [[PANC-1 (line)]] | alt | 227 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +13.9) | — |
| [[SW48 (line)]] | wt | 539 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -16.1) |
| [[KATO III (line)]] | alt | 511 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -20.8) |
| [[RKO (line)]] | wt | 334 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -18.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.542× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 464 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.23× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -13.2) |
| [[H4 (line)]] | wt | 211 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.44× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.495× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 196 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.64× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 310 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 2.65× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 254 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +15.6) ⚠ cell-cycle shift, explains ~30% of this change | [[Selinexor (drug)]] 5 µM 0.580× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 236 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 250 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.87× (z +9.7) | [[Selinexor (drug)]] 5 µM 0.574× (z -12.7) |
| [[SNU-423 (line)]] | alt | 113 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +16.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.45× (z +9.5) | — |
| [[SW480 (line)]] | alt | 294 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -11.3) |
| [[A-172 (line)]] | wt | 189 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 1.74× (z +8.8) ⚠ toxic | [[Selinexor (drug)]] 5 µM 0.553× (z -13.6) |
| [[A498 (line)]] | wt | 317 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Selinexor (drug)]] 5 µM 0.575× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 237 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 158 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.448× (z -16.7) |
| [[NCI-H2030 (line)]] | alt | 336 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.536× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 170 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 291 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 292 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -10.5) |
| [[AN3 CA (line)]] | alt | 261 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 510 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 202 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 259 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 601 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 243 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EZR]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 | STRING 883 |
| [[ROCK2]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SGMS2]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ARAP2]] | +0.56 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[CLTB]] | +0.55 | +0.35 / +0.60 | both halves | 1e-04 | pathway: Gap junction trafficking and regulation |
| [[MISP]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LMO7]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 | same gene group |
| [[RAPH1]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ANXA3]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[DIAPH1]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PTPN21]] | +0.52 | +0.39 / +0.56 | both halves | 6e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[KRTAP5-AS1]] | +0.52 | +0.38 / +0.54 | both halves | 6e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL22]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[TRMU]] | -0.63 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[TRIT1]] | -0.61 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[GGA2]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PMS2CL]] | -0.58 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[TAF11]] | -0.57 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[C12orf76]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[ASB7]] | -0.55 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[ZNF8-DT]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[MED6]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FNTB]] | -0.53 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[VDAC1P8]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA3]] | B | ANXA3 activity raises TJP1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without ANXA3 | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[CLIC5]] | B | CLIC5 activity raises TJP1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 1.95× lower at baseline in the lines without CLIC5 | 0.010 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[C6orf132]] | B | C6orf132 activity raises TJP1's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without C6orf132 | 0.034 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[C1orf116]] | B | C1orf116 activity raises TJP1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without C1orf116 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MISP]] | B | MISP activity raises TJP1's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.67× lower at baseline in the lines without MISP | 0.080 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[EPB41L4A]] | B | EPB41L4A activity raises TJP1's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 1.34× lower at baseline in the lines without EPB41L4A | 0.099 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction -0.529). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, -19.9); signed map (5.8, 33.9). **Vector** length 130, 45.7% of its response variance represented; |z| ≥ 3 in 1,688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +15.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +7.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.1 | +11.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.8 | +7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.2 | +5.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.4 | +6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +0.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -12.7 | -16.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -8.0 | -9.2 |
|  | [[NG25 (drug)]] 5 µM |  | -5.1 | -7.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | -4.7 | -6.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.5 | -6.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.8 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | tight junction protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.1 — chr15:29,699,367-29,968,915 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZO-1, MGC133289, DKFZp686M05161 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; ZU5 domain containing ; SH3 domain containing |
| Hallmark sets | TGF_BETA_SIGNALING, UV_RESPONSE_DN, APICAL_JUNCTION |
| Reactome | 19 pathways, smallest: Regulation of gap junction activity; RUNX1 regulates expression of components of tight junctions; SARS-CoV-2 targets PDZ proteins in cell-cell junction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07157](https://www.uniprot.org/uniprotkb/Q07157) (Tight junction protein 1):

> TJP1, TJP2, and TJP3 are closely related scaffolding proteins that link tight junction (TJ) transmembrane proteins such as claudins, junctional adhesion molecules, and occludin to the actin cytoskeleton. Forms a multistranded TJP1/ZO1 condensate which elongates to form a tight junction belt, the belt is anchored at the apical cell membrane via interaction with PATJ (By similarity). The tight junction acts to limit movement of substances through the paracellular space and as a boundary between …

**Summary**, from NCBI Gene [7082](https://www.ncbi.nlm.nih.gov/gene/7082):

> This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family of proteins, and acts as a tight junction adaptor protein that also regulates adherens junctions. Tight junctions regulate the movement of ions and macromolecules between endothelial and epithelial cells. The multidomain structure of this scaffold protein, including a postsynaptic density 95/disc-large/zona occludens (PDZ) domain, a Src homology (SH3) domain, a guanylate kinase (GuK) domain and unique (U) …

**Accessions** — [HGNC:11827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11827) · Entrez [7082](https://www.ncbi.nlm.nih.gov/gene/7082) · UniProt [Q07157](https://www.uniprot.org/uniprotkb/Q07157) · Ensembl [ENSG00000104067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104067)

## Data

Gene col 2412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2412); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2412]; `tensor/DDL_lfc|DDL_z.npy` [2412]; `embed/gene_vectors.npy` [2412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2412 or target_col == 2412). Every well: [[TJP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TJP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
