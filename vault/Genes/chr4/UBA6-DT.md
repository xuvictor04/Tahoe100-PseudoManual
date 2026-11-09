---
symbol: "UBA6-DT"
type: "gene"
col: 14514
ensembl_id: "ENSG00000248049"
name: "UBA6 divergent transcript"
location: "4q13.2"
module: 26
arm: "+"
pooled_cpm: 84.12
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 37
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# UBA6-DT

*UBA6 divergent transcript* — 4q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.99× (z +8.5, q 2e-14, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (23 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.342× (z -13.2, q 7e-37, down in 42 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.487× (z -8.8, q 8e-17, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIX1-AS1]] (+0.74, fdr 7e-06), [[LINC01340]] (+0.72, fdr 8e-06), [[CFAP418-AS1]] (+0.71, fdr 7e-06); moves opposite to [[DNMT3B]] (-0.60, fdr 1e-04), [[CEP131]] (-0.58, fdr 7e-05), [[SLC23A2]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DIRC3]] → it (grade B ⚠); 5 go from it, the strongest it → [[AK9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +8.5 | 2e-14 | 31/45 (A-172, SHP-77, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.4 | 3e-08 | 33/45 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.36×** | +5.4 | 2e-05 | 28/45 (A-427, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.1 | 4e-05 | 26/46 (Panc 03.27, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.001 | 26/46 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.002 | 24/45 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.004 | 27/44 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.019 | 24/45 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.11 | 15/46 (C-33 A, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.28× | +3.1 | 0.11 | 18/45 (KATO III, A-427, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.61× | +3.1 | 0.11 | 16/46 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | 1.61× | +3.1 | 0.11 | 20/46 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 24 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.342×** | -13.2 | 7e-37 | 42/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.347×** | -13.0 | 3e-36 | 43/45 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.371×** | -11.7 | 2e-29 | 40/44 (COLO 205, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.425×** | -10.5 | 1e-23 | 41/45 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.454×** | -9.7 | 3e-20 | 42/45 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.486×** | -8.9 | 8e-17 | 41/45 (COLO 205, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.487×** | -8.8 | 8e-17 | 38/45 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.488×** | -8.5 | 2e-15 | 37/44 (COLO 205, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.544×** | -7.5 | 4e-12 | 38/45 (COLO 205, HCT15, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.583×** | -6.6 | 2e-09 | 31/45 (HCT15, LOX-IMVI, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.613×** | -5.8 | 4e-07 | 30/45 (NCI-H1573, C32, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.639×** | -5.3 | 6e-06 | 26/40 (Hs 766T, H4, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.656×** | -5.2 | 1e-05 | 31/45 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -5.0 | 3e-05 | 33/46 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.464×** | -4.9 | 3e-05 | 30/42 (COLO 205, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -4.7 | 8e-05 | 26/45 (HT-29, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.699×** | -4.1 | 1e-03 | 28/45 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.731×** | -3.9 | 0.003 | 26/45 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.588×** | -3.4 | 0.015 | 25/45 (HCT15, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.714×** | -3.3 | 0.018 | 22/45 (C32, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.600×** | -3.3 | 0.021 | 23/43 (CFPAC-1, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.728×** | -3.1 | 0.031 | 19/44 (CFPAC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.614×** | -3.1 | 0.032 | 16/46 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.035 | 16/44 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.720×** | -2.9 | 0.064 | 20/46 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.851× | -2.8 | 0.077 | 19/46 (C32, CFPAC-1, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.791×** | -2.8 | 0.083 | 18/45 (CFPAC-1, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 453 | 0 | 17 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -19.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.147× (z -14.8) |
| [[SW480 (line)]] | alt | 78.6 | 0 | 17 (14 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -17.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.250× (z -13.6) |
| [[COLO 205 (line)]] | alt | 309 | 0 | 13 (12 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0911× (z -18.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.344× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.191× (z -10.4) |
| [[HT-29 (line)]] | alt | 90.9 | 0 | 11 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -15.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.180× (z -13.5) |
| [[HCT15 (line)]] | alt | 149 | 0 | 10 (8 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.160× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 218 | 0 | 10 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -16.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 239 | 0 | 9 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 47.4 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.301× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 295 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -10.7) |
| [[LS 180 (line)]] | wt | 52.1 | 1 (1 ⚠) | 5 (4 ⚠) | [[Selinexor (drug)]] 5 µM 2.35× (z +8.5) ⚠ cell-cycle shift, explains ~80% of this change | [[Digitoxin (drug)]] 5 µM 0.123× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.254× (z -9.7) |
| [[Hs 766T (line)]] | wt | 114 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0871× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[HS-578T (line)]] | alt | 105 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 69.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0863× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[SNU-1 (line)]] | wt | 103 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.142× (z -12.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 63.6 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -10.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 96.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 119 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.292× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 49.7 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.33× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -13.7) ⚠ toxic |
| [[HOP62 (line)]] | alt | 86.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 52.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -9.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 34.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -9.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 60.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 45.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.18× (z +11.8) | — |
| [[A-427 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.46× (z +9.5) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[A498 (line)]] | wt | 59.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.82× (z +8.7) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[C-33 A (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0878× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[NCI-H2030 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.43× (z +8.8) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +13.5) | — |
| [[SHP-77 (line)]] | alt | 71.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 1271 (line)]] | alt | 83.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0667× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIX1-AS1]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[LINC01340]] | +0.72 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[CFAP418-AS1]] | +0.71 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[MGAM]] | +0.70 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LINC01762]] | +0.68 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LINC01135]] | +0.68 | +0.64 / +0.53 | both halves | 1e-05 | same gene group |
| [[FSIP2-AS1]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ST8SIA5]] | +0.67 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[AEBP2]] | +0.66 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[HAS2-AS1]] | +0.66 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.66 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PELO-AS1]] | +0.66 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT3B]] | -0.60 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[CEP131]] | -0.58 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[SLC23A2]] | -0.57 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[TSPAN33]] | -0.56 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[COPG2]] | -0.55 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3]] | B | DIRC3 activity raises UBA6-DT's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without DIRC3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[LINC02112]] | B | LINC02112 activity raises UBA6-DT's level | lines that do not express LINC02112 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without LINC02112 | 0.032 | ⚠ within organs, on part of the lines; also absent: DNAH6, IQCM, LINC02932; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises UBA6-DT's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.41× lower at baseline in the lines without FSIP2-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[ENOX1]] | B | ENOX1 activity raises UBA6-DT's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without ENOX1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[F11-AS1]] | B | F11-AS1 activity raises UBA6-DT's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.53× lower at baseline in the lines without F11-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent |
| [[IQCJ]] | B | IQCJ activity raises UBA6-DT's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 2.71× lower at baseline in the lines without IQCJ | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises UBA6-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 2.03× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AK9]] | C | UBA6-DT activity raises AK9's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without UBA6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent; its own permutation p |
| [[C12orf60]] | C | UBA6-DT activity raises C12orf60's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without UBA6-DT | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent |
| [[CLEC2D]] | C | UBA6-DT activity raises CLEC2D's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 3.71× lower at baseline in the lines without UBA6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ZRANB2-DT]] | C | UBA6-DT activity raises ZRANB2-DT's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without UBA6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent; its own permutation p |
| [[ITGB3BP]] | C | UBA6-DT activity raises ITGB3BP's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without UBA6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.9, 15.6); signed map (24.9, -0.0). **Vector** length 106, 34.8% of its response variance represented; |z| ≥ 3 in 1,327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +14.2 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.6 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.8 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.4 | -8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.5 | -7.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.0 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | UBA6 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q13.2 — chr4:67,701,209-68,080,952 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LOC550112; previously UBA6-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [550112](https://www.ncbi.nlm.nih.gov/gene/550112):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49083) · Entrez [550112](https://www.ncbi.nlm.nih.gov/gene/550112) · Ensembl [ENSG00000248049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248049)

## Data

Gene col 14514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14514); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14514]; `tensor/DDL_lfc|DDL_z.npy` [14514]; `embed/gene_vectors.npy` [14514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14514 or target_col == 14514). Every well: [[UBA6-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBA6-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
