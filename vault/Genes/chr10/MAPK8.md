---
symbol: "MAPK8"
type: "gene"
col: 2865
ensembl_id: "ENSG00000107643"
name: "mitogen-activated protein kinase 8"
location: "10q11.22"
module: 159
arm: "+"
pooled_cpm: 226.76
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# MAPK8

*mitogen-activated protein kinase 8* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +14.3, q 2e-43, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.435× (z -16.3, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.591× (z -10.3, q 1e-22, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC13B]] (+0.66, fdr 1e-05), [[SMURF2]] (+0.64, fdr 7e-06), [[RASA2]] (+0.61, fdr 2e-05); moves opposite to [[MAIP1]] (-0.60, fdr 2e-04), [[PNISR-AS1]] (-0.58, fdr 5e-05), [[TMEM79]] (-0.58, fdr 3e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RAB3B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +14.3 | 2e-43 | 48/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +13.6 | 2e-39 | 48/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +12.9 | 6e-36 | 47/48 (LOX-IMVI, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +10.8 | 6e-25 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 4e-11 | 36/48 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +6.6 | 4e-09 | 36/48 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.5 | 4e-06 | 33/48 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +5.3 | 7e-06 | 26/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.1 | 2e-05 | 27/48 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +5.0 | 3e-05 | 25/48 (COLO 205, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.9 | 4e-05 | 29/48 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.004 | 33/49 (SW1417, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.021 | 25/48 (NCI-H2347, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.023 | 14/49 (CFPAC-1, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.051 | 19/47 (BT-474, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.435×** | -16.3 | 0e+00 | 46/49 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -13.5 | 3e-39 | 42/44 (Panc 03.27, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.591×** | -10.3 | 1e-22 | 41/48 (SW480, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -7.0 | 3e-10 | 31/49 (NCI-H1792, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.732×** | -6.1 | 9e-08 | 39/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -5.3 | 1e-05 | 27/48 (NCI-H661, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.628×** | -4.8 | 1e-04 | 34/48 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.638×** | -4.6 | 3e-04 | 38/48 (HEC-1-A, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.646×** | -4.5 | 5e-04 | 32/48 (CFPAC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.687×** | -3.9 | 0.006 | 29/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **0.813×** | -3.8 | 0.008 | 23/45 (RKO, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | 0.842× | -3.3 | 0.051 | 19/49 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.846× | -3.2 | 0.066 | 21/47 (RKO, SW1417, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.894× | -3.1 | 0.069 | 3/48 (Panc 03.27, RPMI-7951, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.857× | -3.0 | 0.089 | 19/48 (SW48, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 166 | 9 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -14.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 213 | 7 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 182 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -12.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 293 | 6 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.626× (z -8.8) |
| [[BT-474 (line)]] | alt | 253 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.70× (z +16.5) | — |
| [[Panc 03.27 (line)]] | alt | 211 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -10.7) |
| [[HT-29 (line)]] | alt | 221 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.489× (z -10.0) |
| [[LS 180 (line)]] | wt | 181 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 526 | 2 | 5 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.14× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -9.1) |
| [[SNU-423 (line)]] | alt | 300 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.32× (z +10.9) | [[Auranofin (drug)]] 5 µM 0.338× (z -14.1) |
| [[SW480 (line)]] | alt | 246 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.87× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.289× (z -21.1) |
| [[A-172 (line)]] | wt | 168 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.34× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.523× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 231 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -13.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 329 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -11.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 284 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 196 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.415× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 259 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 192 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.386× (z -11.5) |
| [[A549 (line)]] | wt | 252 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 289 | 5 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +14.5) | — |
| [[HEC-1-A (line)]] | alt | 220 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.91× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.482× (z -11.2) |
| [[HOP62 (line)]] | alt | 296 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 206 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -11.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 306 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.9) |
| [[SW 900 (line)]] | alt | 292 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.470× (z -8.9) |
| [[COLO 205 (line)]] | alt | 127 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.3) | — |
| [[HS-578T (line)]] | alt | 235 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -8.7) |
| [[LoVo (line)]] | wt | 201 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 147 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.04× (z +13.7) | [[Auranofin (drug)]] 5 µM 0.489× (z -8.8) |
| [[A498 (line)]] | wt | 182 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -12.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 149 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 187 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 105 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.16× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 232 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -12.5) |
| [[A-427 (line)]] | wt | 216 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -14.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 276 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.506× (z -9.3) |
| [[HCT15 (line)]] | alt | 231 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 314 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -11.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 236 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.372× (z -8.8) |
| [[C32 (line)]] | wt | 85.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 188 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[H4 (line)]] | wt | 242 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -13.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 168 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +9.4) | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.279× (z -10.4) |
| [[SHP-77 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 228 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC13B]] | +0.66 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SMURF2]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[RASA2]] | +0.61 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ZFAND6]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[INPP4A]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SVIP]] | +0.56 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[CYTH3]] | +0.55 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[PCMT1]] | +0.55 | +0.51 / +0.29 | both halves | 3e-04 |  |
| [[RPS6KA5]] | +0.55 | +0.49 / +0.42 | both halves | 4e-05 | pathway: Interleukin-17 signaling |
| [[MICU2]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ACTG1]] | +0.54 | +0.33 / +0.40 | both halves | 1e-04 | pathway: Leishmania infection |
| [[PAFAH1B3]] | +0.53 | +0.33 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAIP1]] | -0.60 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | -0.58 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TMEM79]] | -0.58 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[MFF-DT]] | -0.58 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[HIKESHI]] | -0.57 | -0.59 / -0.23 | both halves | 5e-04 |  |
| [[PRR3]] | -0.56 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[PEF1]] | -0.56 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[TDP2]] | -0.56 | -0.58 / -0.33 | both halves | 1e-04 | pathway: DNA Double-Strand Break Repair |
| [[CCDC30]] | -0.56 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PAAF1]] | -0.56 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZNF304]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[METTL6]] | -0.55 | -0.46 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB3B]] | B | RAB3B activity raises MAPK8's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.28× lower at baseline in the lines without RAB3B | 0.063 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[VIM]] | B | VIM activity raises MAPK8's level | lines that do not express VIM (18) vs lines expressing it (32) | 1.02× lower at baseline in the lines without VIM | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LOXL2, ADAMTS18, MAP1B |
| [[CCN1]] | B | CCN1 activity raises MAPK8's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without CCN1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.6, 3.9); signed map (-0.7, 51.5). **Vector** length 108, 37.9% of its response variance represented; |z| ≥ 3 in 1,347 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +13.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.2 | +14.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.1 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.3 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.0 | -10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.9 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.3 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:48,306,639-48,439,360 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JNK, JNK1, SAPK1; previously PRKM8 |
| Gene groups (HGNC) | Mitogen-activated protein kinase 8-10 (JNK) family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 53 pathways, smallest: Activation of BIM and translocation to mitochondria; Activation of BMF and translocation to mitochondria; Activation of the AP-1 family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P45983](https://www.uniprot.org/uniprotkb/P45983) (Mitogen-activated protein kinase 8):

> Serine/threonine-protein kinase involved in various processes such as cell proliferation, differentiation, migration, transformation and programmed cell death. Extracellular stimuli such as pro-inflammatory cytokines or physical stress stimulate the stress-activated protein kinase/c-Jun N-terminal kinase (SAP/JNK) signaling pathway. In this cascade, two dual specificity kinases MAP2K4/MKK4 and MAP2K7/MKK7 phosphorylate and activate MAPK8/JNK1. In turn, MAPK8/JNK1 phosphorylates a number of …

**Summary**, from NCBI Gene [5599](https://www.ncbi.nlm.nih.gov/gene/5599):

> The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase is activated by various cell stimuli, and targets specific transcription factors, and thus mediates immediate-early gene expression in response to cell stimuli. The activation of this kinase by …

**Accessions** — [HGNC:6881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6881) · Entrez [5599](https://www.ncbi.nlm.nih.gov/gene/5599) · UniProt [P45983](https://www.uniprot.org/uniprotkb/P45983) · Ensembl [ENSG00000107643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107643)

## Data

Gene col 2865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2865); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2865]; `tensor/DDL_lfc|DDL_z.npy` [2865]; `embed/gene_vectors.npy` [2865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2865 or target_col == 2865). Every well: [[MAPK8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
