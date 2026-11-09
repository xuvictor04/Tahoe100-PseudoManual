---
symbol: "CAMSAP2"
type: "gene"
col: 3971
ensembl_id: "ENSG00000118200"
name: "calmodulin regulated spectrin associated protein family member 2"
location: "1q32.1"
module: 202
arm: "+"
pooled_cpm: 205.3
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# CAMSAP2

*calmodulin regulated spectrin associated protein family member 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.71× (z +25.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.706× (z -11.3, q 5e-27, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.737× (z -10.3, q 2e-22, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 7 lines (SNU-423 0.453×, HOP62 0.471×, NCI-H2347 0.521×, NCI-H1792 0.507×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.402×, SW 900 0.425×, HCT15 0.309×, C-33 A 0.413×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.579×, NCI-H1792 0.526×; ⚠ cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.648×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MZF1-AS1]] (+0.58, fdr 2e-04), [[IPO9-AS1]] (+0.57, fdr 1e-04), [[NR2F1-AS1]] (+0.57, fdr 9e-05); moves opposite to [[SEPTIN7P14]] (-0.59, fdr 2e-05), [[ANAPC5]] (-0.57, fdr 4e-05), [[RPA1]] (-0.55, fdr 8e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FOXD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +25.7 | 0e+00 | 45/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +15.0 | 0e+00 | 41/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +12.9 | 1e-35 | 41/48 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +9.7 | 3e-20 | 37/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +9.3 | 2e-18 | 33/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +8.9 | 8e-17 | 28/48 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +7.8 | 4e-13 | 26/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +7.6 | 3e-12 | 27/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +6.7 | 1e-09 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +6.7 | 1e-09 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +5.6 | 9e-07 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.13× | +4.1 | 0.002 | 10/47 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +4.0 | 0.002 | 12/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.13× | +3.8 | 0.005 | 17/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.08× | +3.8 | 0.005 | 11/48 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.010 | 18/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3971.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 7 lines (SNU-423 0.453×, HOP62 0.471×, NCI-H2347 0.521×, NCI-H1792 0.507×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.402×, SW 900 0.425×, HCT15 0.309×, C-33 A 0.413×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.579×, NCI-H1792 0.526×; ⚠ cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.648×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -11.3 | 5e-27 | 32/44 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.737×** | -10.3 | 2e-22 | 30/48 (SNU-423, HOP62, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.760×** | -9.3 | 2e-18 | 31/49 (C32, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.771×** | -8.8 | 2e-16 | 26/48 (SNU-423, HOP62, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.756×** | -7.5 | 1e-11 | 33/45 (C32, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.803×** | -7.4 | 1e-11 | 25/48 (HOP62, SNU-423, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -6.8 | 8e-10 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.891× | -5.5 | 3e-06 | 7/48 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | 0.850× | -5.5 | 3e-06 | 20/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 0.870× | -4.7 | 1e-04 | 15/48 (NCI-H23, AN3 CA, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.880× | -4.3 | 8e-04 | 13/48 (KATO III, AN3 CA, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.888× | -3.8 | 0.006 | 10/49 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.814×** | -3.6 | 0.012 | 17/47 (HepG2/C3A, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.815×** | -3.6 | 0.012 | 17/38 (HS-578T, C32, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.864× | -3.5 | 0.016 | 15/47 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.866× | -3.5 | 0.018 | 14/48 (NCI-H460, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.882× | -3.0 | 0.081 | 12/48 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 277 | 13 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +27.7) | [[Dinaciclib (drug)]] 0.5 µM 0.652× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 413 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +20.2) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 239 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.521× (z -12.4) |
| [[A-172 (line)]] | wt | 349 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +22.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.648× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 229 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +25.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.565× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 236 | 6 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 6.35× (z +19.6) | [[Panobinostat (drug)]] 0.5 µM 0.635× (z -9.3) |
| [[COLO 205 (line)]] | alt | 146 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 190 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.501× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 296 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -14.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 232 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +29.5) | — |
| [[HOP62 (line)]] | alt | 231 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.471× (z -13.1) |
| [[HS-578T (line)]] | alt | 154 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +16.6) | [[Panobinostat (drug)]] 0.5 µM 0.533× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 255 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.99× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.507× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 187 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +23.2) | — |
| [[A-427 (line)]] | wt | 238 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -15.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 252 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 214 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +22.8) | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -14.0) |
| [[A549 (line)]] | wt | 166 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +19.0) | — |
| [[CFPAC-1 (line)]] | alt | 165 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +14.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.550× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 138 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 227 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 2.63× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.585× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 142 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 3.43× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 134 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +27.4) | — |
| [[RKO (line)]] | wt | 271 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 226 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.93× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -12.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 230 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 212 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -14.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +15.5) | — |
| [[LoVo (line)]] | wt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 217 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.7) | — |
| [[AN3 CA (line)]] | alt | 235 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -9.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 289 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.384× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 244 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +15.0) | — |
| [[hTERT-HPNE (line)]] | wt | 195 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.2) | — |
| [[J82 (line)]] | alt | 179 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +14.2) | — |
| [[KATO III (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 186 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.70× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 142 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +16.1) | — |
| [[AsPC-1 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 124 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZF1-AS1]] | +0.58 | +0.52 / +0.32 | both halves | 2e-04 |  |
| [[IPO9-AS1]] | +0.57 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[NR2F1-AS1]] | +0.57 | +0.56 / +0.36 | both halves | 9e-05 |  |
| [[HECTD2]] | +0.56 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[TRPC1]] | +0.56 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[DLGAP4-AS1]] | +0.55 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[ZFPM2]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[FAM131B-AS2]] | +0.54 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[GRK4]] | +0.54 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[EID2]] | +0.54 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[ITPRIPL2]] | +0.53 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[GGPS1]] | +0.53 | +0.46 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN7P14]] | -0.59 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ANAPC5]] | -0.57 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[RPA1]] | -0.55 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[IFT172]] | -0.55 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[NUDT21]] | -0.55 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[PMS2P3-1]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[GUSBP1]] | -0.52 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[MSTO2P]] | -0.51 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[ANAPC4]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[NOMO2]] | -0.51 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[MARF1]] | -0.50 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[GPR107]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXD1]] | B | FOXD1 activity raises CAMSAP2's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without FOXD1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |
| [[HDAC6]] | B | HDAC6 activity raises CAMSAP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.3, 7.6); signed map (26.5, 8.9). **Vector** length 105, 29.3% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +25.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +0.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.3 | +1.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.8 | -10.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.7 | -8.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.9 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.8 | -7.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.6 | -3.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | +0.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.0 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin regulated spectrin associated protein family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:200,738,893-200,860,704 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1078; previously CAMSAP1L1 |
| Gene groups (HGNC) | CAMSAP family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08AD1](https://www.uniprot.org/uniprotkb/Q08AD1) (Calmodulin-regulated spectrin-associated protein 2):

> Key microtubule-organizing protein that specifically binds the minus-end of non-centrosomal microtubules and regulates their dynamics and organization. Specifically recognizes growing microtubule minus-ends and autonomously decorates and stabilizes microtubule lattice formed by microtubule minus-end polymerization. Acts on free microtubule minus-ends that are not capped by microtubule-nucleating proteins or other factors and protects microtubule minus-ends from depolymerization. In addition, it …

**Summary**, from NCBI Gene [23271](https://www.ncbi.nlm.nih.gov/gene/23271):

> Enables microtubule minus-end binding activity. Involved in several processes, including regulation of Golgi organization; regulation of dendrite development; and regulation of microtubule polymerization. Located in Golgi apparatus; centrosome; and microtubule minus-end. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29188) · Entrez [23271](https://www.ncbi.nlm.nih.gov/gene/23271) · UniProt [Q08AD1](https://www.uniprot.org/uniprotkb/Q08AD1) · Ensembl [ENSG00000118200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118200)

## Data

Gene col 3971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3971); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3971]; `tensor/DDL_lfc|DDL_z.npy` [3971]; `embed/gene_vectors.npy` [3971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3971 or target_col == 3971). Every well: [[CAMSAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMSAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
