---
symbol: "ZER1"
type: "gene"
col: 8350
ensembl_id: "ENSG00000160445"
name: "zyg-11 related cell cycle regulator"
location: "9q34.11"
module: 145
arm: "+"
pooled_cpm: 38.02
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 31
n_dd_up_clean: 11
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# ZER1

*zyg-11 related cell cycle regulator* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.82× (z +15.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.305× (z -17.5, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.292× (z -9.5, q 2e-19, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL20]] (+0.73, fdr 1e-05), [[RETREG3]] (+0.70, fdr 1e-05), [[SPSB3]] (+0.70, fdr 4e-05); moves opposite to [[NCR3LG1]] (-0.61, fdr 4e-05), [[SNX5]] (-0.61, fdr 1e-05), [[SRSF1]] (-0.58, fdr 3e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.82×** | +15.4 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +13.6 | 1e-39 | 46/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.91×** | +12.6 | 3e-34 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.8 | 1e-12 | 33/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +5.0 | 5e-05 | 31/48 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +4.4 | 0.001 | 25/48 (RKO, SW1417, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.003 | 28/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.006 | 25/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.020 | 18/48 (SNU-423, SW 900, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.020 | 16/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.030 | 14/48 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.057 | 10/48 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.305×** | -17.5 | 0e+00 | 47/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.469×** | -10.8 | 1e-24 | 29/37 (Panc 03.27, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.474×** | -10.6 | 5e-24 | 39/47 (SNU-423, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -9.6 | 2e-19 | 37/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[EX229 (drug)]] 5 µM |  | **0.292×** | -9.5 | 2e-19 | 44/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.532×** | -9.3 | 1e-18 | 35/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.314×** | -9.0 | 2e-17 | 43/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.564×** | -8.5 | 2e-15 | 41/48 (SW480, C32, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.344×** | -8.3 | 9e-15 | 45/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.345×** | -8.2 | 1e-14 | 41/48 (NCI-H1792, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.378×** | -7.5 | 3e-12 | 38/47 (NCI-H460, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.606×** | -7.4 | 7e-12 | 41/47 (HCT15, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.593×** | -7.3 | 1e-11 | 40/48 (C-33 A, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -7.2 | 2e-11 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -6.7 | 7e-10 | 29/43 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.530×** | -6.7 | 7e-10 | 43/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.754×** | -5.9 | 1e-07 | 31/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -5.6 | 6e-07 | 29/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.701×** | -5.2 | 5e-06 | 27/47 (C32, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -4.8 | 5e-05 | 27/48 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.679×** | -4.1 | 0.001 | 21/48 (A498, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.6 | 3 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.65× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.117× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 43.8 | 0 | 7 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -13.7) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.115× (z -9.4) |
| [[PANC-1 (line)]] | alt | 21.9 | 2 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +10.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.302× (z -10.8) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -9.2) |
| [[SW480 (line)]] | alt | 37.6 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +13.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -13.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -10.7) |
| [[C32 (line)]] | wt | 41.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0863× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0703× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 49.2 | 1 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -8.6) |
| [[A549 (line)]] | wt | 31.3 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0876× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 64.4 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.51× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.410× (z -9.9) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 43.2 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +8.8) | [[Lonafarnib (drug)]] 5 µM 0.0723× (z -13.4) ⚠ toxic |
| [[J82 (line)]] | alt | 60.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -10.4) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.335× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 45.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.31× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -12.6) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 26.6 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0600× (z -17.9) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -9.2) |
| [[COLO 205 (line)]] | alt | 43.3 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 48.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 29.8 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -12.1) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 29.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.19× (z +10.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.187× (z -12.7) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 54.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -8.7) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 63.9 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.8) ⚠ cell-cycle shift, explains ~97% of this change |
| [[A498 (line)]] | wt | 34.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -10.4) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 48.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.85× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.283× (z -9.5) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 60.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -18.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 51.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0845× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 42.4 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.210× (z -11.0) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 30.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.317× (z -8.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.0) ⚠ cell-cycle shift, explains ~97% of this change |
| [[KATO III (line)]] | alt | 41.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.40× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.124× (z -14.6) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 27.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.01× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0950× (z -14.0) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.234× (z -10.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 28.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 68.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.359× (z -9.0) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.191× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.291× (z -10.0) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 69.6 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0779× (z -8.9) |
| [[SW1417 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.152× (z -15.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL20]] | +0.73 | +0.51 / +0.79 | both halves | 1e-05 |  |
| [[RETREG3]] | +0.70 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.70 | +0.40 / +0.77 | both halves | 4e-05 |  |
| [[HAGH]] | +0.69 | +0.48 / +0.76 | both halves | 2e-05 |  |
| [[CRAMP1]] | +0.68 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[USP20]] | +0.68 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ACOT8]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[ATXN3]] | +0.67 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[SYF2]] | +0.66 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[WIPI2]] | +0.64 | +0.33 / +0.71 | both halves | 1e-04 |  |
| [[ZNHIT3]] | +0.64 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[GATAD2B]] | +0.64 | +0.42 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCR3LG1]] | -0.61 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[SNX5]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.58 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[STK26]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PFKM]] | -0.56 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.55 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[CCT5]] | -0.55 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FKBP4]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.8, -43.3); signed map (-18.6, 12.2). **Vector** length 119, 38.9% of its response variance represented; |z| ≥ 3 in 1,320 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +13.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +12.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +15.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Resveratrol (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.7 | -17.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -10.3 | -5.9 |
|  | [[EX229 (drug)]] 5 µM |  | -8.5 | -9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.4 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.9 | -8.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.8 | -9.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.8 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | zyg-11 related cell cycle regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,729,786-128,772,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZYG, Hzyg; previously C9orf60, ZYG11BL |
| Gene groups (HGNC) | ZYG11 cell cycle regulator family; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7L7](https://www.uniprot.org/uniprotkb/Q7Z7L7) (Protein zer-1 homolog):

> Substrate recognition subunit in the E3 ubiquitin ligase complex ZER1-CUL2-Elongin BC. Targets substrates bearing N-terminal degrons for proteasomal degradation with the first four residues of substrates being the key recognition elements. Involved in the clearance of proteolytic fragments generated by caspase cleavage during apoptosis since N-terminal glycine degrons are strongly enriched at caspase cleavage sites. Also important in the quality control of protein N-myristoylation in which …

**Summary**, from NCBI Gene [10444](https://www.ncbi.nlm.nih.gov/gene/10444):

> This gene encodes a subunit of an E3 ubiquitin ligase complex that may be involved in meiosis. The encoded protein contains three leucine-rich repeat motifs. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:30960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30960) · Entrez [10444](https://www.ncbi.nlm.nih.gov/gene/10444) · UniProt [Q7Z7L7](https://www.uniprot.org/uniprotkb/Q7Z7L7) · Ensembl [ENSG00000160445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160445)

## Data

Gene col 8350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8350); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8350]; `tensor/DDL_lfc|DDL_z.npy` [8350]; `embed/gene_vectors.npy` [8350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8350 or target_col == 8350). Every well: [[ZER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
