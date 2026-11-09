---
symbol: "TMEM241"
type: "gene"
col: 5568
ensembl_id: "ENSG00000134490"
name: "solute carrier family 35 member D4"
location: "18q11.2"
module: 211
arm: "+"
pooled_cpm: 40.31
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# TMEM241

*solute carrier family 35 member D4* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.55× (z +27.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.539× (z -15.7, q 0e+00, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.317× (z -10.7, q 7e-25, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE3D]] (+0.69, fdr 1e-05), [[ST6GALNAC4]] (+0.69, fdr 5e-05), [[GNPNAT1]] (+0.67, fdr 1e-05); moves opposite to [[EP300]] (-0.65, fdr 6e-05), [[CDKN1B]] (-0.63, fdr 1e-05), [[C3orf38]] (-0.62, fdr 4e-05).
> It is in [[Module 211]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.55×** | +27.0 | 0e+00 | 48/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.98×** | +24.6 | 0e+00 | 47/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.93×** | +24.3 | 0e+00 | 48/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +17.9 | 0e+00 | 48/48 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.69×** | +15.1 | 0e+00 | 48/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +12.8 | 2e-35 | 41/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.84×** | +9.7 | 2e-20 | 43/48 (A-172, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +9.5 | 1e-19 | 40/48 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +9.3 | 8e-19 | 37/48 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.76×** | +5.2 | 9e-06 | 28/48 (KATO III, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.70×** | +4.9 | 5e-05 | 24/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.63×** | +4.5 | 3e-04 | 18/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 4e-04 | 20/48 (KATO III, SW1417, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 4e-04 | 18/48 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.004 | 18/48 (NCI-H2347, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.007 | 18/48 (RKO, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.539×** | -15.7 | 0e+00 | 37/47 (PANC-1, HEC-1-A, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -12.1 | 4e-31 | 38/47 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.527×** | -11.5 | 3e-28 | 41/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.531×** | -10.9 | 1e-25 | 35/48 (PANC-1, A-427, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.317×** | -10.7 | 7e-25 | 44/48 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -8.4 | 4e-15 | 31/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -7.2 | 5e-11 | 32/48 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.678×** | -7.0 | 2e-10 | 32/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.591×** | -4.9 | 5e-05 | 23/48 (SHP-77, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.740×** | -4.7 | 2e-04 | 23/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.6 | 2e-04 | 22/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~95% of this change | **0.794×** | -4.2 | 0.001 | 19/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.807×** | -3.7 | 0.008 | 18/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -3.7 | 0.008 | 17/48 (A-427, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.816×** | -3.4 | 0.025 | 18/47 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 0.839× | -3.2 | 0.050 | 10/48 (PANC-1, SW48, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.070 | 11/48 (PANC-1, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 71.9 | 5 | 11 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -27.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.189× (z -11.8) |
| [[SW480 (line)]] | alt | 53.3 | 5 | 8 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +13.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -14.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.190× (z -9.8) |
| [[KATO III (line)]] | alt | 49.0 | 3 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 4.45× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0756× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 39.8 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.76× (z +18.0) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 86.5 | 4 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.86× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.149× (z -9.2) |
| [[A-172 (line)]] | wt | 23.5 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 8.53× (z +15.7) | — |
| [[A-427 (line)]] | wt | 95.1 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.252× (z -14.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0886× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 55.8 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.87× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -21.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.183× (z -9.4) |
| [[LS 180 (line)]] | wt | 28.3 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 6.33× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SHP-77 (line)]] | alt | 44.0 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.04× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.107× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[PF-06260933 (drug)]] 5 µM 0.0897× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 41.4 | 3 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 4.79× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HOP62 (line)]] | alt | 26.6 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.52× (z +15.3) | [[Digitoxin (drug)]] 5 µM 0.295× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 41.9 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.95× (z +13.6) | [[Harringtonine (drug)]] 5 µM 0.216× (z -12.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 51.7 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.88× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 30.4 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A498 (line)]] | wt | 20.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.54× (z +12.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 28.2 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 4.56× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H1792 (line)]] | alt | 50.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.88× (z +13.1) | [[Harringtonine (drug)]] 5 µM 0.320× (z -9.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2347 (line)]] | alt | 19.7 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.91× (z +11.4) | — |
| [[C32 (line)]] | wt | 19.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +13.2) | — |
| [[Hs 766T (line)]] | wt | 46.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.56× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.32× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 38.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 57.2 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.79× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 26.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.00× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW 900 (line)]] | alt | 20.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.79× (z +12.0) | — |
| [[SW48 (line)]] | wt | 47.1 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.39× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.186× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 92.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CFPAC-1 (line)]] | alt | 26.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.55× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 38.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.95× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 7.52× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 25.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.51× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 43.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.60× (z +16.9) | — |
| [[RKO (line)]] | wt | 40.8 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.75× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.203× (z -10.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.47× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 26.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.65× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 49.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -10.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[H4 (line)]] | wt | 32.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.00× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.101× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 23.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.73× (z +9.6) | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Raltitrexed (drug)]] 5 µM 0.367× (z -9.0) ⚠ cell-cycle shift, explains ~11% of this change |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE3D]] | +0.69 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.69 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[GNPNAT1]] | +0.67 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.66 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[CLYBL]] | +0.66 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[GARNL3]] | +0.66 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NLE1]] | +0.65 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.65 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PDCD11]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ARHGAP8]] | +0.64 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[C20orf27]] | +0.64 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CMSS1]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EP300]] | -0.65 | -0.38 / -0.65 | both halves | 6e-05 |  |
| [[CDKN1B]] | -0.63 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[C3orf38]] | -0.62 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[USP11]] | -0.60 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[CREBBP]] | -0.60 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[ACBD5]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[FAM120AOS]] | -0.58 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[TET2]] | -0.57 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[LINC03048]] | -0.57 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[NCOA2]] | -0.57 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[ZNF490]] | -0.56 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[KDM3B]] | -0.56 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.1, -40.4); signed map (-9.9, -55.0). **Vector** length 103, 30.1% of its response variance represented; |z| ≥ 3 in 1,377 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.8 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +17.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +12.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.0 | +15.1 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.7 | +4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.3 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.1 | +5.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -8.0 | -15.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.7 | -10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member D4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:23,197,144-23,437,961 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11386, FLJ44259; previously C18orf45, TMEM241 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q24JQ0](https://www.uniprot.org/uniprotkb/Q24JQ0) (UDP-N-acetylglucosamine transporter SLC35D4):

> Golgi-localized UDP-N-acetylglucosamine (UDP-GlcNAc) transporter that transports UDP-N-acetylglucosamine into Golgi lumen. Contributes to lysosomal targeting of NPC2, a key protein required for lysosomal cholesterol exiting, and that utilizes the mannose-6-phosphate (M6P) modification pathway for its lysosomal targeting.

**Summary**, from NCBI Gene [85019](https://www.ncbi.nlm.nih.gov/gene/85019):

> Enables UDP-N-acetylglucosamine transmembrane transporter activity. Involved in UDP-N-acetylglucosamine transmembrane transport. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31723) · Entrez [85019](https://www.ncbi.nlm.nih.gov/gene/85019) · UniProt [Q24JQ0](https://www.uniprot.org/uniprotkb/Q24JQ0) · Ensembl [ENSG00000134490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134490)

## Data

Gene col 5568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5568); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5568]; `tensor/DDL_lfc|DDL_z.npy` [5568]; `embed/gene_vectors.npy` [5568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5568 or target_col == 5568). Every well: [[TMEM241 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM241.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
