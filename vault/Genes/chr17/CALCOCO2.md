---
symbol: "CALCOCO2"
type: "gene"
col: 5862
ensembl_id: "ENSG00000136436"
name: "calcium binding and coiled-coil domain 2"
location: "17q21.32"
module: 30
arm: "+"
pooled_cpm: 104.62
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CALCOCO2

*calcium binding and coiled-coil domain 2* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.86× (z +14.1, q 3e-42, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.598× (z -17.4, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5R1]] (+0.63, fdr 3e-05), [[PLD3]] (+0.63, fdr 3e-05), [[YIPF1]] (+0.63, fdr 3e-05); moves opposite to [[SATB2]] (-0.59, fdr 1e-05), [[PPP1R1C]] (-0.59, fdr 3e-05), [[FJX1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRKG1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +14.1 | 3e-42 | 47/48 (MIA PaCa-2, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +12.3 | 3e-32 | 40/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +12.2 | 5e-32 | 43/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +12.2 | 7e-32 | 44/48 (A498, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +9.1 | 2e-17 | 40/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +8.1 | 6e-14 | 31/49 (PANC-1, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +7.5 | 7e-12 | 28/44 (PANC-1, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +7.4 | 1e-11 | 30/48 (SNU-1, BT-474, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +6.9 | 2e-10 | 30/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +6.5 | 5e-09 | 35/45 (NCI-H2030, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +4.2 | 0.001 | 20/48 (BT-474, NCI-H2030, …) | two highest doses |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.002 | 15/48 (HS-578T, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.017 | 14/48 (NCI-H23, BT-474, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.023 | 20/48 (NCI-H661, SHP-77, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.026 | 17/49 (MIA PaCa-2, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.15× | +3.4 | 0.026 | 18/48 (A498, LoVo, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.050 | 16/48 (HEC-1-A, SNU-1, …) | rises with dose | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.050 | 12/48 (SK-MEL-2, BT-474, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.097 | 13/48 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Oxaliplatin (drug)]] 0.05 µM |  | 1.13× | +2.9 | 0.097 | 2/48 (Hs 766T, SK-MEL-2) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5862.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -17.4 | 0e+00 | 40/48 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -15.3 | 0e+00 | 44/49 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -13.4 | 8e-39 | 37/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -8.0 | 1e-13 | 35/49 (CFPAC-1, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.767×** | -6.3 | 3e-08 | 29/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.772×** | -6.2 | 5e-08 | 34/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.764×** | -6.2 | 5e-08 | 27/47 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.768×** | -6.1 | 9e-08 | 26/48 (A-172, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.773×** | -5.9 | 2e-07 | 28/48 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -5.4 | 4e-06 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -5.3 | 5e-06 | 23/48 (A-427, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.670×** | -5.0 | 3e-05 | 29/48 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.804×** | -4.9 | 4e-05 | 25/47 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.699×** | -4.5 | 3e-04 | 21/38 (HS-578T, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.831×** | -4.4 | 4e-04 | 24/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.831×** | -4.1 | 0.002 | 24/47 (A549, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.783×** | -3.1 | 0.063 | 13/48 (RPMI-7951, A549, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.874× | -3.0 | 0.068 | 11/48 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 168 | 4 | 4 | [[Bortezomib (drug)]] 0.05 µM 1.96× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 69.7 | 6 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 2.21× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -11.7) |
| [[PANC-1 (line)]] | alt | 175 | 6 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.84× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.537× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 146 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -20.0) |
| [[HOP62 (line)]] | alt | 91.2 | 3 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.36× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 88.2 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.17× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -13.3) |
| [[SW480 (line)]] | alt | 78.1 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -10.3) |
| [[A549 (line)]] | wt | 141 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.00× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -15.4) |
| [[COLO 205 (line)]] | alt | 110 | 2 | 2 | [[Bortezomib (drug)]] 0.05 µM 2.54× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.6) |
| [[H4 (line)]] | wt | 141 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 90.4 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.20× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.4) |
| [[RKO (line)]] | wt | 67.8 | 3 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.46× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -11.1) |
| [[LS 180 (line)]] | wt | 98.1 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.66× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 96.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -15.9) |
| [[SW 900 (line)]] | alt | 83.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -10.2) |
| [[A-172 (line)]] | wt | 136 | 1 | 1 | [[Bortezomib (drug)]] 0.05 µM 1.85× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -10.6) |
| [[A-427 (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.601× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 104 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -9.6) |
| [[BT-474 (line)]] | alt | 208 | 1 (1 ⚠) | 1 | [[Artesunate (drug)]] 5 µM 1.62× (z +8.8) ⚠ cell-cycle shift, explains ~12% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -9.7) |
| [[KATO III (line)]] | alt | 174 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -12.1) |
| [[LoVo (line)]] | wt | 95.8 | 1 | 1 | [[Bortezomib (drug)]] 0.05 µM 2.13× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -16.9) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.76× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 68.5 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.41× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 76.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 70.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.624× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 92.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 133 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.09× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -20.4) |
| [[SNU-1 (line)]] | wt | 80.0 | 2 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.18× (z +9.0) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.11× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 135 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -18.1) |
| [[SW1417 (line)]] | alt | 84.0 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.21× (z +10.9) | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.9) |
| [[HCT15 (line)]] | alt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 96.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.52× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -14.2) |
| [[HT-29 (line)]] | alt | 73.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 51.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -8.5) |
| [[SW 1088 (line)]] | alt | 125 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0778× (z -9.6) |
| [[SW48 (line)]] | wt | 76.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.69× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5R1]] | +0.63 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[PLD3]] | +0.63 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[YIPF1]] | +0.63 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[SEL1L]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SNX3]] | +0.61 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ERP44]] | +0.60 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[RTN3]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SARAF]] | +0.60 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[ALDH2]] | +0.60 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[OSBPL9]] | +0.59 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[ORC3]] | +0.59 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ASAP3]] | +0.58 | +0.47 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SATB2]] | -0.59 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PPP1R1C]] | -0.59 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[FJX1]] | -0.58 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[PIGW]] | -0.58 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CDK6-AS1]] | -0.57 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ZNF337-AS1]] | -0.57 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[HIVEP1]] | -0.57 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CYREN]] | -0.57 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[CTBP1-DT]] | -0.55 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[INAFM2]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SPRED1]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[NEK8]] | -0.54 | -0.50 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG1-AS1]] | B | PRKG1-AS1 activity raises CALCOCO2's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 1.15× lower at baseline in the lines without PRKG1-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC |
| [[HDAC6]] | B | HDAC6 activity lowers CALCOCO2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers CALCOCO2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.2, -3.1); signed map (-35.4, -1.4). **Vector** length 146, 46.8% of its response variance represented; |z| ≥ 3 in 1,264 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +13.2 | +14.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +12.6 | +12.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.2 | +12.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.6 | +12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.8 | +9.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.0 | +3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.4 | +2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.2 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.4 | -15.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.7 | -17.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.4 | -5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.4 | -6.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -5.0 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.7 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium binding and coiled-coil domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,831,018-48,866,522 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17318, NDP52 |
| Gene groups (HGNC) | Zinc fingers UBZ1 CCHH-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13137](https://www.uniprot.org/uniprotkb/Q13137) (Calcium-binding and coiled-coil domain-containing protein 2):

> Xenophagy-specific receptor required for autophagy-mediated intracellular bacteria degradation. Acts as an effector protein of galectin-sensed membrane damage that restricts the proliferation of infecting pathogens such as Salmonella typhimurium upon entry into the cytosol by targeting LGALS8-associated bacteria for autophagy. Initially orchestrates bacteria targeting to autophagosomes and subsequently ensures pathogen degradation by regulating pathogen-containing autophagosome maturation. …

**Summary**, from NCBI Gene [10241](https://www.ncbi.nlm.nih.gov/gene/10241):

> This gene encodes a coiled-coil domain-containing protein. The encoded protein functions as a receptor for ubiquitin-coated bacteria and plays an important role in innate immunity by mediating macroautophagy. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:29912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29912) · Entrez [10241](https://www.ncbi.nlm.nih.gov/gene/10241) · UniProt [Q13137](https://www.uniprot.org/uniprotkb/Q13137) · Ensembl [ENSG00000136436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136436)

## Data

Gene col 5862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5862); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5862]; `tensor/DDL_lfc|DDL_z.npy` [5862]; `embed/gene_vectors.npy` [5862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5862 or target_col == 5862). Every well: [[CALCOCO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALCOCO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
