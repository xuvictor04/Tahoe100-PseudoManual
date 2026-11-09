---
symbol: "PARP1"
type: "gene"
col: 6806
ensembl_id: "ENSG00000143799"
name: "poly(ADP-ribose) polymerase 1"
location: "1q42.12"
module: 6
arm: "+"
pooled_cpm: 63.55
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PARP1

*poly(ADP-ribose) polymerase 1* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.80× (z +19.3, q 0e+00, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +4.6, q 2e-04, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.524× (z -11.3, q 1e-26, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPD3]] (+0.73, fdr 7e-06), [[PRKDC]] (+0.72, fdr 7e-06), [[SKP2]] (+0.72, fdr 9e-06); moves opposite to [[ZNF425]] (-0.69, fdr 3e-05), [[ATE1OSP]] (-0.69, fdr 3e-05), [[KRBOX5]] (-0.67, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NUP210]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **4.80×** | +19.3 | 0e+00 | 46/46 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.40×** | +17.5 | 0e+00 | 44/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.34×** | +13.7 | 2e-40 | 44/45 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.24×** | +9.9 | 7e-21 | 43/48 (HS-578T, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.22×** | +9.8 | 1e-20 | 44/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **2.05×** | +8.8 | 9e-17 | 41/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.70×** | +6.5 | 5e-09 | 35/48 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.56×** | +5.5 | 3e-06 | 41/48 (SW 900, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.6 | 2e-04 | 33/48 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.31×** | +4.6 | 2e-04 | 35/48 (BT-474, NCI-H23, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | **1.47×** | +4.5 | 3e-04 | 29/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.5 | 4e-04 | 2/48 (KATO III, NCI-H1792) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.41×** | +4.2 | 0.001 | 29/46 (HCT15, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.39×** | +3.9 | 0.004 | 26/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +3.8 | 0.005 | 25/48 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.063 | 18/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.524×** | -11.3 | 1e-26 | 34/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.514×** | -8.2 | 6e-14 | 33/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -7.8 | 9e-13 | 34/48 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -5.5 | 5e-06 | 30/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.818×** | -3.5 | 0.048 | 23/48 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.583×** | -3.5 | 0.048 | 24/48 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.773× | -3.2 | 0.12 | 21/48 (A-427, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.777× | -3.1 | 0.13 | 21/47 (KATO III, SW480, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.772× | -3.1 | 0.13 | 20/48 (CFPAC-1, RPMI-7951, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.781× | -3.1 | 0.13 | 20/48 (A498, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 71.8 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 6.27× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.2) |
| [[A-427 (line)]] | wt | 101 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Harringtonine (drug)]] 5 µM 0.254× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 66.2 | 5 (5 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.19× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -12.5) |
| [[HS-578T (line)]] | alt | 30.8 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 64.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.229× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 20.2 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.91× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HOP62 (line)]] | alt | 26.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.95× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[PANC-1 (line)]] | alt | 86.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.8) |
| [[A498 (line)]] | wt | 93.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Harringtonine (drug)]] 0.5 µM 0.372× (z -10.6) |
| [[C32 (line)]] | wt | 42.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.29× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Harringtonine (drug)]] 0.5 µM 0.245× (z -9.1) |
| [[J82 (line)]] | alt | 72.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.0) |
| [[KATO III (line)]] | alt | 58.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.67× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 40.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 27.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.0× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW 900 (line)]] | alt | 48.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 92.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 27.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.92× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HCT15 (line)]] | alt | 92.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.81× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.9) |
| [[Hs 766T (line)]] | wt | 37.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.25× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.6) |
| [[HT-29 (line)]] | alt | 31.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.01× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.31× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 47.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 79.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 89.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 49.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 38.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.42× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 72.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Harringtonine (drug)]] 5 µM 0.274× (z -8.7) |
| [[SNU-423 (line)]] | alt | 24.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.5× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW1417 (line)]] | alt | 51.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.8) |
| [[A549 (line)]] | wt | 52.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[C-33 A (line)]] | alt | 115 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -8.5) |
| [[H4 (line)]] | wt | 49.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.44× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HEC-1-A (line)]] | alt | 83.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.0) |
| [[LoVo (line)]] | wt | 50.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 35.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.74× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 85.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SNU-1 (line)]] | wt | 69.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.270× (z -9.4) |
| [[AN3 CA (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.4) |
| [[SHP-77 (line)]] | alt | 131 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW 1271 (line)]] | alt | 50.6 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0794× (z -8.5) |
| [[SW48 (line)]] | wt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.7) |
| [[BT-474 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPD3]] | +0.73 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.72 | +0.76 / +0.66 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 993 |
| [[SKP2]] | +0.72 | +0.57 / +0.70 | both halves | 9e-06 | STRING 457 |
| [[PODXL2]] | +0.71 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LYPD6]] | +0.71 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[RBBP7]] | +0.71 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[CASP2]] | +0.69 | +0.59 / +0.55 | both halves | 1e-05 | STRING 597 |
| [[TMEM109]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 | pathway: Signaling by TGF-beta Receptor Complex |
| [[CDCA7L]] | +0.68 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[LRRC20]] | +0.67 | +0.53 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF425]] | -0.69 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ATE1OSP]] | -0.69 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[KRBOX5]] | -0.67 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[THAP2]] | -0.67 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CCDC59]] | -0.66 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CFAP53]] | -0.66 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[LINC01004]] | -0.65 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[CDKL3]] | -0.64 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[EIF3J-DT]] | -0.64 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MED18]] | -0.64 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[PIGP]] | -0.63 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[TERF2IP]] | -0.63 | -0.59 / -0.50 | both halves | 1e-05 | pathway: Base Excision Repair; STRING 570 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity raises PARP1's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without NUP210 | 0.017 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[CELSR2]] | B | CELSR2 activity raises PARP1's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without CELSR2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[ARHGDIB]] | B | ARHGDIB activity lowers PARP1's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.43× higher at baseline in the lines without ARHGDIB | 0.093 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[SHMT1]] | C | SHMT1 activity raises PARP1's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.59× lower at baseline in the lines without SHMT1 | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.1, -38.8); signed map (-32.0, -41.2). **Vector** length 106, 36.0% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Leading Strand Synthesis* (reactome, mean cos +0.50 to 12); *Polymerase switching* (reactome, mean cos +0.50 to 12); *Polymerase switching on the C-strand of the telomere* (reactome, mean cos +0.50 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.2 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.5 | +9.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.1 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +0.1 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.2 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:226,360,210-226,408,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PARP, ARTD1, Poly-PARP, PARS; previously PPOL, ADPRT |
| Gene groups (HGNC) | Zinc fingers PARP-type; Poly(ADP-ribose) polymerases |
| Reactome | 24 pathways, smallest: vRNA Synthesis; POLB-Dependent Long Patch Base Excision Repair; HDR through MMEJ (alt-NHEJ) |
| Matched by | ensembl_id |

**Function**, from UniProt [P09874](https://www.uniprot.org/uniprotkb/P09874) (Poly):

> Poly-ADP-ribosyltransferase that mediates poly-ADP-ribosylation of proteins and plays a key role in DNA repair. Mediates glutamate, aspartate, serine, threonine, histidine or tyrosine ADP-ribosylation of proteins: the ADP-D-ribosyl group of NAD(+) is transferred to the acceptor carboxyl group of target residues and further ADP-ribosyl groups are transferred to the 2'-position of the terminal adenosine moiety, building up a polymer with an average chain length of 20-30 units. Serine …

**Summary**, from NCBI Gene [142](https://www.ncbi.nlm.nih.gov/gene/142):

> This gene encodes a chromatin-associated enzyme, poly(ADP-ribosyl)transferase, which modifies various nuclear proteins by poly(ADP-ribosyl)ation. The modification is dependent on DNA and is involved in the regulation of various important cellular processes such as differentiation, proliferation, and tumor transformation and also in the regulation of the molecular events involved in the recovery of cell from DNA damage. In addition, this enzyme may be the site of mutation in Fanconi anemia, and …

**Accessions** — [HGNC:270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:270) · Entrez [142](https://www.ncbi.nlm.nih.gov/gene/142) · UniProt [P09874](https://www.uniprot.org/uniprotkb/P09874) · Ensembl [ENSG00000143799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143799)

## Data

Gene col 6806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6806); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6806]; `tensor/DDL_lfc|DDL_z.npy` [6806]; `embed/gene_vectors.npy` [6806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6806 or target_col == 6806). Every well: [[PARP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
