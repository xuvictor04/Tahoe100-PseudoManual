---
symbol: "CHSY1"
type: "gene"
col: 5254
ensembl_id: "ENSG00000131873"
name: "chondroitin sulfate synthase 1"
location: "15q26.3"
module: 134
arm: "+"
pooled_cpm: 94.9
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# CHSY1

*chondroitin sulfate synthase 1* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +12.2, q 2e-31, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.402× (z -17.0, q 0e+00, down in 34 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.417× (z -16.3, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK2]] (+0.72, fdr 7e-06), [[POM121]] (+0.68, fdr 7e-06), [[TENT4A]] (+0.67, fdr 7e-06); moves opposite to [[C11orf58]] (-0.54, fdr 1e-05), [[ITSN2]] (-0.53, fdr 4e-05), [[LARP7]] (-0.52, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GPR155]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +12.2 | 2e-31 | 34/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +9.2 | 7e-18 | 36/48 (SNU-423, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +8.1 | 9e-14 | 37/47 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.47×** | +7.2 | 8e-11 | 30/47 (LS 180, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +5.7 | 2e-06 | 30/49 (LS 180, SW1417, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.4 | 7e-06 | 25/47 (NCI-H1573, LoVo, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +4.7 | 2e-04 | 25/47 (LoVo, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.25×** | +4.3 | 0.001 | 23/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.007 | 17/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.20×** | +3.6 | 0.020 | 17/47 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.4 | 0.027 | 18/47 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.13× | +3.4 | 0.027 | 5/47 (RPMI-7951, Panc 03.27, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.4 | 0.032 | 13/36 (SW 900, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.078 | 12/47 (HOP62, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.080 | 15/47 (SNU-423, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 1.12× | +3.0 | 0.080 | 2/48 (A549, C32) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.080 | 12/47 (SW 900, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.096 | 9/47 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.402×** | -17.0 | 0e+00 | 34/42 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.417×** | -16.3 | 0e+00 | 42/47 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.453×** | -15.4 | 0e+00 | 44/48 (C-33 A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -14.1 | 7e-43 | 37/47 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.494×** | -12.7 | 1e-34 | 35/44 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -10.4 | 3e-23 | 34/47 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -7.7 | 9e-13 | 34/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.713×** | -6.3 | 2e-08 | 28/46 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.763×** | -5.3 | 8e-06 | 25/47 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.785×** | -4.7 | 1e-04 | 25/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.789×** | -4.4 | 5e-04 | 22/46 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -4.3 | 9e-04 | 1/49 (NCI-H23) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.692×** | -3.7 | 0.008 | 20/46 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.5 | 0.016 | 21/47 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.836× | -3.5 | 0.018 | 21/47 (H4, NCI-H1792, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.884× | -3.4 | 0.024 | 8/47 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.846× | -3.3 | 0.038 | 16/47 (KATO III, SNU-423, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.847× | -3.2 | 0.043 | 13/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.850× | -3.2 | 0.044 | 15/47 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.856× | -3.0 | 0.068 | 14/47 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.857× | -3.0 | 0.071 | 16/47 (KATO III, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 604 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -27.6) |
| [[LOX-IMVI (line)]] | wt | 189 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -21.9) |
| [[NCI-H460 (line)]] | wt | 73.2 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.193× (z -17.4) |
| [[NCI-H2030 (line)]] | alt | 89.1 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.72× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.3) |
| [[PANC-1 (line)]] | alt | 109 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.442× (z -16.1) |
| [[RPMI-7951 (line)]] | alt | 244 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.166× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 153 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.4) |
| [[HOP62 (line)]] | alt | 253 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.357× (z -15.1) |
| [[Hs 766T (line)]] | wt | 96.2 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.337× (z -14.7) |
| [[LoVo (line)]] | wt | 67.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +19.7) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -14.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -15.2) |
| [[SW 900 (line)]] | alt | 119 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0776× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -9.7) |
| [[A-427 (line)]] | wt | 42.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -19.7) |
| [[C-33 A (line)]] | alt | 181 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0213× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 183 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.314× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 43.1 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.305× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.6) |
| [[SNU-1 (line)]] | wt | 143 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -15.8) |
| [[A-172 (line)]] | wt | 100 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.45× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.507× (z -8.8) |
| [[H4 (line)]] | wt | 103 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0988× (z -19.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 60.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -16.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 52.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 49.0 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.286× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.309× (z -10.6) |
| [[SNU-423 (line)]] | alt | 74.3 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 9.51× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.2) |
| [[A549 (line)]] | wt | 75.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.337× (z -8.9) |
| [[BT-474 (line)]] | alt | 72.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -13.2) |
| [[HCT15 (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -14.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 94.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.2) |
| [[J82 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.341× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 56.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 107 | 0 | 2 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0876× (z -9.3) |
| [[SW1417 (line)]] | alt | 47.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +14.5) | — |
| [[A498 (line)]] | wt | 44.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 30.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +13.4) | — |
| [[KATO III (line)]] | alt | 63.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.9) | — |
| [[RKO (line)]] | wt | 61.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.374× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 96.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -11.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 33.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK2]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[POM121]] | +0.68 | +0.63 / +0.72 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[TENT4A]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[USP37]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RNF126]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PDXP]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[VLDLR]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[UBE2O]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[HK1]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[ALKBH5]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SMAP2]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ITSN2]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[LARP7]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ATXN7L1]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR155]] | B | GPR155 activity raises CHSY1's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 2.47× lower at baseline in the lines without GPR155 | 0.007 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[TMEM145]] | B | TMEM145 activity raises CHSY1's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without TMEM145 | 0.046 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[CLEC2B]] | B | CLEC2B activity raises CHSY1's level | lines that do not express CLEC2B (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without CLEC2B | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, TMEM158, FRMD4A |
| [[APLN]] | B | APLN activity raises CHSY1's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without APLN | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC03047]] | B | LINC03047 activity raises CHSY1's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without LINC03047 | 0.054 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |
| [[PLOD2]] | B | PLOD2 activity raises CHSY1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.60× lower at baseline in the lines without PLOD2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises CHSY1's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without KDM2B-DT | 0.081 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.4, -17.6); signed map (-40.0, 23.4). **Vector** length 137, 42.7% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +12.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.3 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.8 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +8.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.8 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.9 | -16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.2 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -7.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.4 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | chondroitin sulfate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:101,175,727-101,252,048 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0990, CSS1 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases; Beta 3-glycosyltransferases |
| Reactome | 8 pathways, smallest: Defective CHSY1 causes TPBS; CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X52](https://www.uniprot.org/uniprotkb/Q86X52) (Chondroitin sulfate synthase 1):

> Catalytic component of CHSY1-CHPF2 and CHSY1-CHPF chondroitin sulfate synthase complexes. Has both beta-1,3-glucuronic acid and beta-1,4-N-acetylgalactosamine transferase activity. Transfers glucuronic acid (GlcUA) from UDP-GlcUA and N-acetylgalactosamine (GalNAc) from UDP-GalNAc to the non-reducing end of the elongating chondroitin polymer. Involved in the negative control of osteogenesis likely through the modulation of NOTCH signaling.

**Summary**, from NCBI Gene [22856](https://www.ncbi.nlm.nih.gov/gene/22856):

> This gene encodes a member of the chondroitin N-acetylgalactosaminyltransferase family. These enzymes possess dual glucuronyltransferase and galactosaminyltransferase activity and play critical roles in the biosynthesis of chondroitin sulfate, a glycosaminoglycan involved in many biological processes including cell proliferation and morphogenesis. Decreased expression of this gene may play a role in colorectal cancer, and mutations in this gene are a cause of temtamy preaxial brachydactyly …

**Accessions** — [HGNC:17198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17198) · Entrez [22856](https://www.ncbi.nlm.nih.gov/gene/22856) · UniProt [Q86X52](https://www.uniprot.org/uniprotkb/Q86X52) · Ensembl [ENSG00000131873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131873)

## Data

Gene col 5254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5254); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5254]; `tensor/DDL_lfc|DDL_z.npy` [5254]; `embed/gene_vectors.npy` [5254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5254 or target_col == 5254). Every well: [[CHSY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHSY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
