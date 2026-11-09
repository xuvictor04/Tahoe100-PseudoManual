---
symbol: "RNF24"
type: "gene"
col: 2102
ensembl_id: "ENSG00000101236"
name: "ring finger protein 24"
location: "20p13"
module: 79
arm: "+"
pooled_cpm: 191.64
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# RNF24

*ring finger protein 24* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +10.5, q 4e-23, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.308× (z -24.4, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.701× (z -10.8, q 6e-25, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARHSP1]] (+0.70, fdr 7e-06), [[RFX2]] (+0.68, fdr 1e-05), [[ANKRD37]] (+0.67, fdr 7e-06); moves opposite to [[MAPKAPK5]] (-0.72, fdr 7e-06), [[PCBD2]] (-0.68, fdr 1e-05), [[UNC50]] (-0.66, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +10.5 | 4e-23 | 41/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +9.4 | 2e-18 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.0 | 5e-17 | 39/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +8.4 | 4e-15 | 32/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +7.5 | 7e-12 | 42/49 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +7.1 | 9e-11 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +6.6 | 4e-09 | 29/49 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +5.9 | 2e-07 | 29/48 (AsPC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.8 | 4e-07 | 26/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +5.6 | 1e-06 | 27/48 (LOX-IMVI, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.56×** | +5.0 | 3e-05 | 29/48 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +5.0 | 3e-05 | 27/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 17/49 (PANC-1, BT-474, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.017 | 22/48 (AsPC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.048 | 10/48 (LS 180, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.17× | +3.2 | 0.049 | 14/49 (PANC-1, HepG2/C3A, …) | top dose only | plate-row cell shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.1 | 0.070 | 16/49 (PANC-1, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.308×** | -24.4 | 0e+00 | 40/44 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.354×** | -20.1 | 0e+00 | 44/49 (HCT15, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.571×** | -11.1 | 1e-26 | 36/45 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.701×** | -10.8 | 6e-25 | 34/48 (C32, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.668×** | -8.7 | 5e-16 | 34/48 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -6.9 | 4e-10 | 26/49 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -6.7 | 2e-09 | 27/48 (HOP62, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -6.0 | 1e-07 | 37/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -6.0 | 1e-07 | 30/48 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -5.6 | 2e-06 | 29/48 (HT-29, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.782×** | -5.3 | 7e-06 | 29/48 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -5.1 | 2e-05 | 26/48 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -5.0 | 3e-05 | 2/50 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.798×** | -4.8 | 5e-05 | 26/48 (SW 900, LOX-IMVI, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.676×** | -4.4 | 4e-04 | 27/48 (NCI-H1792, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.824×** | -4.1 | 0.001 | 24/48 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.719×** | -3.7 | 0.006 | 21/48 (NCI-H1792, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.747×** | -3.3 | 0.027 | 21/48 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.864× | -3.1 | 0.042 | 20/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.058 | 14/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.768×** | -3.0 | 0.067 | 18/48 (NCI-H1792, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 515 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -25.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -19.9) |
| [[HOP62 (line)]] | alt | 581 | 4 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.427× (z -14.9) |
| [[SW480 (line)]] | alt | 156 | 9 (3 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.91× (z +18.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 107 | 8 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 402 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -22.5) |
| [[SW 900 (line)]] | alt | 276 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.548× (z -11.7) |
| [[BT-474 (line)]] | alt | 212 | 5 (2 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.06× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -16.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 240 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 152 | 3 | 5 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.08× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 183 | 6 (3 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 4.03× (z +18.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -18.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 428 | 2 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.12× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -12.8) |
| [[SNU-423 (line)]] | alt | 326 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 281 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -12.0) |
| [[HS-578T (line)]] | alt | 259 | 5 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.67× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 131 | 1 | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.63× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -14.8) |
| [[A-172 (line)]] | wt | 232 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.549× (z -8.7) |
| [[KATO III (line)]] | alt | 190 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -9.9) |
| [[LS 180 (line)]] | wt | 154 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 184 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 244 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.564× (z -11.0) |
| [[A498 (line)]] | wt | 122 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -13.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 231 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.256× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.603× (z -8.5) |
| [[HCT15 (line)]] | alt | 313 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0422× (z -27.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 109 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.79× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 63.2 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 160 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -18.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 213 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -15.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 233 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -11.3) |
| [[J82 (line)]] | alt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -15.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 60.7 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.89× (z +9.7) | — |
| [[H4 (line)]] | wt | 216 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -12.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 170 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 174 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 69.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.179× (z -16.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.43× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -9.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 94.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -8.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 415 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 201 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 174 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARHSP1]] | +0.70 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RFX2]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TNNI3]] | +0.66 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LIFR]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[BBLN]] | +0.63 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.63 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[SLC2A3]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RNF114]] | +0.62 | +0.52 / +0.51 | both halves | 1e-05 | same gene group |
| [[CDKN2D]] | +0.62 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | -0.72 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[PCBD2]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[UNC50]] | -0.66 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[FAIM]] | -0.63 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[EPM2A]] | -0.62 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ZNF507]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.60 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[DPH5-DT]] | -0.60 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[LINC01355]] | -0.60 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.60 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD40]] | -0.59 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[ZNF587B]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises RNF24's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without PLOD2 | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[NDRG1]] | B | NDRG1 activity raises RNF24's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without NDRG1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[TOP2A]] | B | TOP2A activity raises RNF24's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CFAP45]] | B | CFAP45 activity raises RNF24's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without CFAP45 | 0.035 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[MLLT3]] | B | MLLT3 activity raises RNF24's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without MLLT3 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[SNAP25]] | B | SNAP25 activity raises RNF24's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without SNAP25 | 0.079 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[DEPP1]] | B | DEPP1 activity raises RNF24's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.54× lower at baseline in the lines without DEPP1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[ICAM1]] | B | ICAM1 activity raises RNF24's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.43× lower at baseline in the lines without ICAM1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[NRN1]] | B | NRN1 activity raises RNF24's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without NRN1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[SLC25A37]] | B | SLC25A37 activity raises RNF24's level | lines that do not express SLC25A37 (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without SLC25A37 | 0.099 | ⚠ within organs, on part of the lines; also absent: SSBP2, TP53I13; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -10.5); signed map (-33.4, 21.3). **Vector** length 142, 49.4% of its response variance represented; |z| ≥ 3 in 1,566 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.2 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.7 | +7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +9.2 | +8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.9 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.0 | +5.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.4 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +3.2 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.9 | -10.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -8.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -6.6 | -5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.8 | -4.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.6 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,927,309-4,015,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G1L |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y225](https://www.uniprot.org/uniprotkb/Q9Y225) (RING finger protein 24):

> May play a role in TRPCs intracellular trafficking.

**Summary**, from NCBI Gene [11237](https://www.ncbi.nlm.nih.gov/gene/11237):

> This gene encodes an integral membrane protein that contains a RING-type zinc finger. The encoded protein may interact with multiple transient receptor potential cation channel subfamily C (TRPC) proteins and regulate the trafficking and insertion of these proteins into the plasma membrane. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:13779](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13779) · Entrez [11237](https://www.ncbi.nlm.nih.gov/gene/11237) · UniProt [Q9Y225](https://www.uniprot.org/uniprotkb/Q9Y225) · Ensembl [ENSG00000101236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101236)

## Data

Gene col 2102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2102); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2102]; `tensor/DDL_lfc|DDL_z.npy` [2102]; `embed/gene_vectors.npy` [2102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2102 or target_col == 2102). Every well: [[RNF24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
