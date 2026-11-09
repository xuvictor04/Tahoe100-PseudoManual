---
symbol: "FAM193A"
type: "gene"
col: 4609
ensembl_id: "ENSG00000125386"
name: "family with sequence similarity 193 member A"
location: "4p16.3"
module: 20
arm: "-"
pooled_cpm: 220.63
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# FAM193A

*family with sequence similarity 193 member A* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.77× (z +16.1, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.362× (z -28.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASH1L]] (+0.67, fdr 1e-05), [[LRCH3]] (+0.67, fdr 1e-05), [[RFX1]] (+0.65, fdr 1e-05); moves opposite to [[LINC03009]] (-0.64, fdr 2e-05), [[CRYZ]] (-0.60, fdr 2e-05), [[PGAM1]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +16.1 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +12.6 | 8e-34 | 32/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +11.9 | 4e-30 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +9.8 | 1e-20 | 38/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +9.4 | 8e-19 | 40/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.003 | 25/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.2 | 0.003 | 18/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.8 | 0.009 | 9/48 (KATO III, H4, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.082 | 17/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.082 | 22/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.2 | 0.082 | 18/48 (PANC-1, HEC-1-A, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.362×** | -28.6 | 0e+00 | 48/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.368×** | -28.1 | 0e+00 | 46/49 (NCI-H1792, HCT15, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.371×** | -27.9 | 0e+00 | 48/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.363×** | -26.4 | 0e+00 | 44/45 (C-33 A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -25.0 | 0e+00 | 43/44 (SK-MEL-2, H4, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -22.8 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.603×** | -14.2 | 4e-44 | 46/48 (SNU-423, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -12.4 | 3e-33 | 46/48 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.750×** | -11.5 | 9e-29 | 31/49 (A-172, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.672×** | -10.8 | 2e-25 | 41/47 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -8.9 | 3e-17 | 30/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.812×** | -8.3 | 4e-15 | 30/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.769×** | -7.4 | 5e-12 | 31/48 (SW 1271, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.772×** | -7.3 | 1e-11 | 40/48 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.622×** | -5.7 | 4e-07 | 39/49 (NCI-H1792, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.845× | -4.6 | 1e-04 | 18/48 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.871× | -3.9 | 0.002 | 15/48 (SNU-423, A-172, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.014 | 19/49 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.887× | -3.1 | 0.039 | 13/47 (COLO 205, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.930× | -3.0 | 0.069 | 2/48 (AsPC-1, NCI-H2347) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.931× | -2.9 | 0.076 | 6/48 (A-172, BT-474, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.868× | -2.9 | 0.083 | 14/47 (HCT15, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 228 | 7 (3 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -19.7) |
| [[SW480 (line)]] | alt | 182 | 5 (1 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +16.1) | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -21.4) |
| [[A-172 (line)]] | wt | 245 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.337× (z -18.4) |
| [[SW 900 (line)]] | alt | 247 | 2 | 10 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.325× (z -17.4) |
| [[HT-29 (line)]] | alt | 203 | 3 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.297× (z -20.4) |
| [[LoVo (line)]] | wt | 195 | 4 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.483× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 247 | 1 | 10 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -21.5) |
| [[PANC-1 (line)]] | alt | 177 | 5 (2 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 198 | 2 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.419× (z -16.6) |
| [[HOP62 (line)]] | alt | 299 | 1 | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -20.2) |
| [[KATO III (line)]] | alt | 181 | 4 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.306× (z -18.9) |
| [[LOX-IMVI (line)]] | wt | 339 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -26.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.242× (z -22.2) |
| [[MIA PaCa-2 (line)]] | alt | 225 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.271× (z -20.5) |
| [[SNU-423 (line)]] | alt | 232 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -18.0) |
| [[A549 (line)]] | wt | 202 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -28.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.308× (z -20.9) |
| [[CFPAC-1 (line)]] | alt | 240 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.434× (z -15.4) |
| [[COLO 205 (line)]] | alt | 176 | 5 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +16.8) | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -12.5) |
| [[H4 (line)]] | wt | 254 | 3 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0984× (z -31.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.384× (z -13.4) |
| [[J82 (line)]] | alt | 309 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -28.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -21.3) |
| [[NCI-H1573 (line)]] | alt | 351 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 226 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.285× (z -21.0) |
| [[A498 (line)]] | wt | 248 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -18.5) |
| [[C32 (line)]] | wt | 251 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 188 | 4 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.384× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 214 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 174 | 1 | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.444× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 239 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0524× (z -47.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.363× (z -17.1) |
| [[AsPC-1 (line)]] | alt | 201 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -20.0) |
| [[BT-474 (line)]] | alt | 198 | 1 (1 ⚠) | 6 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 1.97× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -17.4) |
| [[Hs 766T (line)]] | wt | 163 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.360× (z -14.9) |
| [[HS-578T (line)]] | alt | 153 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -19.0) |
| [[hTERT-HPNE (line)]] | wt | 194 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -16.5) |
| [[SW1417 (line)]] | alt | 130 | 2 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.365× (z -16.0) |
| [[A-427 (line)]] | wt | 249 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.408× (z -15.8) |
| [[C-33 A (line)]] | alt | 285 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -12.2) |
| [[CHP-212 (line)]] | wt | 286 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 254 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -28.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -21.2) |
| [[RPMI-7951 (line)]] | alt | 181 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -17.5) |
| [[SW48 (line)]] | wt | 215 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.408× (z -9.8) |
| [[HCT15 (line)]] | alt | 271 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.494× (z -10.3) |
| [[LS 180 (line)]] | wt | 166 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 279 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.508× (z -9.2) |
| [[RKO (line)]] | wt | 200 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -15.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.512× (z -8.9) |
| [[SW 1271 (line)]] | alt | 261 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.237× (z -10.3) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.238× (z -10.2) |
| [[AN3 CA (line)]] | alt | 279 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -13.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 95.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.5) |
| [[NCI-H2122 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASH1L]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[LRCH3]] | +0.67 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[RFX1]] | +0.65 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF609]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RBX1]] | +0.65 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RBM5]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PPP6R2]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[BPTF]] | +0.62 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[CUX1]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[BRAF]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[IP6K1]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PQBP1]] | +0.60 | +0.35 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03009]] | -0.64 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[CRYZ]] | -0.60 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PGAM1]] | -0.58 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PFKM]] | -0.58 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[MINPP1]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[COPS7B]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[STARD3NL]] | -0.55 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[CIPC]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[RPE]] | -0.55 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[TMED7]] | -0.53 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[PRELID3B]] | -0.53 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[FKBP1A]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.5, -13.6); signed map (-1.8, -8.8). **Vector** length 95.6, 35.9% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +12.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +16.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.0 | +11.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.8 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | -1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +0.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.9 | -14.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.4 | -8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -26.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -8.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.9 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 193 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,536,647-2,732,573 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RES4-22; previously C4orf8 |
| Matched by | ensembl_id |

**Function**, from UniProt [P78312](https://www.uniprot.org/uniprotkb/P78312) (Protein FAM193A):

> Acts as a positive regulator of p53/TP53 by interacting with p53 repressors MDM2 and MDM4 and destabilizing MDM4 which leads to enhanced p53 transcriptional activity.

**Summary**, from NCBI Gene [8603](https://www.ncbi.nlm.nih.gov/gene/8603):

> Involved in positive regulation of signal transduction by p53 class mediator. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16822) · Entrez [8603](https://www.ncbi.nlm.nih.gov/gene/8603) · UniProt [P78312](https://www.uniprot.org/uniprotkb/P78312) · Ensembl [ENSG00000125386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125386)

## Data

Gene col 4609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4609); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4609]; `tensor/DDL_lfc|DDL_z.npy` [4609]; `embed/gene_vectors.npy` [4609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4609 or target_col == 4609). Every well: [[FAM193A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM193A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
