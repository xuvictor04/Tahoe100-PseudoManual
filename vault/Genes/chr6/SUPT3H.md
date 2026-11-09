---
symbol: "SUPT3H"
type: "gene"
col: 12171
ensembl_id: "ENSG00000196284"
name: "SPT3 homolog, SAGA and STAGA complex component"
location: "6p21.1"
module: 211
arm: "+"
pooled_cpm: 208.61
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 34
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# SUPT3H

*SPT3 homolog, SAGA and STAGA complex component* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Sapanisertib (drug)]] 0.05 µM: 1.31× (z +4.5, q 0.004, up in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[BAY1125976 (drug)]] 5 µM: 1.45× (z +3.4, q 0.061, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (25 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.456× (z -19.5, q 0e+00, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.544× (z -15.1, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADK]] (+0.67, fdr 7e-06), [[SLC39A11]] (+0.65, fdr 1e-05), [[DIAPH2]] (+0.64, fdr 7e-06); moves opposite to [[HOXA3]] (-0.54, fdr 1e-05), [[PEX13]] (-0.52, fdr 2e-05), [[HOXB3]] (-0.51, fdr 3e-05).
> It is in [[Module 211]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.31×** | +4.5 | 0.004 | 33/47 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.2 | 0.009 | 26/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.37×** | +3.9 | 0.017 | 33/47 (HS-578T, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.25×** | +3.8 | 0.019 | 22/46 (C32, SW480, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.061 | 26/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.061 | 19/47 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.061 | 26/48 (A-427, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.074 | 24/46 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.074 | 20/47 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.39× | +3.0 | 0.15 | 19/49 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 27 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12171.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.456×** | -19.5 | 0e+00 | 43/47 (RKO, NCI-H1573, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.394×** | -16.4 | 0e+00 | 47/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.419×** | -15.3 | 0e+00 | 47/47 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -15.1 | 0e+00 | 44/48 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.414×** | -14.9 | 0e+00 | 40/43 (HCT15, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.443×** | -14.3 | 2e-44 | 44/47 (SNU-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.446×** | -13.7 | 1e-40 | 43/46 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.462×** | -13.5 | 6e-40 | 47/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.240×** | -13.1 | 1e-37 | 47/48 (LOX-IMVI, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.452×** | -12.9 | 2e-36 | 38/44 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.518×** | -11.5 | 4e-29 | 38/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.506×** | -11.5 | 5e-29 | 40/47 (RKO, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.487×** | -10.3 | 4e-23 | 39/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.607×** | -8.8 | 7e-17 | 43/47 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.615×** | -8.5 | 5e-16 | 36/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -7.3 | 1e-11 | 36/47 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -6.3 | 7e-09 | 32/47 (SW480, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.765×** | -4.7 | 6e-05 | 33/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.838× | -4.4 | 2e-04 | 20/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.626×** | -4.3 | 3e-04 | 32/47 (RKO, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.004 | 23/47 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.698×** | -3.3 | 0.015 | 25/48 (HepG2/C3A, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.018 | 26/46 (AsPC-1, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.846× | -2.8 | 0.072 | 19/47 (C32, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 432 | 0 | 20 (18 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -17.2) |
| [[PANC-1 (line)]] | alt | 254 | 0 | 18 (16 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -23.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -15.9) |
| [[HOP62 (line)]] | alt | 423 | 0 | 17 (13 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -17.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 378 | 0 | 17 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -25.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -20.9) |
| [[NCI-H460 (line)]] | wt | 108 | 1 (1 ⚠) | 15 (13 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.09× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -21.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -9.0) |
| [[RKO (line)]] | wt | 320 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -30.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.118× (z -11.3) |
| [[H4 (line)]] | wt | 319 | 0 | 14 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -8.9) |
| [[HS-578T (line)]] | alt | 338 | 0 | 14 (12 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -18.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 312 | 0 | 14 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.125× (z -22.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.115× (z -12.8) |
| [[SNU-423 (line)]] | alt | 356 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -19.1) |
| [[C32 (line)]] | wt | 212 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -24.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 135 | 0 | 12 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -26.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 207 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 185 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -20.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.172× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 325 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -26.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 299 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -25.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.412× (z -11.3) |
| [[SNU-1 (line)]] | wt | 202 | 0 | 11 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0997× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 321 | 0 | 10 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -22.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -19.3) |
| [[J82 (line)]] | alt | 173 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 319 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -23.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -14.4) |
| [[SHP-77 (line)]] | alt | 174 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -13.1) |
| [[SW480 (line)]] | alt | 169 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -19.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.318× (z -17.4) |
| [[C-33 A (line)]] | alt | 261 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.405× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 205 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -21.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 304 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -17.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -13.6) |
| [[KATO III (line)]] | alt | 195 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -11.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A498 (line)]] | wt | 123 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -13.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -9.0) |
| [[LoVo (line)]] | wt | 205 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.473× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 233 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -13.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.168× (z -10.7) |
| [[SW 900 (line)]] | alt | 158 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -13.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.128× (z -12.2) |
| [[A-172 (line)]] | wt | 96.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.202× (z -10.1) |
| [[A549 (line)]] | wt | 135 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -13.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 110 | 1 (1 ⚠) | 5 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.59× (z +9.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.1) |
| [[SW1417 (line)]] | alt | 142 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.232× (z -16.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.250× (z -8.5) |
| [[SW48 (line)]] | wt | 219 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -15.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 114 | 1 (1 ⚠) | 4 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.68× (z +9.6) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.6) |
| [[HCT15 (line)]] | alt | 148 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0552× (z -26.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[BT-474 (line)]] | alt | 88.4 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -10.2) ⚠ cell-cycle shift, explains ~52% of this change |
| [[LS 180 (line)]] | wt | 132 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.180× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -12.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.135× (z -11.4) |
| [[AN3 CA (line)]] | alt | 212 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -12.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW 1271 (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0634× (z -13.9) ⚠ transcription drop; cell-cycle shift, explains ~53% of this change |
| [[CHP-212 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADK]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SLC39A11]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DIAPH2]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ERC1]] | +0.63 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[IMMP2L]] | +0.62 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[NLN]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NDUFAF2]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.58 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[PHF14]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[CMSS1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RABGAP1L]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[HLCS]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA3]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PEX13]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[HOXB3]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 | same gene group |
| [[RHOXF1]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[PPM1D]] | -0.50 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[HNMT]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[DHRS3]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 | same gene group |
| [[USP33]] | -0.47 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[ITM2B]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CBX8]] | -0.47 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[PIGS]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.5, -34.4); signed map (3.9, -52.2). **Vector** length 96.2, 37.5% of its response variance represented; |z| ≥ 3 in 1,710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.7 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +1.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.9 | -13.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.3 | -13.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | -4.6 | -8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.8 | +0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | SPT3 homolog, SAGA and STAGA complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:44,809,317-45,377,953 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPT3, SPT3L |
| Gene groups (HGNC) | SAGA complex; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O75486](https://www.uniprot.org/uniprotkb/O75486) (Transcription initiation protein SPT3 homolog):

> Probable transcriptional activator.

**Summary**, from NCBI Gene [8464](https://www.ncbi.nlm.nih.gov/gene/8464):

> Enables transcription coactivator activity. Involved in regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of SAGA complex and transcription factor TFTC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11466) · Entrez [8464](https://www.ncbi.nlm.nih.gov/gene/8464) · UniProt [O75486](https://www.uniprot.org/uniprotkb/O75486) · Ensembl [ENSG00000196284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196284)

## Data

Gene col 12171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12171); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12171]; `tensor/DDL_lfc|DDL_z.npy` [12171]; `embed/gene_vectors.npy` [12171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12171 or target_col == 12171). Every well: [[SUPT3H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUPT3H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
