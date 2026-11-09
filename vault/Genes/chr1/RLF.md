---
symbol: "RLF"
type: "gene"
col: 3864
ensembl_id: "ENSG00000117000"
name: "RLF zinc finger"
location: "1p34.2"
module: 79
arm: "+"
pooled_cpm: 275.86
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# RLF

*RLF zinc finger* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 12.3× (z +17.8, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.222× (z -19.7, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.764× (z -5.2, q 4e-05, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF292]] (+0.74, fdr 7e-06), [[ADM]] (+0.69, fdr 1e-05), [[DDIT4]] (+0.68, fdr 1e-05); moves opposite to [[ARMC6]] (-0.60, fdr 2e-05), [[LY6G5B]] (-0.58, fdr 3e-05), [[PSME3]] (-0.55, fdr 3e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **12.3×** | +17.8 | 0e+00 | 49/49 (SW480, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.12×** | +15.4 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +12.9 | 9e-36 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.88×** | +12.6 | 5e-34 | 47/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.17×** | +10.5 | 1e-23 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.71×** | +10.3 | 8e-23 | 40/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.99×** | +9.3 | 9e-19 | 41/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.71×** | +7.0 | 2e-10 | 41/48 (NCI-H1792, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +6.4 | 1e-08 | 35/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.55×** | +5.9 | 2e-07 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.26×** | +5.8 | 4e-07 | 44/48 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +5.1 | 1e-05 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 39/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.6 | 2e-04 | 28/38 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.023 | 33/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.071 | 33/48 (SW48, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.075 | 25/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +2.9 | 0.097 | 28/49 (HT-29, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.222×** | -19.7 | 0e+00 | 44/44 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.308×** | -16.0 | 0e+00 | 49/49 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.764×** | -5.2 | 4e-05 | 39/48 (A-172, AN3 CA, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.783×** | -4.7 | 3e-04 | 28/49 (A549, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.719×** | -4.5 | 8e-04 | 37/48 (CFPAC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.712×** | -4.4 | 8e-04 | 38/47 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.757×** | -3.8 | 0.012 | 38/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.759×** | -3.7 | 0.013 | 38/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.843× | -3.3 | 0.058 | 23/48 (AsPC-1, hTERT-HPNE, …) | top dose only | low cells (technical?) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.786×** | -3.3 | 0.058 | 30/48 (NCI-H2347, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.792×** | -3.2 | 0.077 | 32/48 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.801× | -3.0 | 0.11 | 33/48 (RKO, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.801× | -3.0 | 0.11 | 27/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.802× | -3.0 | 0.11 | 30/49 (AsPC-1, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 196 | 13 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.6× (z +29.9) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -9.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 232 | 11 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.51× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 283 | 10 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +17.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.45× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -17.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 226 | 9 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.1× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 232 | 9 (3 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.2× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -20.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 225 | 5 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.15× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.503× (z -10.2) |
| [[BT-474 (line)]] | alt | 227 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 198 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.50× (z +29.8) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -13.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 224 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.81× (z +25.7) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 255 | 8 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.08× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 20.8× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 281 | 6 (3 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.74× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -15.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 294 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -16.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 360 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 16.1× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -12.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 343 | 6 (3 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.8× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -21.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 223 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.10× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 240 | 6 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +22.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.1× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -23.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 199 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -17.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 199 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.92× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[COLO 205 (line)]] | alt | 223 | 6 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.62× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 367 | 6 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.1× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 329 | 5 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 16.9× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -15.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 200 | 3 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.09× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 294 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.83× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -16.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 405 | 2 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.92× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.410× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 267 | 3 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 10.5× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -18.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 292 | 4 (1 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 13.6× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -14.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 298 | 4 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -18.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 367 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.6× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 397 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -25.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 370 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.3× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -26.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 380 | 4 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -19.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 299 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 20.7× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -11.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 295 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.60× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 193 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.0× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -21.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 365 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 18.6× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -14.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 405 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.18× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -17.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 248 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -15.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 419 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.1× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 267 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.7× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 320 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.1× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -17.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 264 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -17.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 248 | 4 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.2× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 272 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -11.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 416 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.68× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -12.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 184 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 365 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 201 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +9.4) | — |
| [[NCI-H2122 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 368 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF292]] | +0.74 | +0.72 / +0.79 | both halves | 7e-06 | same gene group; STRING 413 |
| [[ADM]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[RYBP]] | +0.65 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[RBPJ]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[MXI1]] | +0.64 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[CTR9]] | +0.63 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[FAM13A]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | +0.61 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[ZNF654]] | +0.61 | +0.69 / +0.56 | both halves | 1e-05 | same gene group |
| [[PFKFB4]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC6]] | -0.60 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[LY6G5B]] | -0.58 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PSME3]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SAE1]] | -0.55 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[EIF4EBP2]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HCFC1]] | -0.53 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[GATAD2A]] | -0.53 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[TRNT1]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[KLC2]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[GNL3L]] | -0.51 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ABCF2]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RBM12]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, -13.6); signed map (-33.3, 24.5). **Vector** length 87.5, 41.2% of its response variance represented; |z| ≥ 3 in 1,342 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.51 to 16); *hypoxia* (control, mean cos +0.56 to 5); *glycolysis* (hallmark, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.9 | +0.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.8 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.5 | +10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.6 | +9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | +15.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | +4.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.1 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | RLF zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,161,387-40,240,921 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF292L, Zn-15L |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13129](https://www.uniprot.org/uniprotkb/Q13129) (Zinc finger protein Rlf):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [6018](https://www.ncbi.nlm.nih.gov/gene/6018):

> Predicted to enable DNA binding activity and DNA-binding transcription activator activity, RNA polymerase II-specific. Predicted to be involved in positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within negative regulation of heterochromatin formation. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10025) · Entrez [6018](https://www.ncbi.nlm.nih.gov/gene/6018) · UniProt [Q13129](https://www.uniprot.org/uniprotkb/Q13129) · Ensembl [ENSG00000117000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117000)

## Data

Gene col 3864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3864); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3864]; `tensor/DDL_lfc|DDL_z.npy` [3864]; `embed/gene_vectors.npy` [3864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3864 or target_col == 3864). Every well: [[RLF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RLF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
