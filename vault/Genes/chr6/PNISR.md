---
symbol: "PNISR"
type: "gene"
col: 5317
ensembl_id: "ENSG00000132424"
name: "PNN interacting serine and arginine rich protein"
location: "6q16.2"
module: 21
arm: "+"
pooled_cpm: 303.82
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PNISR

*PNN interacting serine and arginine rich protein* — 6q16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.27× (z +14.4, q 3e-44, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.04× (z +12.5, q 2e-33, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.362× (z -17.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAMP2]] (+0.77, fdr 7e-06), [[LUC7L3]] (+0.73, fdr 7e-06), [[PABPN1]] (+0.73, fdr 7e-06); moves opposite to [[TUBG1]] (-0.65, fdr 7e-06), [[EIF2S1]] (-0.65, fdr 7e-06), [[PHB1]] (-0.65, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +14.4 | 3e-44 | 48/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +12.5 | 2e-33 | 48/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +9.6 | 1e-19 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.45×** | +9.3 | 2e-18 | 37/48 (A-172, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +8.0 | 1e-13 | 43/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.5 | 3e-06 | 33/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.36×** | +5.5 | 4e-06 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.35×** | +5.2 | 1e-05 | 31/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +4.9 | 6e-05 | 34/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.6 | 0.020 | 32/48 (LoVo, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.030 | 25/48 (C32, AN3 CA, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.20× | +3.2 | 0.065 | 24/48 (HepG2/C3A, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.362×** | -17.8 | 0e+00 | 48/48 (NCI-H460, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.372×** | -17.3 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.397×** | -16.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.566×** | -10.0 | 3e-21 | 48/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.609×** | -8.7 | 3e-16 | 47/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.796×** | -5.7 | 1e-06 | 26/49 (HT-29, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.548×** | -5.5 | 3e-06 | 46/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.788×** | -4.2 | 0.002 | 35/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.2 | 0.079 | 23/48 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.096 | 21/49 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 304 | 7 (2 ⚠) | 5 | [[Digitoxin (drug)]] 5 µM 2.65× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.295× (z -19.0) |
| [[PANC-1 (line)]] | alt | 430 | 6 (2 ⚠) | 5 | [[Digitoxin (drug)]] 5 µM 2.55× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +15.1) | [[Belinostat (drug)]] 5 µM 0.341× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 297 | 7 (3 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.99× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +11.8) | [[Belinostat (drug)]] 5 µM 0.364× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 258 | 5 (2 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 3.83× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -11.1) |
| [[C32 (line)]] | wt | 248 | 6 (3 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 3.12× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.391× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 328 | 3 (2 ⚠) | 5 | [[Digitoxin (drug)]] 5 µM 1.99× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.294× (z -16.3) |
| [[KATO III (line)]] | alt | 282 | 5 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.334× (z -14.1) |
| [[LoVo (line)]] | wt | 377 | 6 (3 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 3.42× (z +16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +15.0) | [[Belinostat (drug)]] 5 µM 0.513× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 281 | 5 (2 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.93× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.353× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 391 | 4 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.313× (z -15.0) |
| [[HS-578T (line)]] | alt | 252 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.415× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 381 | 3 (2 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 2.43× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.279× (z -15.6) |
| [[SHP-77 (line)]] | alt | 321 | 3 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.32× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.401× (z -12.8) |
| [[SNU-1 (line)]] | wt | 579 | 3 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.67× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.290× (z -15.9) |
| [[SW 900 (line)]] | alt | 324 | 3 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 2.38× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.317× (z -13.6) |
| [[A-172 (line)]] | wt | 199 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +19.4) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -11.0) |
| [[A-427 (line)]] | wt | 265 | 3 (2 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.27× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.444× (z -11.5) |
| [[BT-474 (line)]] | alt | 292 | 2 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 2.10× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -10.9) |
| [[COLO 205 (line)]] | alt | 217 | 3 (2 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.48× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.364× (z -12.0) |
| [[HCT15 (line)]] | alt | 525 | 2 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.04× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.279× (z -18.3) |
| [[J82 (line)]] | alt | 251 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.389× (z -11.5) |
| [[LS 180 (line)]] | wt | 433 | 2 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.20× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.473× (z -10.1) |
| [[RKO (line)]] | wt | 310 | 3 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.92× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.5) | [[Belinostat (drug)]] 5 µM 0.365× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 309 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.2) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -13.4) |
| [[SW1417 (line)]] | alt | 232 | 2 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 2.48× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.404× (z -11.8) |
| [[SW480 (line)]] | alt | 216 | 3 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.33× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.345× (z -15.4) |
| [[A498 (line)]] | wt | 164 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.5) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 5 µM 0.361× (z -11.7) |
| [[C-33 A (line)]] | alt | 552 | 2 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.07× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.378× (z -14.0) |
| [[H4 (line)]] | wt | 215 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.4) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 253 | 2 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.36× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.319× (z -13.7) |
| [[HOP62 (line)]] | alt | 275 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.2) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 5 µM 0.312× (z -12.9) |
| [[HT-29 (line)]] | alt | 366 | 1 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.88× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.386× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 288 | 2 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 3.59× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -12.8) |
| [[SNU-423 (line)]] | alt | 420 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -16.3) |
| [[SW48 (line)]] | wt | 351 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.376× (z -10.4) |
| [[A549 (line)]] | wt | 221 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.17× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.302× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 236 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.2) ⚠ cell-cycle shift, explains ~52% of this change | [[Belinostat (drug)]] 5 µM 0.327× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 205 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -14.8) |
| [[Hs 766T (line)]] | wt | 360 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 1.98× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.311× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 242 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -15.8) |
| [[AN3 CA (line)]] | alt | 436 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.20× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.450× (z -8.8) |
| [[CHP-212 (line)]] | wt | 430 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.338× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 304 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.422× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 446 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.363× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 232 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -13.3) |
| [[SW 1271 (line)]] | alt | 564 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -11.8) |
| [[NCI-H661 (line)]] | alt | 412 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -9.3) |
| [[SW 1088 (line)]] | alt | 251 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.178× (z -9.3) |
| [[NCI-H2122 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 358 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP2]] | +0.77 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[LUC7L3]] | +0.73 | +0.76 / +0.75 | both halves | 7e-06 | STRING 999 |
| [[PABPN1]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[NAA38]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SRSF11]] ⚠ | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | STRING 945; ⚠ in the vector space only through flagged drug-doses |
| [[YTHDC1]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[RNPC3]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 | STRING 495 |
| [[TMEM91]] | +0.64 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ZSCAN16-AS1]] | +0.63 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FAM151B-DT]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[FMC1]] | +0.63 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[CD72]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[XPA]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBG1]] | -0.65 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[EIF2S1]] | -0.65 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[PHB1]] | -0.65 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[BLTP2]] | -0.62 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[SLC25A39]] | -0.62 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[STK25]] | -0.61 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TINF2]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[EHD4]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[B4GALT7]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PSMD2]] | -0.59 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TTLL12]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RIC8A]] | -0.57 | -0.55 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PNISR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.2, -4.6); signed map (-6.1, 2.2). **Vector** length 131, 55.0% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +9.7 | +9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.2 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +14.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.4 | +5.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +5.1 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +4.8 | +1.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.3 | +0.7 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -7.7 | -1.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.6 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.0 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -17.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.5 | -1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.5 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +2.0 |

## What is on record

|  |  |
|---|---|
| Name | PNN interacting serine and arginine rich protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.2 — chr6:99,397,629-99,425,331 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14752, bA98I9.2, DKFZp564B0769, SRrp130; previously C6orf111, SFRS18 |
| Matched by | ensembl_id |

UniProt [Q8TF01](https://www.uniprot.org/uniprotkb/Q8TF01) carries no function annotation.

**Summary**, from NCBI Gene [25957](https://www.ncbi.nlm.nih.gov/gene/25957):

> Enables RNA binding activity. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21222) · Entrez [25957](https://www.ncbi.nlm.nih.gov/gene/25957) · UniProt [Q8TF01](https://www.uniprot.org/uniprotkb/Q8TF01) · Ensembl [ENSG00000132424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132424)

## Data

Gene col 5317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5317); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5317]; `tensor/DDL_lfc|DDL_z.npy` [5317]; `embed/gene_vectors.npy` [5317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5317 or target_col == 5317). Every well: [[PNISR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNISR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
