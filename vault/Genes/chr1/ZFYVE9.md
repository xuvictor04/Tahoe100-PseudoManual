---
symbol: "ZFYVE9"
type: "gene"
col: 8040
ensembl_id: "ENSG00000157077"
name: "zinc finger FYVE-type containing 9"
location: "1p32.3"
module: 18
arm: "+"
pooled_cpm: 78.99
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ZFYVE9

*zinc finger FYVE-type containing 9* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.53× (z +11.5, q 5e-28, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.567× (z -21.7, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC22A15]] (+0.63, fdr 1e-05), [[NSMAF]] (+0.63, fdr 1e-05), [[CHCHD4]] (+0.63, fdr 1e-05); moves opposite to [[AGRN]] (-0.63, fdr 1e-05), [[NFKB2]] (-0.61, fdr 7e-06), [[TBC1D10A]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +11.5 | 5e-28 | 34/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +9.5 | 6e-19 | 39/45 (RKO, A-427, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +9.3 | 3e-18 | 31/48 (RKO, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +7.0 | 4e-10 | 27/48 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +5.4 | 1e-05 | 24/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +4.8 | 1e-04 | 20/48 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 4e-04 | 23/49 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.17× | +4.2 | 0.002 | 17/48 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +4.2 | 0.002 | 17/48 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +4.1 | 0.002 | 19/48 (Hs 766T, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.16× | +4.0 | 0.004 | 17/48 (NCI-H2347, Hs 766T, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.8 | 0.006 | 3/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.025 | 13/48 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.029 | 19/48 (NCI-H2347, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.048 | 13/48 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.058 | 8/48 (HOP62, AsPC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.082 | 19/48 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.567×** | -21.7 | 0e+00 | 41/48 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.502×** | -18.6 | 0e+00 | 42/48 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.503×** | -18.6 | 0e+00 | 44/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.505×** | -17.1 | 0e+00 | 35/44 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.592×** | -14.2 | 1e-43 | 38/48 (NCI-H2030, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -13.7 | 9e-41 | 35/48 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.635×** | -12.3 | 9e-33 | 37/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.624×** | -12.3 | 1e-32 | 35/43 (A-427, HCT15, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.740×** | -7.8 | 3e-13 | 30/50 (C32, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.785×** | -6.5 | 4e-09 | 24/48 (A-172, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.787×** | -6.5 | 5e-09 | 26/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.789×** | -6.2 | 4e-08 | 26/48 (J82, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.807×** | -5.8 | 3e-07 | 28/47 (SW1417, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -5.8 | 3e-07 | 19/48 (SW480, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **0.809×** | -5.5 | 1e-06 | 24/47 (HepG2/C3A, RKO, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.750×** | -4.1 | 0.001 | 21/48 (RKO, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.911× | -3.5 | 0.011 | 9/48 (J82, NCI-H2030, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.894× | -3.0 | 0.060 | 4/48 (A549, HepG2/C3A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.897× | -2.9 | 0.079 | 8/47 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.899× | -2.9 | 0.096 | 7/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 104 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -26.3) |
| [[NCI-H460 (line)]] | wt | 68.6 | 0 | 13 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.220× (z -22.6) |
| [[RKO (line)]] | wt | 124 | 4 (2 ⚠) | 9 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.50× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.492× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 103 | 2 (1 ⚠) | 10 (6 ⚠) | [[Auranofin (drug)]] 5 µM 4.49× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -11.7) |
| [[C32 (line)]] | wt | 92.5 | 1 | 8 (6 ⚠) | [[Auranofin (drug)]] 5 µM 2.40× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -22.3) |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.434× (z -10.0) |
| [[SW48 (line)]] | wt | 129 | 1 | 8 (5 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.88× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.220× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.1) |
| [[A549 (line)]] | wt | 66.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 101 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.13× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -14.1) |
| [[A-172 (line)]] | wt | 59.3 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.25× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -21.4) |
| [[A-427 (line)]] | wt | 118 | 1 | 6 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.69× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.465× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 93.1 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.38× (z +17.3) | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -16.3) |
| [[PANC-1 (line)]] | alt | 90.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -23.8) |
| [[A498 (line)]] | wt | 47.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -22.0) |
| [[C-33 A (line)]] | alt | 174 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.68× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.335× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 81.2 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.188× (z -18.1) |
| [[HS-578T (line)]] | alt | 79.1 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.18× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -19.3) |
| [[Panc 03.27 (line)]] | alt | 84.4 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.527× (z -11.1) |
| [[SNU-1 (line)]] | wt | 117 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 82.4 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -17.5) |
| [[LoVo (line)]] | wt | 107 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -14.0) |
| [[LS 180 (line)]] | wt | 82.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.472× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 80.9 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -18.8) |
| [[SW1417 (line)]] | alt | 68.3 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~14% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.433× (z -10.5) |
| [[BT-474 (line)]] | alt | 37.6 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.60× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HCT15 (line)]] | alt | 103 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HepG2_C3A (line)]] | wt | 90.7 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.131× (z -18.7) ⚠ toxic; cell-cycle shift, explains ~14% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.358× (z -9.8) |
| [[KATO III (line)]] | alt | 59.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.348× (z -11.6) |
| [[SNU-423 (line)]] | alt | 70.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -26.4) |
| [[AN3 CA (line)]] | alt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HOP62 (line)]] | alt | 70.0 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.49× (z +17.1) | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 95.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.496× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 55.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -15.5) |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0815× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.5) |
| [[SW 900 (line)]] | alt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.4) |
| [[COLO 205 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A15]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[CHCHD4]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[KANK1]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TMEM161A]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PDS5A]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[VWA8]] | +0.59 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[USP46]] | +0.58 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.58 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MRPS5]] | +0.58 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ABCC5]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[KPNA3]] | +0.57 | +0.68 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGRN]] | -0.63 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[NFKB2]] | -0.61 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[TBC1D10A]] | -0.59 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TAGLN2]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CDKN2A]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[REL]] | -0.55 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[LMNA]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[BCL3]] | -0.54 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SLC41A2]] | -0.54 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CTNND1]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[BDKRB2]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[HLA-A]] | -0.51 | -0.60 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises ZFYVE9's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.24× lower at baseline in the lines without ADCY3 | 0.043 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[BDKRB2]] | B | BDKRB2 activity lowers ZFYVE9's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.47× higher at baseline in the lines without BDKRB2 | 0.053 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[MVB12B]] | B | MVB12B activity raises ZFYVE9's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without MVB12B | 0.063 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers ZFYVE9's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RILPL1]] | C | RILPL1's natural level strengthens ZFYVE9's drug response | RILPL1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.17; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[RUSC2]] | C | RUSC2 activity raises ZFYVE9's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without RUSC2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |
| [[PCGF6]] | C | PCGF6's natural level strengthens ZFYVE9's drug response | PCGF6's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.03; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (17.8, -4.4); signed map (-17.7, -50.4). **Vector** length 121, 36.5% of its response variance represented; |z| ≥ 3 in 1,405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +11.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +8.8 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.1 | +7.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.5 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.7 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +4.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -21.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -3.6 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger FYVE-type containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,142,089-52,348,671 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMADIP, SARA, PPP1R173; previously MADHIP |
| Gene groups (HGNC) | Zinc fingers FYVE-type |
| Reactome | 10 pathways, smallest: SMAD2/3 Phosphorylation Motif Mutants in Cancer; TGFBR1 KD Mutants in Cancer; Loss of Function of SMAD2/3 in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [O95405](https://www.uniprot.org/uniprotkb/O95405) (Zinc finger FYVE domain-containing protein 9):

> Early endosomal protein that functions to recruit SMAD2/SMAD3 to intracellular membranes and to the TGF-beta receptor. Plays a significant role in TGF-mediated signaling by regulating the subcellular location of SMAD2 and SMAD3 and modulating the transcriptional activity of the SMAD3/SMAD4 complex. Possibly associated with TGF-beta receptor internalization.

**Summary**, from NCBI Gene [9372](https://www.ncbi.nlm.nih.gov/gene/9372):

> This gene encodes a double zinc finger motif-containing protein that participates in the transforming growth factor-beta (TGFB) signalling pathway. The encoded protein interacts directly with SMAD2 and SMAD3, and recruits SMAD2 to the TGFB receptor. There are multiple pseudogenes for this gene on chromosomes 2, 15, and X. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:6775](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6775) · Entrez [9372](https://www.ncbi.nlm.nih.gov/gene/9372) · UniProt [O95405](https://www.uniprot.org/uniprotkb/O95405) · Ensembl [ENSG00000157077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157077)

## Data

Gene col 8040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8040); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8040]; `tensor/DDL_lfc|DDL_z.npy` [8040]; `embed/gene_vectors.npy` [8040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8040 or target_col == 8040). Every well: [[ZFYVE9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFYVE9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
