---
symbol: "EIF2S3"
type: "gene"
col: 5113
ensembl_id: "ENSG00000130741"
name: "eukaryotic translation initiation factor 2 subunit gamma"
location: "Xp22.11"
module: 11
arm: "-"
pooled_cpm: 217.15
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# EIF2S3

*eukaryotic translation initiation factor 2 subunit gamma* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +25.0, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.45× (z +9.4, q 5e-19, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.782× (z -8.9, q 3e-16, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF3H]] (+0.66, fdr 7e-06), [[EIF3L]] (+0.61, fdr 7e-06), [[IARS1]] (+0.60, fdr 1e-05); moves opposite to [[TOPORS]] (-0.71, fdr 7e-06), [[DYNLL1]] (-0.69, fdr 7e-06), [[EID2]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +25.0 | 0e+00 | 49/49 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +21.2 | 0e+00 | 43/44 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +17.3 | 0e+00 | 45/45 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +9.4 | 5e-19 | 41/48 (C-33 A, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +8.6 | 1e-15 | 38/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +8.0 | 1e-13 | 40/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +6.2 | 6e-08 | 37/49 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +5.2 | 1e-05 | 25/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +5.0 | 3e-05 | 41/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.9 | 7e-05 | 26/50 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 7e-05 | 24/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.8 | 9e-05 | 0/50 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.002 | 32/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | 1.16× | +3.8 | 0.006 | 20/48 (NCI-H460, LS 180, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.5 | 0.019 | 26/45 (SHP-77, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.019 | 24/48 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.050 | 17/48 (C32, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.052 | 13/48 (RKO, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.052 | 17/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.052 | 13/49 (SK-MEL-2, RKO, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.081 | 3/48 (RKO, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.782×** | -8.9 | 3e-16 | 28/48 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.806×** | -5.1 | 1e-04 | 25/47 (LoVo, A549, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.841× | -4.4 | 0.002 | 21/48 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.3 | 0.002 | 23/48 (LoVo, RKO, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.843× | -4.1 | 0.004 | 20/47 (SW480, SW48, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.850× | -4.0 | 0.007 | 21/47 (A-427, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.9 | 0.009 | 20/48 (LoVo, RKO, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.5 | 0.034 | 12/48 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.771×** | -3.5 | 0.034 | 18/49 (LoVo, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.785×** | -3.2 | 0.071 | 19/48 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 234 | 5 (4 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +22.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.80× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 281 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +21.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 227 | 3 (3 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +12.2) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.468× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.625× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 312 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +22.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.79× (z +10.0) | — |
| [[SW480 (line)]] | alt | 328 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.60× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -21.3) |
| [[A-172 (line)]] | wt | 233 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.6) | — |
| [[A-427 (line)]] | wt | 270 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +22.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.62× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -15.9) |
| [[LS 180 (line)]] | wt | 174 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.46× (z +18.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -13.4) |
| [[C-33 A (line)]] | alt | 343 | 3 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.15× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 134 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 151 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +18.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 225 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.626× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 201 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +20.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 182 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +12.9) ⚠ cell-cycle shift, explains ~88% of this change | — |
| [[Panc 03.27 (line)]] | alt | 207 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +19.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.640× (z -10.6) |
| [[A498 (line)]] | wt | 239 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +18.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 267 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +18.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 136 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.627× (z -9.1) |
| [[C32 (line)]] | wt | 75.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +12.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 177 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 209 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 268 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +16.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 293 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +14.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 265 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +15.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 158 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +15.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 142 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +13.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 243 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +13.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 131 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +16.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 218 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 164 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +14.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 166 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -14.4) |
| [[PANC-1 (line)]] | alt | 186 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +19.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 120 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 155 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +13.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 367 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +15.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 238 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -13.0) |
| [[BT-474 (line)]] | alt | 237 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.68× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.583× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 157 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +15.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.610× (z -8.8) |
| [[H4 (line)]] | wt | 198 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 191 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 177 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 178 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 235 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3H]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 969 |
| [[EIF3L]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 978 |
| [[IARS1]] | +0.60 | +0.66 / +0.55 | both halves | 1e-05 | STRING 413 |
| [[MTHFD2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SNHG29]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SNHG16]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RSL24D1]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[HSPA9]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 | STRING 468 |
| [[SLC25A6]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[RPS3A]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 992 |
| [[PLEKHB2]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOPORS]] | -0.71 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[DYNLL1]] | -0.69 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[EID2]] | -0.66 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[TBCC]] | -0.65 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[KIAA1586]] | -0.62 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[NSMCE3]] | -0.60 | -0.41 / -0.69 | both halves | 4e-05 |  |
| [[MRFAP1L1]] | -0.59 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[RBX1]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.57 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[THAP1]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[FDX2]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-29.5, -27.3); signed map (-55.6, -8.7). **Vector** length 111, 35.1% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +9.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +8.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.0 | +0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +4.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.0 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.9 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.0 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.0 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.4 | +0.3 |
|  | [[Carbamazepine (drug)]] 5 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2 subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:24,054,946-24,078,810 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EIF2gamma; previously EIF2G |
| Gene groups (HGNC) | Translational GTPases |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 24 pathways, smallest: Recycling of eIF2:GDP; Cellular response to mitochondrial stress; Response of EIF2AK1 (HRI) to heme deficiency |
| Matched by | ensembl_id |

**Function**, from UniProt [P41091](https://www.uniprot.org/uniprotkb/P41091) (Eukaryotic translation initiation factor 2 subunit 3):

> Member of the eIF2 complex that functions in the early steps of protein synthesis by forming a ternary complex with GTP and initiator tRNA. This complex binds to a 40S ribosomal subunit, followed by mRNA binding to form the 43S pre-initiation complex (43S PIC) (By similarity). Junction of the 60S ribosomal subunit to form the 80S initiation complex is preceded by hydrolysis of the GTP bound to eIF2 and release of an eIF2-GDP binary complex (By similarity). In order for eIF2 to recycle and …

**Summary**, from NCBI Gene [1968](https://www.ncbi.nlm.nih.gov/gene/1968):

> The protein encoded by this gene is the largest subunit of a heterotrimeric GTP-binding protein involved in the recruitment of methionyl-tRNA(i) to the 40 S ribosomal subunit. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:3267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3267) · Entrez [1968](https://www.ncbi.nlm.nih.gov/gene/1968) · UniProt [P41091](https://www.uniprot.org/uniprotkb/P41091) · Ensembl [ENSG00000130741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130741)

## Data

Gene col 5113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5113); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5113]; `tensor/DDL_lfc|DDL_z.npy` [5113]; `embed/gene_vectors.npy` [5113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5113 or target_col == 5113). Every well: [[EIF2S3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2S3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
