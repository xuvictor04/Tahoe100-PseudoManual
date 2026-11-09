---
symbol: "TNRC6A"
type: "gene"
col: 1642
ensembl_id: "ENSG00000090905"
name: "trinucleotide repeat containing adaptor 6A"
location: "16p12.1"
module: 146
arm: "+"
pooled_cpm: 193.33
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# TNRC6A

*trinucleotide repeat containing adaptor 6A* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.35× (z +13.7, q 6e-40, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.501× (z -17.2, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.683× (z -13.9, q 1e-41, down in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (C32 0.391×, A-172 0.432×, A498 0.475×, NCI-H460 0.568×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.312×, SNU-1 0.241×, Hs 766T 0.321×, NCI-H460 0.446×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.309×, NCI-H1573 0.446×, hTERT-HPNE 0.418×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD3]] (+0.67, fdr 7e-06), [[ZFP14]] (+0.67, fdr 9e-06), [[MRPL22]] (+0.66, fdr 7e-06); moves opposite to [[NIPAL1]] (-0.63, fdr 7e-06), [[RIPK1]] (-0.62, fdr 8e-06), [[SOWAHC]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.35×** | +13.7 | 6e-40 | 48/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +10.9 | 2e-25 | 45/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +10.6 | 4e-24 | 36/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +9.5 | 4e-19 | 35/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +6.6 | 6e-09 | 26/48 (RKO, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +6.0 | 2e-07 | 30/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 3e-07 | 27/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.62×** | +5.5 | 3e-06 | 37/47 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +4.3 | 0.001 | 22/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.18× | +4.2 | 0.002 | 18/48 (LoVo, KATO III, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.12× | +4.1 | 0.002 | 1/48 (NCI-H661) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +4.0 | 0.003 | 7/48 (hTERT-HPNE, KATO III, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.9 | 0.005 | 13/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.8 | 0.006 | 22/48 (C-33 A, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.8 | 0.006 | 23/45 (C-33 A, RKO, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 20/48 (C32, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.021 | 11/47 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.022 | 17/48 (KATO III, SW480, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.3 | 0.026 | 15/49 (SHP-77, A-427, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.028 | 10/48 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.084 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1642.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (C32 0.391×, A-172 0.432×, A498 0.475×, NCI-H460 0.568×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.312×, SNU-1 0.241×, Hs 766T 0.321×, NCI-H460 0.446×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.309×, NCI-H1573 0.446×, hTERT-HPNE 0.418×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.501×** | -17.2 | 0e+00 | 39/44 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.562×** | -14.9 | 0e+00 | 45/49 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -13.9 | 1e-41 | 36/49 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.625×** | -11.2 | 4e-27 | 34/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.811×** | -5.2 | 2e-05 | 26/50 (C32, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.818×** | -5.0 | 5e-05 | 25/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~7% of this change | 0.846× | -4.3 | 0.001 | 21/48 (SW 1088, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.857× | -4.0 | 0.005 | 21/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | 0.878× | -3.2 | 0.081 | 16/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.887× | -3.1 | 0.11 | 10/48 (HS-578T, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 212 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 265 | 2 | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -9.3) |
| [[C32 (line)]] | wt | 224 | 1 | 7 (6 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.98× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -23.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -18.6) |
| [[A549 (line)]] | wt | 196 | 3 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.12× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -12.3) |
| [[J82 (line)]] | alt | 182 | 4 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.39× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.504× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -9.6) |
| [[KATO III (line)]] | alt | 192 | 5 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.13× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -13.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 141 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +25.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.87× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 183 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.83× (z +13.2) | — |
| [[LoVo (line)]] | wt | 178 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +20.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 218 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.17× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 208 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.48× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 246 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.74× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -17.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 164 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 197 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 174 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -15.3) |
| [[A498 (line)]] | wt | 286 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 129 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -10.4) |
| [[SNU-423 (line)]] | alt | 177 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -11.0) |
| [[SW1417 (line)]] | alt | 224 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.83× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -12.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.496× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 156 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 176 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.56× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 219 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -14.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 156 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.38× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.523× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -16.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 193 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.469× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 190 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 3.42× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 262 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.77× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -12.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 265 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -14.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 232 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.17× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 195 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.80× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -8.8) |
| [[HOP62 (line)]] | alt | 161 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 215 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -9.5) |
| [[A-172 (line)]] | wt | 211 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -18.4) |
| [[AN3 CA (line)]] | alt | 229 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -8.5) ⚠ cell-cycle shift, explains ~19% of this change |
| [[AsPC-1 (line)]] | alt | 140 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.4) |
| [[H4 (line)]] | wt | 164 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.9) |
| [[Hs 766T (line)]] | wt | 235 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -15.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 165 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.479× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -20.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 239 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -16.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ZFP14]] | +0.67 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[MRPL22]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[EHMT2]] | +0.65 | +0.63 / +0.76 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[RHOT1]] | +0.65 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[RHOXF1]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[IRAK1BP1]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[ZNF224]] | +0.64 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[C12orf76]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SLC25A12]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[RCOR3]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPAL1]] | -0.63 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[RIPK1]] | -0.62 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[SOWAHC]] | -0.58 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[HOMER1]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[STK10]] | -0.58 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[SLC4A7]] | -0.58 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[DUSP5-DT]] | -0.57 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[LINC01128]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.56 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[FSCN2]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TBILA]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TNRC6A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.9, -9.5); signed map (-27.2, -9.7). **Vector** length 124, 43.0% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +8.9 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +8.8 | +6.6 |
|  | [[NG25 (drug)]] 5 µM |  | +6.7 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +13.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +10.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +5.8 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +4.9 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -4.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.1 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.9 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | trinucleotide repeat containing adaptor 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:24,610,209-24,827,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAGH26, KIAA1460, GW182; previously TNRC6 |
| Gene groups (HGNC) | TNRC6 adaptor family |
| Reactome | 64 pathways, smallest: Post-transcriptional silencing by small RNAs; Regulation of NPAS4 mRNA translation; Regulation of CDH11 mRNA translation by microRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDV7](https://www.uniprot.org/uniprotkb/Q8NDV7) (Trinucleotide repeat-containing gene 6A protein):

> Plays a role in RNA-mediated gene silencing by both micro-RNAs (miRNAs) and short interfering RNAs (siRNAs). Required for miRNA-dependent repression of translation and for siRNA-dependent endonucleolytic cleavage of complementary mRNAs by argonaute family proteins. As a scaffolding protein, associates with argonaute proteins bound to partially complementary mRNAs, and can simultaneously recruit CCR4-NOT and PAN deadenylase complexes.

**Summary**, from NCBI Gene [27327](https://www.ncbi.nlm.nih.gov/gene/27327):

> This gene encodes a member of the trinucleotide repeat containing 6 protein family. The protein functions in post-transcriptional gene silencing through the RNA interference (RNAi) and microRNA pathways. The protein associates with messenger RNAs and Argonaute proteins in cytoplasmic bodies known as GW-bodies or P-bodies. Inhibiting expression of this gene delocalizes other GW-body proteins and impairs RNAi and microRNA-induced gene silencing. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11969) · Entrez [27327](https://www.ncbi.nlm.nih.gov/gene/27327) · UniProt [Q8NDV7](https://www.uniprot.org/uniprotkb/Q8NDV7) · Ensembl [ENSG00000090905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090905)

## Data

Gene col 1642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1642); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1642]; `tensor/DDL_lfc|DDL_z.npy` [1642]; `embed/gene_vectors.npy` [1642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1642 or target_col == 1642). Every well: [[TNRC6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNRC6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
