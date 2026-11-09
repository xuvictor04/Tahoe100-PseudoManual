---
symbol: "UBE3D"
type: "gene"
col: 3989
ensembl_id: "ENSG00000118420"
name: "ubiquitin protein ligase E3D"
location: "6q14.1"
module: 33
arm: "+"
pooled_cpm: 74.97
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# UBE3D

*ubiquitin protein ligase E3D* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.90× (z +21.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.434× (z -16.3, q 0e+00, down in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.686× (z -10.8, q 3e-25, down in 30 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM241]] (+0.69, fdr 1e-05), [[FXN]] (+0.69, fdr 7e-06), [[SFXN4]] (+0.65, fdr 7e-06); moves opposite to [[USP11]] (-0.58, fdr 3e-05), [[FAM120AOS]] (-0.58, fdr 1e-04), [[FBXO8]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.90×** | +21.7 | 0e+00 | 48/48 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.81×** | +21.1 | 0e+00 | 47/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.75×** | +20.6 | 0e+00 | 48/48 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +15.1 | 0e+00 | 47/48 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +12.6 | 2e-34 | 42/48 (NCI-H2347, J82, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.42×** | +10.2 | 2e-22 | 32/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +9.3 | 8e-19 | 37/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +9.3 | 2e-18 | 40/48 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +7.9 | 1e-13 | 34/48 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.48×** | +7.8 | 3e-13 | 43/49 (J82, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.36×** | +6.3 | 1e-08 | 31/48 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +6.3 | 1e-08 | 30/49 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.31×** | +5.5 | 1e-06 | 27/48 (C32, HOP62, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.4 | 4e-04 | 23/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.65×** | +4.3 | 5e-04 | 27/48 (LOX-IMVI, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 23/48 (HT-29, LoVo, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 16/49 (KATO III, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.002 | 19/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 18/48 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.009 | 15/48 (HOP62, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.434×** | -16.3 | 0e+00 | 35/43 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.654×** | -12.2 | 5e-32 | 28/48 (PANC-1, A498, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.573×** | -11.3 | 2e-27 | 37/49 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -10.8 | 3e-25 | 30/49 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.623×** | -8.9 | 5e-17 | 28/45 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.673×** | -8.1 | 7e-14 | 38/48 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.394×** | -8.0 | 7e-14 | 39/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.706×** | -7.1 | 1e-10 | 31/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.704×** | -6.9 | 4e-10 | 28/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.751×** | -5.6 | 1e-06 | 30/47 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.781×** | -5.0 | 2e-05 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -4.2 | 0.001 | 22/48 (C32, LS 180, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.827×** | -3.8 | 0.005 | 21/47 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.830×** | -3.8 | 0.006 | 18/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.887× | -3.4 | 0.023 | 14/49 (SW480, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.690×** | -3.2 | 0.049 | 18/48 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 117 | 3 | 11 (10 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -31.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 74.4 | 4 | 9 (7 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.93× (z +13.5) | [[Harringtonine (drug)]] 5 µM 0.208× (z -18.9) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 97.3 | 1 | 9 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -18.8) |
| [[SNU-423 (line)]] | alt | 128 | 4 | 6 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -22.4) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.1) |
| [[A549 (line)]] | wt | 60.6 | 3 | 5 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.91× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -19.6) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 68.1 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 27.2 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.88× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.5) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HS-578T (line)]] | alt | 29.0 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.82× (z +15.0) | — |
| [[KATO III (line)]] | alt | 87.4 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.4 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +14.0) | — |
| [[SK-MEL-2 (line)]] | alt | 65.9 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.56× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.417× (z -8.7) |
| [[SW480 (line)]] | alt | 154 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.518× (z -10.3) |
| [[HT-29 (line)]] | alt | 75.2 | 5 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.56× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -9.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 58.4 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.60× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 108 | 5 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.67× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -12.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 100 | 1 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.5) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -12.3) |
| [[LS 180 (line)]] | wt | 95.3 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +11.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 94.3 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -11.1) |
| [[A-172 (line)]] | wt | 21.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 8.94× (z +14.2) | — |
| [[C32 (line)]] | wt | 51.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.57× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.0) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HEC-1-A (line)]] | alt | 158 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -15.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.29× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 83.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.87× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -17.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 21.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +13.1) | — |
| [[BT-474 (line)]] | alt | 57.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.69× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.1) ⚠ cell-cycle shift, explains ~70% of this change |
| [[CFPAC-1 (line)]] | alt | 27.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HepG2_C3A (line)]] | wt | 68.8 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -12.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 59.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +14.7) | — |
| [[RKO (line)]] | wt | 83.9 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.72× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 58.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.41× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 85.1 | 2 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.37× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 39.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.48× (z +13.8) | — |
| [[A-427 (line)]] | wt | 55.3 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.468× (z -11.8) |
| [[C-33 A (line)]] | alt | 112 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -21.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.03× (z +11.8) | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -14.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 60.8 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.22× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -10.9) |
| [[Hs 766T (line)]] | wt | 46.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -15.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 123 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.2) |
| [[CHP-212 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM241]] | +0.69 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[FXN]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SFXN4]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[RSAD1]] | +0.64 | +0.43 / +0.65 | both halves | 4e-05 |  |
| [[NARS2]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PPAT]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.63 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[EBPL]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[MCOLN2]] | +0.62 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[C20orf27]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NLE1]] | +0.62 | +0.40 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP11]] | -0.58 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[FAM120AOS]] | -0.58 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[FBXO8]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[STXBP2]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[UBE2A]] | -0.55 | -0.40 / -0.43 | both halves | 5e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[UBE3B]] | -0.54 | -0.30 / -0.50 | both halves | 2e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[RUSC1-AS1]] | -0.54 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[SP2]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ATXN1L]] | -0.54 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[CYLD]] | -0.53 | -0.30 / -0.60 | both halves | 2e-04 |  |
| [[CFLAR]] | -0.53 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[CGGBP1]] | -0.52 | -0.26 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises UBE3D's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without MCOLN2 | 0.012 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[ANK2]] | B | ANK2 activity raises UBE3D's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without ANK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[DUXAP10]] | B | DUXAP10 activity raises UBE3D's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without DUXAP10 | 0.033 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises UBE3D's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without SLC5A4-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[MEX3A]] | B | MEX3A activity raises UBE3D's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without MEX3A | 0.095 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.5, -40.7); signed map (-8.4, -54.2). **Vector** length 113, 35.1% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.6 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +12.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.8 | +10.2 |
|  | [[EX229 (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +9.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.6 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.5 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.1 | -10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -9.6 | -12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -5.7 | -6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -16.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.6 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:82,892,390-83,065,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434A1520, H10BH, YJR141W; previously C6orf157, UBE2CBP |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6J8](https://www.uniprot.org/uniprotkb/Q7Z6J8) (E3 ubiquitin-protein ligase E3D):

> E3 ubiquitin-protein ligase which accepts ubiquitin from specific E2 ubiquitin-conjugating enzymes, and transfers it to substrates, generally promoting their degradation by the proteasome. Independently of its E3 ubiquitin-protein ligase activity, acts as an inhibitor of CPSF3 endonuclease activity by blocking CPSF3 active site.

**Summary**, from NCBI Gene [90025](https://www.ncbi.nlm.nih.gov/gene/90025):

> Enables several functions, including cyclin binding activity; ribonuclease inhibitor activity; and ubiquitin-like protein conjugating enzyme binding activity. Involved in protein autoubiquitination; protein monoubiquitination; and protein polyubiquitination. Part of ubiquitin ligase complex. Is active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21381) · Entrez [90025](https://www.ncbi.nlm.nih.gov/gene/90025) · UniProt [Q7Z6J8](https://www.uniprot.org/uniprotkb/Q7Z6J8) · Ensembl [ENSG00000118420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118420)

## Data

Gene col 3989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3989); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3989]; `tensor/DDL_lfc|DDL_z.npy` [3989]; `embed/gene_vectors.npy` [3989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3989 or target_col == 3989). Every well: [[UBE3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
