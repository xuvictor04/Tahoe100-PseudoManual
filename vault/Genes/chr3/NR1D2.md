---
symbol: "NR1D2"
type: "gene"
col: 10519
ensembl_id: "ENSG00000174738"
name: "nuclear receptor subfamily 1 group D member 2"
location: "3p24.2"
module: 69
arm: "+"
pooled_cpm: 100.85
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 19
n_dd_up_clean: 19
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# NR1D2

*nuclear receptor subfamily 1 group D member 2* — 3p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.95× (z +46.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.491× (z -11.7, q 6e-29, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.478× (z -6.4, q 2e-08, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB10]] (+0.77, fdr 7e-06), [[CREBRF]] (+0.69, fdr 7e-06), [[MTUS1-DT]] (+0.66, fdr 1e-05); moves opposite to [[RNGTT]] (-0.72, fdr 7e-06), [[GBA2]] (-0.59, fdr 1e-05), [[DEPDC5]] (-0.59, fdr 4e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[FAM227B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.95×** | +46.2 | 0e+00 | 48/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.77×** | +24.9 | 0e+00 | 47/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.29×** | +24.1 | 0e+00 | 48/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.61×** | +21.3 | 0e+00 | 46/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +18.8 | 0e+00 | 45/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.45×** | +14.8 | 0e+00 | 42/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.09×** | +14.1 | 4e-43 | 47/49 (HT-29, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.15×** | +12.0 | 4e-31 | 45/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.15×** | +12.0 | 4e-31 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.40×** | +10.6 | 2e-24 | 44/48 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.85×** | +10.2 | 9e-23 | 42/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +9.5 | 7e-20 | 42/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.55×** | +7.3 | 2e-11 | 33/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +6.2 | 2e-08 | 29/48 (LoVo, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.1 | 5e-08 | 30/48 (SW480, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.7 | 8e-05 | 25/48 (C32, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 3e-04 | 27/50 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.2 | 8e-04 | 25/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.491×** | -11.7 | 6e-29 | 46/48 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.580×** | -9.0 | 9e-17 | 37/48 (SW1417, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.607×** | -8.2 | 5e-14 | 38/48 (A-427, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.617×** | -7.5 | 1e-11 | 37/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.478×** | -6.4 | 2e-08 | 40/48 (LoVo, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.684×** | -5.9 | 4e-07 | 36/48 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.506×** | -5.9 | 4e-07 | 38/48 (SW 1271, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.507×** | -5.8 | 4e-07 | 36/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.635×** | -5.3 | 6e-06 | 34/48 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.545×** | -5.2 | 1e-05 | 32/48 (HT-29, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.561×** | -5.0 | 3e-05 | 36/47 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.627×** | -4.0 | 0.003 | 24/48 (HCT15, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.783×** | -4.0 | 0.003 | 27/48 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.716×** | -3.9 | 0.004 | 24/49 (SW48, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.781×** | -3.8 | 0.005 | 28/48 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.789×** | -3.7 | 0.009 | 25/48 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.743×** | -3.5 | 0.017 | 21/48 (SW48, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.046 | 17/49 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Everolimus (drug)]] 5 µM |  | **0.775×** | -3.1 | 0.060 | 17/50 (HCT15, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.8 | 15 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +34.4) | — |
| [[LoVo (line)]] | wt | 90.6 | 11 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.18× (z +32.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.360× (z -11.5) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 256 | 6 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +29.7) | [[Panobinostat (drug)]] 5 µM 0.509× (z -10.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.509× (z -9.5) |
| [[SW48 (line)]] | wt | 178 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +26.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -12.0) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 80.6 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +23.4) | — |
| [[SW480 (line)]] | alt | 72.9 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +19.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.408× (z -10.1) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 153 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +28.4) | — |
| [[NCI-H1792 (line)]] | alt | 84.1 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.21× (z +27.6) | — |
| [[PANC-1 (line)]] | alt | 68.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +34.1) | — |
| [[A549 (line)]] | wt | 73.6 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +34.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -8.9) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 232 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +33.7) | — |
| [[HS-578T (line)]] | alt | 103 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +28.6) | — |
| [[KATO III (line)]] | alt | 99.8 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +28.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 226 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +33.8) | [[Panobinostat (drug)]] 0.5 µM 0.501× (z -9.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 91.1 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.82× (z +27.1) | [[Panobinostat (drug)]] 5 µM 0.351× (z -10.2) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HCT15 (line)]] | alt | 98.5 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +28.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.369× (z -8.6) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 116 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +22.7) | — |
| [[J82 (line)]] | alt | 100 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +27.9) | — |
| [[LOX-IMVI (line)]] | wt | 78.3 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +23.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -11.6) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 81.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +22.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +25.0) | — |
| [[Panc 03.27 (line)]] | alt | 123 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +25.8) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 86.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +23.8) | — |
| [[A-172 (line)]] | wt | 139 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +38.8) | — |
| [[NCI-H1573 (line)]] | alt | 90.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +26.6) | — |
| [[NCI-H23 (line)]] | alt | 47.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +29.5) | — |
| [[RPMI-7951 (line)]] | alt | 150 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +23.2) | — |
| [[SNU-423 (line)]] | alt | 98.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +26.8) | — |
| [[AsPC-1 (line)]] | alt | 73.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +26.3) | — |
| [[BT-474 (line)]] | alt | 64.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +19.9) | — |
| [[C32 (line)]] | wt | 40.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +23.5) | — |
| [[COLO 205 (line)]] | alt | 60.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +23.6) | — |
| [[HepG2_C3A (line)]] | wt | 81.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +18.1) | [[Belinostat (drug)]] 5 µM 0.343× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 83.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +18.9) | — |
| [[A498 (line)]] | wt | 87.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +28.9) | — |
| [[Hs 766T (line)]] | wt | 90.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +22.1) | — |
| [[HT-29 (line)]] | alt | 141 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +22.9) | — |
| [[C-33 A (line)]] | alt | 89.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +17.4) | — |
| [[CFPAC-1 (line)]] | alt | 45.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +25.9) | — |
| [[SNU-1 (line)]] | wt | 75.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +20.1) | — |
| [[NCI-H2030 (line)]] | alt | 39.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +14.7) | — |
| [[SK-MEL-2 (line)]] | alt | 128 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +25.5) | — |
| [[AN3 CA (line)]] | alt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +12.2) | — |
| [[CHP-212 (line)]] | wt | 83.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +12.9) | — |
| [[SW 1088 (line)]] | alt | 94.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +10.5) | — |
| [[SW 1271 (line)]] | alt | 246 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +13.8) | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB10]] | +0.77 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MTUS1-DT]] | +0.66 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[SIRT1]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CYLD]] | +0.63 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NBR1]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CFL2]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ATG2B]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[FMR1]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ITSN2]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RBM33]] | +0.61 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[STAT5A]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.72 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[GBA2]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[DEPDC5]] | -0.59 | -0.40 / -0.61 | both halves | 4e-05 |  |
| [[MYO9B]] | -0.58 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[ZBED4]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[GFOD2]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[LMBR1]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ZFYVE28]] | -0.56 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[TMEM104]] | -0.55 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[ARPC5L]] | -0.55 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[POP1]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[NACC1]] | -0.55 | -0.49 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM227B]] | C | NR1D2's natural level weakens FAM227B's drug response | NR1D2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.43; direction not clear | 0.096 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, -39.3); signed map (12.5, -11.9). **Vector** length 133, 49.6% of its response variance represented; |z| ≥ 3 in 1,629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.3 | +14.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.9 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.7 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.9 | +10.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.4 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.0 | -11.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.7 | -6.4 |
|  | [[EX229 (drug)]] 5 µM |  | -8.4 | -5.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -7.6 | -5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.4 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.3 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 1 group D member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.2 — chr3:23,945,286-23,980,617 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BD73, RVR, EAR-1r, HZF2, Hs.37288, REVERBB, REVERBbeta |
| Gene groups (HGNC) | Nuclear receptor subfamily 1 group D |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14995](https://www.uniprot.org/uniprotkb/Q14995) (Nuclear receptor subfamily 1 group D member 2):

> Transcriptional repressor which coordinates circadian rhythm and metabolic pathways in a heme-dependent manner. Integral component of the complex transcription machinery that governs circadian rhythmicity and forms a critical negative limb of the circadian clock by directly repressing the expression of core clock components BMAL1 and CLOCK. Also regulates genes involved in metabolic functions, including lipid metabolism and the inflammatory response. Acts as a receptor for heme which stimulates …

**Summary**, from NCBI Gene [9975](https://www.ncbi.nlm.nih.gov/gene/9975):

> This gene encodes a member of the nuclear hormone receptor family, specifically the NR1 subfamily of receptors. The encoded protein functions as a transcriptional repressor and may play a role in circadian rhythms and carbohydrate and lipid metabolism. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:7963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7963) · Entrez [9975](https://www.ncbi.nlm.nih.gov/gene/9975) · UniProt [Q14995](https://www.uniprot.org/uniprotkb/Q14995) · Ensembl [ENSG00000174738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174738)

## Data

Gene col 10519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10519); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10519]; `tensor/DDL_lfc|DDL_z.npy` [10519]; `embed/gene_vectors.npy` [10519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10519 or target_col == 10519). Every well: [[NR1D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR1D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
