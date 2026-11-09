---
symbol: "MFSD14B"
type: "gene"
col: 7242
ensembl_id: "ENSG00000148110"
name: "solute carrier family 71 member 2"
location: "9q22.32"
module: 163
arm: "+"
pooled_cpm: 52.33
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# MFSD14B

*solute carrier family 71 member 2* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (18 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.10× (z +17.5, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.57× (z +10.6, q 2e-24, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.821× (z -4.6, q 0.002, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 0.342×, RKO 0.318×, PANC-1 0.497×; ⚠ cell-cycle shift, explains ~89% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.213×, C-33 A 0.208×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.108×, A-172 0.427×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAR1]] (+0.72, fdr 7e-06), [[CCNY]] (+0.69, fdr 7e-06), [[ABHD12]] (+0.69, fdr 7e-06); moves opposite to [[CWC22]] (-0.71, fdr 7e-06), [[THAP1]] (-0.69, fdr 7e-06), [[TRIP11]] (-0.68, fdr 7e-06).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GFOD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.10×** | +17.5 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.89×** | +15.0 | 0e+00 | 46/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.71×** | +12.7 | 1e-34 | 42/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +11.3 | 2e-27 | 38/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.64×** | +11.3 | 2e-27 | 38/47 (SNU-423, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.61×** | +11.2 | 4e-27 | 37/48 (SW480, Hs 766T, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +10.6 | 2e-24 | 39/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.36×** | +10.3 | 4e-23 | 32/48 (HEC-1-A, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.51×** | +9.0 | 2e-17 | 32/45 (NCI-H460, Hs 766T, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.41×** | +8.1 | 4e-14 | 33/48 (J82, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +7.2 | 3e-11 | 31/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +7.1 | 6e-11 | 28/48 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.36×** | +7.1 | 8e-11 | 22/41 (A549, HOP62, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.36×** | +6.9 | 2e-10 | 27/49 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.29×** | +6.0 | 6e-08 | 26/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.9 | 1e-07 | 25/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +5.5 | 1e-06 | 23/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +5.1 | 1e-05 | 21/48 (SNU-423, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 1e-05 | 24/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +4.4 | 3e-04 | 15/48 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.011 | 11/48 (SW 900, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.015 | 12/48 (NCI-H460, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.029 | 15/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7242.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 0.342×, RKO 0.318×, PANC-1 0.497×; ⚠ cell-cycle shift, explains ~89% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.213×, C-33 A 0.208×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.108×, A-172 0.427×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.821×** | -4.6 | 0.002 | 21/48 (A-172, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.846× | -3.9 | 0.020 | 15/48 (H4, KATO III, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.851× | -3.8 | 0.020 | 17/48 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.837× | -3.8 | 0.020 | 10/48 (SW48, SW1417, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.738×** | -3.8 | 0.020 | 14/47 (KATO III, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.859× | -3.6 | 0.030 | 11/48 (SNU-423, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.5 | 0.032 | 15/48 (AN3 CA, A-172, …) | two highest doses | composition shift |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.862× | -3.5 | 0.032 | 9/48 (SW1417, SNU-423, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.05 µM |  | 0.849× | -3.5 | 0.034 | 8/48 (SW 1271, Panc 03.27, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.876× | -3.1 | 0.10 | 12/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.874× | -3.1 | 0.11 | 8/48 (SNU-423, SW 900, …) | top dose only | plate-row cell shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.880× | -3.0 | 0.11 | 7/48 (A498, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 40.7 | 4 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +10.3) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.497× (z -9.9) ⚠ cell-cycle shift, explains ~89% of this change |
| [[NCI-H460 (line)]] | wt | 56.1 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +10.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 84.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -14.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Hs 766T (line)]] | wt | 46.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[LoVo (line)]] | wt | 51.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +10.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 48.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.6) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 5 µM 0.213× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[HOP62 (line)]] | alt | 37.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | [[Lonafarnib (drug)]] 5 µM 0.0942× (z -11.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 54.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 62.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 66.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 54.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.02× (z +8.6) | — |
| [[A498 (line)]] | wt | 76.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 54.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | — |
| [[AN3 CA (line)]] | alt | 63.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[H4 (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.160× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HT-29 (line)]] | alt | 57.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H23 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.2) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[RKO (line)]] | wt | 77.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -12.5) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SNU-423 (line)]] | alt | 44.0 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW1417 (line)]] | alt | 71.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[AsPC-1 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAR1]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[CCNY]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ABHD12]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.69 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[NUP93]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[RNF38]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[UBP1]] | +0.66 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.66 | +0.74 / +0.58 | both halves | 7e-06 | same gene group |
| [[AKT1]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NIPA2]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MAST2]] | +0.64 | +0.73 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC22]] | -0.71 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[THAP1]] | -0.69 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[TRIP11]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[MFAP1]] | -0.66 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[SEC62]] | -0.66 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.64 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[ZKSCAN1]] | -0.64 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[MYSM1]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ZNF585A]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[HELQ]] | -0.62 | -0.58 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GFOD1]] | B | GFOD1 activity raises MFSD14B's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without GFOD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[IMPA2]] | C | IMPA2 activity raises MFSD14B's level | lines that do not express IMPA2 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without IMPA2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ATP11A, PLEKHG3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.3, -6.6); signed map (-41.8, -14.9). **Vector** length 104, 27.5% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.7 | +11.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +3.9 | +11.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.5 | +15.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | +11.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.6 | +1.7 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +4.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.1 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -8.0 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -8.0 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 71 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:94,374,569-94,461,042 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14753; previously HIATL1, MFSD14B |
| Gene groups (HGNC) | Solute carrier family 71 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SR56](https://www.uniprot.org/uniprotkb/Q5SR56) (Solute carrier family 71 member 2):

> Probable membrane-bound transporter. May play a role in neuronal nutrient sensing and energy homeostasis.

**Summary**, from NCBI Gene [84641](https://www.ncbi.nlm.nih.gov/gene/84641):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23376) · Entrez [84641](https://www.ncbi.nlm.nih.gov/gene/84641) · UniProt [Q5SR56](https://www.uniprot.org/uniprotkb/Q5SR56) · Ensembl [ENSG00000148110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148110)

## Data

Gene col 7242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7242); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7242]; `tensor/DDL_lfc|DDL_z.npy` [7242]; `embed/gene_vectors.npy` [7242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7242 or target_col == 7242). Every well: [[MFSD14B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD14B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
