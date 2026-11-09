---
symbol: "NCAPD3"
type: "gene"
col: 7532
ensembl_id: "ENSG00000151503"
name: "non-SMC condensin II complex subunit D3"
location: "11q25"
module: 6
arm: "+"
pooled_cpm: 52.64
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NCAPD3

*non-SMC condensin II complex subunit D3* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (20 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.29× (z +19.7, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.06× (z +6.2, q 3e-08, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.701× (z -8.4, q 3e-14, down in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.816× (z -4.8, q 2e-04, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBK]] (+0.87, fdr 7e-06), [[MMS22L]] (+0.87, fdr 7e-06), [[TICRR]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 22 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **3.29×** | +19.7 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **3.09×** | +18.7 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **3.09×** | +18.6 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.60×** | +8.3 | 2e-14 | 37/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.64×** | +8.1 | 4e-14 | 37/48 (SW480, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **1.55×** | +7.2 | 6e-11 | 30/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.48×** | +6.5 | 8e-09 | 34/47 (SW1417, Panc 03.27, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +6.2 | 3e-08 | 26/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +5.9 | 3e-07 | 37/48 (RKO, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.8 | 4e-07 | 23/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.42×** | +5.6 | 1e-06 | 26/43 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +5.4 | 2e-06 | 27/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.34×** | +4.8 | 5e-05 | 23/46 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.37×** | +4.8 | 8e-05 | 26/45 (NCI-H23, H4, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +4.6 | 1e-04 | 24/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.014 | 19/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.032 | 13/47 (PANC-1, Panc 03.27, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.040 | 15/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.701×** | -8.4 | 3e-14 | 35/48 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.664×** | -6.8 | 2e-09 | 33/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.721×** | -5.5 | 9e-06 | 30/48 (HCT15, A498, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.744×** | -5.0 | 1e-04 | 31/48 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.816×** | -4.8 | 2e-04 | 26/48 (HCT15, H4, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.764×** | -4.2 | 0.002 | 24/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.806×** | -4.0 | 0.005 | 19/48 (A-427, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.792×** | -3.9 | 0.007 | 21/47 (NCI-H2030, RKO, …) | two highest doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -3.7 | 0.015 | 19/48 (A-427, NCI-H2030, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.809×** | -3.6 | 0.020 | 16/47 (A-172, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.809×** | -3.6 | 0.020 | 19/48 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.816×** | -3.4 | 0.031 | 17/48 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[palbociclib (drug)]] 5 µM |  | **0.679×** | -3.4 | 0.032 | 13/47 (SK-MEL-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.692×** | -3.2 | 0.053 | 17/48 (hTERT-HPNE, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.821×** | -3.2 | 0.054 | 15/48 (A-427, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.064 | 16/48 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.703×** | -3.1 | 0.066 | 11/48 (A-427, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | 0.840× | -2.9 | 0.094 | 15/48 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.884× | -2.9 | 0.094 | 9/48 (SW 900, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.86 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 38.9 | 7 (7 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 0.05 µM 6.61× (z +10.7) ⚠ cell-cycle shift, explains ~76% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.125× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 90.2 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +15.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 33.7 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.87× (z +9.7) ⚠ cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.296× (z -12.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[KATO III (line)]] | alt | 97.4 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LoVo (line)]] | wt | 31.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.91× (z +11.6) ⚠ cell-cycle shift, explains ~50% of this change | [[Selinexor (drug)]] 5 µM 0.360× (z -12.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H460 (line)]] | wt | 38.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +11.9) ⚠ cell-cycle shift, explains ~50% of this change | [[Selinexor (drug)]] 0.5 µM 0.364× (z -9.7) ⚠ cell-cycle shift, explains ~77% of this change |
| [[PANC-1 (line)]] | alt | 87.3 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[RKO (line)]] | wt | 70.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 29.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.17× (z +9.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 50.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +9.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HS-578T (line)]] | alt | 21.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.29× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LOX-IMVI (line)]] | wt | 45.3 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.91× (z +12.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 56.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +11.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1573 (line)]] | alt | 44.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.54× (z +13.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1792 (line)]] | alt | 26.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.21× (z +10.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H23 (line)]] | alt | 67.9 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.01× (z +10.2) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2347 (line)]] | alt | 46.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +10.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[Panc 03.27 (line)]] | alt | 60.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SNU-423 (line)]] | alt | 30.8 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.44× (z +9.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SW1417 (line)]] | alt | 85.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +11.2) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.61× (z +9.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[CFPAC-1 (line)]] | alt | 29.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +10.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[COLO 205 (line)]] | alt | 23.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.66× (z +8.6) ⚠ cell-cycle shift, explains ~50% of this change | [[Pimozide (drug)]] 0.5 µM 0.134× (z -9.1) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 33.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +9.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-427 (line)]] | wt | 59.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.309× (z -14.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HEC-1-A (line)]] | alt | 92.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 66.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +8.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LS 180 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.309× (z -11.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H2030 (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.454× (z -10.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SNU-1 (line)]] | wt | 74.8 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.296× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.45× (z +8.5) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A549 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 78.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBK]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | STRING 406 |
| [[MMS22L]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 |  |
| [[TICRR]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[MELK]] | +0.84 | +0.84 / +0.84 | both halves | 7e-06 | STRING 455 |
| [[BLM]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[BARD1]] | +0.84 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[FANCI]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 | STRING 471 |
| [[RFC4]] | +0.84 | +0.82 / +0.79 | both halves | 7e-06 | STRING 414 |
| [[DDX12P]] | +0.83 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[SPC25]] | +0.83 | +0.83 / +0.85 | both halves | 7e-06 |  |
| [[POLQ]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises NCAPD3's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without CDC25A | 0.041 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises NCAPD3's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without E2F8 | 0.068 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CRYM]] | B | CRYM activity lowers NCAPD3's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.54× higher at baseline in the lines without CRYM | 0.074 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises NCAPD3's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without TCF19 | 0.086 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[SPINK1]] | B | SPINK1 activity lowers NCAPD3's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.50× higher at baseline in the lines without SPINK1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[DSCC1]] | C | DSCC1 activity raises NCAPD3's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without DSCC1 | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises NCAPD3's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.38× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[SHMT1]] | C | SHMT1 activity raises NCAPD3's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without SHMT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[PBK]] | C | PBK activity raises NCAPD3's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without PBK | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.867). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.3, -44.9); signed map (-37.3, -41.9). **Vector** length 133, 45.2% of its response variance represented; |z| ≥ 3 in 1,374 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *DNA strand elongation* (reactome, mean cos +0.66 to 28); *DNA Replication* (reactome, mean cos +0.65 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.7 | +18.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.0 | +19.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.5 | +18.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.7 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.6 | +8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +6.2 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.3 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -9.2 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.9 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -7.6 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.2 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | non-SMC condensin II complex subunit D3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:134,150,113-134,225,504 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hCAP-D3, CAP-D3, hHCP-6, KIAA0056, FLJ42888, hcp-6 |
| Gene groups (HGNC) | Condensin II subunits; Armadillo like helical domain containing |
| Reactome | 5 pathways, smallest: Condensation of Prophase Chromosomes; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [P42695](https://www.uniprot.org/uniprotkb/P42695) (Condensin-2 complex subunit D3):

> Regulatory subunit of the condensin-2 complex, a complex which establishes mitotic chromosome architecture and is involved in physical rigidity of the chromatid axis. May promote the resolution of double-strand DNA catenanes (intertwines) between sister chromatids. Condensin-mediated compaction likely increases tension in catenated sister chromatids, providing directionality for type II topoisomerase-mediated strand exchanges toward chromatid decatenation. Specifically required for decatenation …

**Summary**, from NCBI Gene [23310](https://www.ncbi.nlm.nih.gov/gene/23310):

> Condensin complexes I and II play essential roles in mitotic chromosome assembly and segregation. Both condensins contain 2 invariant structural maintenance of chromosome (SMC) subunits, SMC2 (MIM 605576) and SMC4 (MIM 605575), but they contain different sets of non-SMC subunits. NCAPD3 is 1 of 3 non-SMC subunits that define condensin II (Ono et al., 2003 [PubMed 14532007]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28952) · Entrez [23310](https://www.ncbi.nlm.nih.gov/gene/23310) · UniProt [P42695](https://www.uniprot.org/uniprotkb/P42695) · Ensembl [ENSG00000151503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151503)

## Data

Gene col 7532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7532); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7532]; `tensor/DDL_lfc|DDL_z.npy` [7532]; `embed/gene_vectors.npy` [7532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7532 or target_col == 7532). Every well: [[NCAPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCAPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
