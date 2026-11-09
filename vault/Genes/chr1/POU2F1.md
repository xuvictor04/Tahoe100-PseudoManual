---
symbol: "POU2F1"
type: "gene"
col: 6694
ensembl_id: "ENSG00000143190"
name: "POU class 2 homeobox 1"
location: "1q24.2"
module: 186
arm: "+"
pooled_cpm: 198.35
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# POU2F1

*POU class 2 homeobox 1* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.10× (z +16.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.429× (z -18.6, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.734× (z -7.1, q 2e-10, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID2]] (+0.60, fdr 1e-05), [[PPP2R5E]] (+0.58, fdr 1e-05), [[TCF20]] (+0.56, fdr 1e-05); moves opposite to [[ASCC2]] (-0.58, fdr 3e-05), [[AP3D1]] (-0.57, fdr 2e-04), [[DDX1]] (-0.56, fdr 3e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Imiquimod (hydrochloride) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.10×** | +16.9 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +14.3 | 6e-44 | 38/49 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +13.4 | 9e-39 | 45/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +12.1 | 1e-31 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +10.7 | 2e-24 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +7.2 | 6e-11 | 33/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.3 | 2e-08 | 31/48 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.2 | 1e-05 | 28/45 (SNU-423, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.9 | 5e-05 | 28/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +4.9 | 5e-05 | 24/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 27/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.001 | 22/48 (Hs 766T, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 22/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.15× | +3.1 | 0.082 | 14/49 (LoVo, CFPAC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.0 | 0.091 | 17/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.429×** | -18.6 | 0e+00 | 43/44 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.480×** | -16.7 | 0e+00 | 45/49 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.595×** | -11.0 | 1e-25 | 39/45 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -8.6 | 1e-15 | 42/47 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.734×** | -7.1 | 2e-10 | 37/48 (HT-29, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.753×** | -6.5 | 8e-09 | 33/48 (HS-578T, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.616×** | -5.8 | 6e-07 | 37/47 (AsPC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.798×** | -5.2 | 2e-05 | 29/48 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.806×** | -4.9 | 5e-05 | 25/48 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -4.7 | 1e-04 | 20/48 (NCI-H1792, COLO 205, …) | rises with dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.681×** | -4.6 | 2e-04 | 33/48 (KATO III, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.683×** | -4.6 | 2e-04 | 28/48 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.835× | -4.1 | 0.002 | 23/48 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.725×** | -3.8 | 0.005 | 24/48 (AsPC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.6 | 0.014 | 19/48 (SK-MEL-2, LOX-IMVI, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.861× | -3.2 | 0.043 | 16/48 (NCI-H661, SW480, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.871× | -3.2 | 0.051 | 12/49 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.874× | -3.1 | 0.062 | 11/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 186 | 3 (1 ⚠) | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 201 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -13.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 199 | 6 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.38× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.471× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 188 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +14.1) | [[Auranofin (drug)]] 5 µM 0.442× (z -12.3) |
| [[H4 (line)]] | wt | 154 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 140 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -14.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 223 | 3 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -10.8) |
| [[PANC-1 (line)]] | alt | 182 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +22.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +22.8) | [[Dinaciclib (drug)]] 0.5 µM 0.514× (z -12.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 226 | 1 | 6 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 6.06× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -12.2) |
| [[HOP62 (line)]] | alt | 132 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 221 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.568× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 338 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.488× (z -11.6) |
| [[SW 900 (line)]] | alt | 176 | 6 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -9.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 193 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +17.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 196 | 2 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 208 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 218 | 2 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -17.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 226 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +18.2) | [[Auranofin (drug)]] 5 µM 0.481× (z -10.6) |
| [[A498 (line)]] | wt | 175 | 3 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.63× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 189 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.510× (z -10.2) |
| [[J82 (line)]] | alt | 181 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -13.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 212 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.524× (z -10.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 309 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -19.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 228 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -9.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 163 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -11.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 188 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.397× (z -11.1) |
| [[HS-578T (line)]] | alt | 149 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +8.9) | [[Lonafarnib (drug)]] 5 µM 0.128× (z -13.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -11.7) |
| [[LS 180 (line)]] | wt | 168 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 175 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -11.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 323 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 153 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -14.9) |
| [[HCT15 (line)]] | alt | 257 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 240 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.494× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 231 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -12.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 153 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 263 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +14.2) | — |
| [[A-172 (line)]] | wt | 167 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -17.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 228 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 148 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +15.2) | — |
| [[RKO (line)]] | wt | 223 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 167 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -9.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 291 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -12.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 126 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 264 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -17.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0965× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 173 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +8.5) | — |
| [[NCI-H2122 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID2]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[PPP2R5E]] | +0.58 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[TCF20]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PTPRJ]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PHLPP1]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ZMYM2]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PAN3]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[PDS5B]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[HOXB6]] | +0.52 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[WDFY3]] | +0.52 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PPM1B]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[SRPK2]] | +0.52 | +0.65 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASCC2]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[AP3D1]] | -0.57 | -0.69 / -0.32 | both halves | 2e-04 |  |
| [[DDX1]] | -0.56 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A46]] | -0.55 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[ZMYM6]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[GTF2H3]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TRAK2]] | -0.53 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[DRG2]] | -0.51 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[FBXW8]] | -0.50 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[EDC3]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CLCN6]] | -0.49 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[TBRG1]] | -0.49 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Imiquimod (hydrochloride) (drug)]] 0.05 µM | C | POU2F1's natural level raises the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (protects the cells) | POU2F1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.304 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.5, -52.8); signed map (-20.0, 16.2). **Vector** length 122, 43.8% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +15.3 | +14.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +6.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.7 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.7 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.6 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -7.1 |
|  | [[EX229 (drug)]] 5 µM |  | -5.2 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.0 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | POU class 2 homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:167,220,876-167,427,345 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OCT1; previously OTF1 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 13 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 3 Promoter; RNA Polymerase III Transcription Initiation; RNA Polymerase III Abortive And Retractive Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P14859](https://www.uniprot.org/uniprotkb/P14859) (POU domain, class 2, transcription factor 1):

> Transcription factor that binds to the octamer motif (5'-ATTTGCAT-3') and activates the promoters of the genes for some small nuclear RNAs (snRNA) and of genes such as those for histone H2B and immunoglobulins. Modulates transcription transactivation by NR3C1, AR and PGR.; (Microbial infection) In case of human herpes simplex virus (HSV) infection, POU2F1 forms a multiprotein-DNA complex with the viral transactivator protein VP16 and HCFC1 thereby enabling the transcription of the viral …

**Summary**, from NCBI Gene [5451](https://www.ncbi.nlm.nih.gov/gene/5451):

> The OCT1 transcription factor was among the first identified members of the POU transcription factor family (summarized by Sturm et al., 1993 [PubMed 8314572]). Members of this family contain the POU domain, a 160-amino acid region necessary for DNA binding to the octameric sequence ATGCAAAT.[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:9212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9212) · Entrez [5451](https://www.ncbi.nlm.nih.gov/gene/5451) · UniProt [P14859](https://www.uniprot.org/uniprotkb/P14859) · Ensembl [ENSG00000143190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143190)

## Data

Gene col 6694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6694); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6694]; `tensor/DDL_lfc|DDL_z.npy` [6694]; `embed/gene_vectors.npy` [6694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6694 or target_col == 6694). Every well: [[POU2F1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU2F1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
