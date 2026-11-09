---
symbol: "SMCHD1"
type: "gene"
col: 2156
ensembl_id: "ENSG00000101596"
name: "structural maintenance of chromosomes flexible hinge domain containing 1"
location: "18p11.32"
module: 22
arm: "+"
pooled_cpm: 267.55
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SMCHD1

*structural maintenance of chromosomes flexible hinge domain containing 1* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +19.6, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.587× (z -13.5, q 1e-38, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.778× (z -6.4, q 2e-08, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 0.332×, LS 180 0.299×, NCI-H23 0.358×, SNU-1 0.297×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW 900 0.337×, RKO 0.365×, COLO 205 0.323×, HEC-1-A 0.471×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (LoVo 0.459×, NCI-H2347 0.500×, MIA PaCa-2 0.494×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMNN]] (+0.64, fdr 1e-05), [[SYNE2]] (+0.60, fdr 7e-06), [[BARD1]] (+0.59, fdr 1e-05); moves opposite to [[GMIP]] (-0.55, fdr 2e-05), [[ZNF778]] (-0.54, fdr 1e-04), [[FRMD6-AS2]] (-0.53, fdr 7e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +19.6 | 0e+00 | 43/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +14.8 | 0e+00 | 46/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +12.0 | 5e-31 | 40/48 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +9.9 | 7e-21 | 39/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +8.9 | 5e-17 | 40/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +8.8 | 2e-16 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +8.6 | 5e-16 | 38/47 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.27×** | +5.9 | 2e-07 | 29/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +5.4 | 3e-06 | 29/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.21×** | +4.9 | 6e-05 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.21×** | +4.8 | 7e-05 | 25/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.21×** | +4.8 | 7e-05 | 23/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.004 | 25/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.005 | 27/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.032 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2156.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 0.332×, LS 180 0.299×, NCI-H23 0.358×, SNU-1 0.297×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW 900 0.337×, RKO 0.365×, COLO 205 0.323×, HEC-1-A 0.471×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (LoVo 0.459×, NCI-H2347 0.500×, MIA PaCa-2 0.494×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.587×** | -13.5 | 1e-38 | 43/49 (SW 900, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.580×** | -13.2 | 2e-37 | 43/44 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.817×** | -7.2 | 1e-10 | 23/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -7.1 | 2e-10 | 38/47 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.749×** | -6.4 | 2e-08 | 31/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -6.4 | 2e-08 | 31/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -5.6 | 2e-06 | 25/49 (A549, HCT15, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.852× | -4.1 | 0.003 | 19/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.863× | -3.7 | 0.012 | 18/48 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.873× | -3.4 | 0.033 | 14/47 (HT-29, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.037 | 23/48 (HEC-1-A, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.912× | -3.3 | 0.041 | 7/48 (A-172, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.862× | -3.3 | 0.041 | 16/47 (C32, SW 900, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 200 | 10 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.620× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 285 | 5 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 456 | 5 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -11.7) |
| [[LS 180 (line)]] | wt | 288 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -16.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 284 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.489× (z -13.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 296 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +24.4) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -19.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 372 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.477× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 285 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -10.6) |
| [[PANC-1 (line)]] | alt | 197 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +27.4) | — |
| [[BT-474 (line)]] | alt | 362 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +24.5) | — |
| [[HT-29 (line)]] | alt | 328 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.504× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 304 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -14.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 225 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 303 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 398 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.494× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 175 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 347 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 276 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.450× (z -11.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 178 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 218 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +17.9) | — |
| [[HCT15 (line)]] | alt | 343 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 543 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -16.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 501 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.509× (z -15.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[AsPC-1 (line)]] | alt | 248 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +19.7) | — |
| [[COLO 205 (line)]] | alt | 230 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -14.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 290 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 206 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 212 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -14.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 299 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.6) | — |
| [[A-172 (line)]] | wt | 230 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.568× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 323 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -12.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 393 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 84.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.3) | — |
| [[H4 (line)]] | wt | 214 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.425× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 226 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.514× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 202 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 162 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 330 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.520× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 265 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -16.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 255 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 192 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 442 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 211 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMNN]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SYNE2]] | +0.60 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[BARD1]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[DEK]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[MIR924HG]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PHIP]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 | STRING 570 |
| [[CDK1]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PSIP1]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CTDSPL2]] | +0.57 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[EZH2]] | +0.57 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SCLT1]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[LINC01572]] | +0.57 | +0.41 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMIP]] | -0.55 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[ZNF778]] | -0.54 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[FRMD6-AS2]] | -0.53 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[DCTN5]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[KCTD10]] | -0.50 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[EAF1]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[LTO1]] | -0.48 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[GPN2]] | -0.48 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[SH3BP5L]] | -0.47 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[EIF3I]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.488). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.8, -52.4); signed map (-46.8, -47.0). **Vector** length 107, 37.3% of its response variance represented; |z| ≥ 3 in 1,200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.3 | +8.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | -1.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -1.8 |
|  | [[Thymol (drug)]] 5 µM |  | +2.3 | -1.3 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | -0.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +0.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | -0.5 |
|  | [[Busulfan (drug)]] 5 µM |  | +2.0 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -7.7 | -7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.5 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +3.9 |

## What is on record

|  |  |
|---|---|
| Name | structural maintenance of chromosomes flexible hinge domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:2,655,726-2,805,017 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0650, FSHD2 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NHR9](https://www.uniprot.org/uniprotkb/A6NHR9) (Structural maintenance of chromosomes flexible hinge domain-containing protein 1):

> Non-canonical member of the structural maintenance of chromosomes (SMC) protein family that plays a key role in epigenetic silencing by regulating chromatin architecture (By similarity). Promotes heterochromatin formation in both autosomes and chromosome X, probably by mediating the merge of chromatin compartments (By similarity). Plays a key role in chromosome X inactivation in females by promoting the spreading of heterochromatin. Recruited to inactivated chromosome X by Xist RNA and acts by …

**Summary**, from NCBI Gene [23347](https://www.ncbi.nlm.nih.gov/gene/23347):

> This gene encodes a protein which contains a hinge region domain found in members of the SMC (structural maintenance of chromosomes) protein family. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:29090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29090) · Entrez [23347](https://www.ncbi.nlm.nih.gov/gene/23347) · UniProt [A6NHR9](https://www.uniprot.org/uniprotkb/A6NHR9) · Ensembl [ENSG00000101596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101596)

## Data

Gene col 2156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2156); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2156]; `tensor/DDL_lfc|DDL_z.npy` [2156]; `embed/gene_vectors.npy` [2156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2156 or target_col == 2156). Every well: [[SMCHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMCHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
