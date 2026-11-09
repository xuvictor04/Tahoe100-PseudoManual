---
symbol: "RPS6KA2"
type: "gene"
col: 980
ensembl_id: "ENSG00000071242"
name: "ribosomal protein S6 kinase A2"
location: "6q27"
module: 97
arm: "+"
pooled_cpm: 68.14
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 29
n_dd_up_clean: 22
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# RPS6KA2

*ribosomal protein S6 kinase A2* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.34× (z +17.3, q 0e+00, up in 40 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (18 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.302× (z -17.2, q 0e+00, down in 39 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.444× (z -11.7, q 2e-29, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERGIC1]] (+0.65, fdr 1e-05), [[PYGB]] (+0.63, fdr 7e-06), [[TBC1D16]] (+0.61, fdr 4e-05); moves opposite to [[MED13]] (-0.52, fdr 1e-04), [[KMO]] (-0.52, fdr 1e-04), [[SRRM2-AS1]] (-0.51, fdr 2e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EDIL3-DT]] → it (grade B ⚠); 6 go from it, the strongest it → [[MTHFD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.34×** | +17.3 | 0e+00 | 40/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +13.0 | 3e-36 | 38/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +11.8 | 7e-30 | 37/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.38×** | +6.4 | 2e-08 | 31/42 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.8 | 8e-07 | 25/42 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.7 | 1e-06 | 27/42 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.45×** | +5.3 | 8e-06 | 24/42 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.44×** | +5.2 | 2e-05 | 26/42 (LS 180, C32, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +5.1 | 2e-05 | 25/42 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.41×** | +4.9 | 6e-05 | 23/42 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 8e-05 | 23/42 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +4.6 | 2e-04 | 25/43 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 2e-04 | 18/41 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.37×** | +4.5 | 3e-04 | 24/41 (NCI-H460, C32, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +4.3 | 8e-04 | 24/43 (AsPC-1, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.302×** | -17.2 | 0e+00 | 39/41 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.390×** | -13.6 | 2e-39 | 36/42 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.386×** | -13.2 | 2e-37 | 36/40 (HEC-1-A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.405×** | -12.5 | 8e-34 | 33/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.444×** | -11.7 | 2e-29 | 30/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.486×** | -10.4 | 3e-23 | 32/42 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -10.3 | 4e-23 | 35/42 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.510×** | -9.7 | 2e-20 | 35/42 (KATO III, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.548×** | -8.7 | 3e-16 | 31/42 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.670×** | -8.2 | 2e-14 | 23/42 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.376×** | -7.4 | 9e-12 | 29/43 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.622×** | -6.6 | 2e-09 | 27/40 (LoVo, SNU-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.634×** | -6.6 | 2e-09 | 34/42 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.625×** | -6.4 | 6e-09 | 30/42 (HS-578T, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.653×** | -6.1 | 3e-08 | 25/42 (HS-578T, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.523×** | -4.9 | 3e-05 | 24/42 (SW48, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.739×** | -4.4 | 3e-04 | 23/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.776×** | -3.4 | 0.015 | 18/41 (H4, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -3.4 | 0.017 | 18/42 (SW 1271, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.742×** | -3.1 | 0.039 | 13/43 (A498, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.865× | -3.0 | 0.052 | 16/42 (A-172, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.0 | 3 | 12 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 4.93× (z +14.7) | [[Digitoxin (drug)]] 5 µM 0.115× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.226× (z -13.8) |
| [[HOP62 (line)]] | alt | 28.0 | 9 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 6.62× (z +13.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 50.1 | 1 | 12 (10 ⚠) | [[Panobinostat (drug)]] 5 µM 3.12× (z +9.4) | [[Digitoxin (drug)]] 0.5 µM 0.145× (z -15.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.151× (z -15.6) |
| [[KATO III (line)]] | alt | 100 | 3 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 4.11× (z +11.8) | [[Digitoxin (drug)]] 5 µM 0.0510× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.256× (z -11.4) |
| [[SW480 (line)]] | alt | 52.0 | 3 | 8 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 4.74× (z +18.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -18.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.401× (z -10.9) |
| [[SNU-423 (line)]] | alt | 137 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.3) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -10.5) |
| [[A498 (line)]] | wt | 130 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.4) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.205× (z -12.4) |
| [[HS-578T (line)]] | alt | 147 | 2 | 6 (2 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.60× (z +8.5) | [[Ixazomib citrate (drug)]] 5 µM 0.172× (z -15.9) |
| [[A-172 (line)]] | wt | 348 | 0 | 7 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.238× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 117 | 1 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.90× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -14.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.219× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 41.2 | 2 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -11.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HepG2_C3A (line)]] | wt | 58.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -18.2) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.183× (z -10.6) |
| [[HT-29 (line)]] | alt | 40.8 | 3 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.54× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.184× (z -11.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 48.3 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -15.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.228× (z -12.7) |
| [[LS 180 (line)]] | wt | 144 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.134× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 74.9 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.10× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.254× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.284× (z -10.4) |
| [[Hs 766T (line)]] | wt | 87.3 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.173× (z -13.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 77.8 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -10.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.370× (z -9.2) |
| [[SHP-77 (line)]] | alt | 121 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SNU-1 (line)]] | wt | 40.4 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0741× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 45.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 74.3 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.27× (z +10.5) | [[Ixazomib citrate (drug)]] 5 µM 0.252× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 137 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -15.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SW1417 (line)]] | alt | 83.8 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.74× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.228× (z -13.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 99.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0828× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0303× (z -13.1) |
| [[H4 (line)]] | wt | 59.1 | 1 | 2 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.59× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.159× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.226× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.50× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 61.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.54× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -10.4) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 55.3 | 0 | 2 (1 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0797× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 52.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 61.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +25.3) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[COLO 205 (line)]] | alt | 53.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0649× (z -10.3) |
| [[C32 (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 34.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +9.6) | — |
| [[A-427 (line)]] | wt | 16.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC1]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PYGB]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TBC1D16]] | +0.61 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[EIF4EBP1]] | +0.58 | +0.45 / +0.41 | both halves | 4e-05 | STRING 400 |
| [[MT1X]] | +0.57 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[HERPUD1]] | +0.56 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[MT2A]] | +0.55 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ESYT2]] | +0.54 | +0.53 / +0.49 | both halves | 2e-05 |  |
| [[ASNS]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ERRFI1]] | +0.54 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[AKNA]] | +0.54 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[GLRX]] | +0.54 | +0.55 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13]] | -0.52 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[KMO]] | -0.52 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[SRRM2-AS1]] | -0.51 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[SLC25A21]] | -0.51 | -0.26 / -0.32 | both halves | 3e-04 | same gene group |
| [[APOBEC3F]] | -0.51 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[ZSCAN31]] | -0.51 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[MIER3]] | -0.50 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[ZNF346]] | -0.50 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[PLS3-AS1]] | -0.50 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[LINC02328]] | -0.50 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[CARD6]] | -0.49 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[ALOX12P2-1]] | -0.49 | -0.50 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDIL3-DT]] | B | EDIL3-DT activity raises RPS6KA2's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 1.58× lower at baseline in the lines without EDIL3-DT | 0.004 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[TBC1D8]] | B | TBC1D8 activity raises RPS6KA2's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.08× lower at baseline in the lines without TBC1D8 | 0.007 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[MLPH]] | B | MLPH activity raises RPS6KA2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without MLPH | 0.032 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[ABLIM3]] | B | ABLIM3 activity raises RPS6KA2's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 1.80× lower at baseline in the lines without ABLIM3 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTHFD2]] | B | RPS6KA2 activity lowers MTHFD2's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 1.09× higher at baseline in the lines without RPS6KA2 | 0.036 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[SSR3]] | B | RPS6KA2 activity lowers SSR3's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 1.58× higher at baseline in the lines without RPS6KA2 | 0.048 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[ESYT2]] | B | RPS6KA2 activity raises ESYT2's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without RPS6KA2 | 0.066 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[SNED1]] | B | RPS6KA2 activity raises SNED1's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without RPS6KA2 | 0.079 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[MLPH]] | B | RPS6KA2 activity raises MLPH's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without RPS6KA2 | 0.082 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[CBLB]] | B | RPS6KA2 activity raises CBLB's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without RPS6KA2 | 0.099 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.6, 10.8); signed map (13.0, 34.7). **Vector** length 107, 31.9% of its response variance represented; |z| ≥ 3 in 1,720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +13.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +17.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +11.8 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.2 | +6.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.6 | +2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.3 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +4.3 | +2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.0 | +1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.0 | +4.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.9 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.8 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | +0.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.5 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:166,409,364-166,906,451 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RSK3, HU-2 |
| Gene groups (HGNC) | MAPK activated protein kinases; MicroRNA protein coding host genes; Ribosomal protein S6 kinase family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 47 pathways, smallest: CREB phosphorylation; RSK activation; Gastrin-CREB signalling pathway via PKC and MAPK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15349](https://www.uniprot.org/uniprotkb/Q15349) (Ribosomal protein S6 kinase alpha-2):

> Serine/threonine-protein kinase that acts downstream of ERK (MAPK1/ERK2 and MAPK3/ERK1) signaling and mediates mitogenic and stress-induced activation of transcription factors, regulates translation, and mediates cellular proliferation, survival, and differentiation. May function as tumor suppressor in epithelial ovarian cancer cells.

**Summary**, from NCBI Gene [6196](https://www.ncbi.nlm.nih.gov/gene/6196):

> This gene encodes a member of the RSK (ribosomal S6 kinase) family of serine/threonine kinases. This kinase contains two non-identical kinase catalytic domains and phosphorylates various substrates, including members of the mitogen-activated kinase (MAPK) signalling pathway. The activity of this protein has been implicated in controlling cell growth and differentiation. Alternative splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:10431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10431) · Entrez [6196](https://www.ncbi.nlm.nih.gov/gene/6196) · UniProt [Q15349](https://www.uniprot.org/uniprotkb/Q15349) · Ensembl [ENSG00000071242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071242)

## Data

Gene col 980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 980); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 980]; `tensor/DDL_lfc|DDL_z.npy` [980]; `embed/gene_vectors.npy` [980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 980 or target_col == 980). Every well: [[RPS6KA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
