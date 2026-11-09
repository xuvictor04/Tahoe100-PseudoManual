---
symbol: "IFNGR2"
type: "gene"
col: 8218
ensembl_id: "ENSG00000159128"
name: "interferon gamma receptor 2"
location: "21q22.11"
module: 14
arm: "+"
pooled_cpm: 70.41
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IFNGR2

*interferon gamma receptor 2* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +27.8, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.233× (z -30.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD83]] (+0.65, fdr 7e-06), [[GATM]] (+0.64, fdr 1e-05), [[PLAU]] (+0.63, fdr 1e-05); moves opposite to [[RNF216]] (-0.61, fdr 2e-05), [[KDM4A]] (-0.54, fdr 4e-05), [[RNF216P1]] (-0.51, fdr 9e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMAD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +27.8 | 0e+00 | 39/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.63×** | +16.6 | 0e+00 | 47/49 (LoVo, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +15.4 | 0e+00 | 37/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +11.1 | 1e-26 | 35/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +8.5 | 2e-15 | 32/45 (HOP62, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +8.2 | 2e-14 | 30/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +7.6 | 3e-12 | 30/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +7.3 | 1e-11 | 27/37 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +6.1 | 6e-08 | 24/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +6.0 | 1e-07 | 26/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +6.0 | 1e-07 | 1/50 (KATO III) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +4.9 | 6e-05 | 22/48 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.23×** | +4.3 | 7e-04 | 19/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.17× | +3.2 | 0.051 | 12/48 (A498, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.17× | +3.2 | 0.056 | 15/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +3.1 | 0.062 | 18/49 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.233×** | -30.1 | 0e+00 | 48/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.251×** | -28.6 | 0e+00 | 48/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.330×** | -22.9 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.473×** | -15.5 | 0e+00 | 45/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.574×** | -11.5 | 2e-28 | 39/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.590×** | -10.9 | 8e-26 | 41/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.437×** | -9.0 | 3e-17 | 40/49 (SK-MEL-2, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.705×** | -6.8 | 6e-10 | 32/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.725×** | -6.7 | 2e-09 | 30/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.741×** | -6.2 | 3e-08 | 31/49 (SW480, NCI-H23, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.761×** | -5.7 | 8e-07 | 30/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.762×** | -5.6 | 9e-07 | 27/48 (hTERT-HPNE, MIA PaCa-2, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -5.6 | 1e-06 | 26/48 (SK-MEL-2, MIA PaCa-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.624×** | -5.1 | 1e-05 | 21/45 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.786×** | -5.0 | 2e-05 | 23/50 (SK-MEL-2, NCI-H596, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.633×** | -4.9 | 2e-05 | 26/48 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -4.9 | 3e-05 | 21/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.860× | -4.3 | 6e-04 | 19/49 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.842× | -4.2 | 7e-04 | 21/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 78.1 | 0 | 15 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -20.1) |
| [[HOP62 (line)]] | alt | 71.0 | 9 (5 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +25.4) | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 37.9 | 10 (7 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +23.8) | [[Panobinostat (drug)]] 5 µM 0.288× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 166 | 4 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +26.7) | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -23.9) |
| [[NCI-H2347 (line)]] | alt | 118 | 5 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -17.8) |
| [[PANC-1 (line)]] | alt | 49.7 | 6 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +27.1) | [[Panobinostat (drug)]] 5 µM 0.278× (z -14.4) |
| [[A-172 (line)]] | wt | 62.5 | 5 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +22.2) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 117 | 4 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.10× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -18.6) |
| [[HS-578T (line)]] | alt | 90.4 | 6 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.191× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 104 | 2 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.0992× (z -24.0) |
| [[NCI-H23 (line)]] | alt | 84.5 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.1000× (z -20.4) |
| [[SNU-423 (line)]] | alt | 44.9 | 5 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +26.4) | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -10.0) |
| [[A-427 (line)]] | wt | 67.7 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.238× (z -15.5) |
| [[HepG2_C3A (line)]] | wt | 80.4 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -13.6) |
| [[SW 900 (line)]] | alt | 82.2 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -11.5) |
| [[SW480 (line)]] | alt | 52.0 | 1 | 5 | [[TAK-901 (drug)]] 5 µM 3.35× (z +8.5) | [[Belinostat (drug)]] 5 µM 0.150× (z -25.6) |
| [[A498 (line)]] | wt | 84.1 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -8.7) |
| [[A549 (line)]] | wt | 80.4 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -18.9) |
| [[CFPAC-1 (line)]] | alt | 95.5 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +25.0) | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 63.3 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -10.7) |
| [[J82 (line)]] | alt | 36.0 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +18.4) | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -9.9) |
| [[KATO III (line)]] | alt | 66.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -21.2) |
| [[LoVo (line)]] | wt | 55.1 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 13.8× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.173× (z -18.5) |
| [[NCI-H1792 (line)]] | alt | 76.7 | 2 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 3.42× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.248× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 78.6 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -17.3) |
| [[SW1417 (line)]] | alt | 45.0 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.338× (z -10.5) |
| [[C32 (line)]] | wt | 70.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -15.4) |
| [[COLO 205 (line)]] | alt | 37.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -9.4) |
| [[Hs 766T (line)]] | wt | 76.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.179× (z -14.3) |
| [[LS 180 (line)]] | wt | 58.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 63.5 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.213× (z -11.7) |
| [[BT-474 (line)]] | alt | 66.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -11.6) |
| [[HT-29 (line)]] | alt | 48.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.195× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 46.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 167 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -18.8) |
| [[RKO (line)]] | wt | 52.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -14.3) |
| [[SW48 (line)]] | wt | 51.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -13.1) |
| [[C-33 A (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.08× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 53.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +9.1) | — |
| [[H4 (line)]] | wt | 61.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.5) | — |
| [[SNU-1 (line)]] | wt | 45.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -8.8) |
| [[SW 1088 (line)]] | alt | 84.5 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0957× (z -8.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AN3 CA (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD83]] | +0.65 | +0.73 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GATM]] | +0.64 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PLAU]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BCL3]] | +0.62 | +0.59 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[NFKBID]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[NFKB1]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[STAT5A]] | +0.60 | +0.46 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ICAM1]] | +0.59 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[BAHCC1]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TNFAIP2]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[LTB]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[KBTBD2]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF216]] | -0.61 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[KDM4A]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[RNF216P1]] | -0.51 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[HERC2P2]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[EPS15L1]] | -0.50 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[PWWP3A]] | -0.50 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[ZNF692]] | -0.50 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[TMEM161A]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.49 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[HERC2P3]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NEIL2]] | -0.49 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[EP400]] | -0.49 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD3]] | B | SMAD3 activity raises IFNGR2's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without SMAD3 | 0.090 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.4, 2.7); signed map (43.0, 7.9). **Vector** length 122, 39.7% of its response variance represented; |z| ≥ 3 in 1,572 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +13.0 | +27.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.4 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.2 | +0.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +16.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | -1.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.8 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -8.2 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -7.6 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -11.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.4 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.3 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.3 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | interferon gamma receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,403,413-33,479,348 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AF-1; previously IFNGT1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Interferon receptors |
| Hallmark sets | TGF_BETA_SIGNALING, IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 8 pathways, smallest: IFNG signaling activates MAPKs; Regulation of IFNG signaling; Interferon gamma signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P38484](https://www.uniprot.org/uniprotkb/P38484) (Interferon gamma receptor 2):

> Associates with IFNGR1 to form a receptor for the cytokine interferon gamma (IFNG). Ligand binding stimulates activation of the JAK/STAT signaling pathway. Required for signal transduction in contrast to other receptor subunit responsible for ligand binding.

**Summary**, from NCBI Gene [3460](https://www.ncbi.nlm.nih.gov/gene/3460):

> This gene (IFNGR2) encodes the non-ligand-binding beta chain of the gamma interferon receptor. Human interferon-gamma receptor is a heterodimer of IFNGR1 and IFNGR2. Defects in IFNGR2 are a cause of mendelian susceptibility to mycobacterial disease (MSMD), also known as familial disseminated atypical mycobacterial infection. MSMD is a genetically heterogeneous disease with autosomal recessive, autosomal dominant or X-linked inheritance. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5440) · Entrez [3460](https://www.ncbi.nlm.nih.gov/gene/3460) · UniProt [P38484](https://www.uniprot.org/uniprotkb/P38484) · Ensembl [ENSG00000159128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159128)

## Data

Gene col 8218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8218); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8218]; `tensor/DDL_lfc|DDL_z.npy` [8218]; `embed/gene_vectors.npy` [8218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8218 or target_col == 8218). Every well: [[IFNGR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFNGR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
