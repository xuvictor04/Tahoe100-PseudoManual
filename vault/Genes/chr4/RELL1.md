---
symbol: "RELL1"
type: "gene"
col: 11216
ensembl_id: "ENSG00000181826"
name: "RELT like 1"
location: "4p14"
module: 64
arm: "-"
pooled_cpm: 52.45
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# RELL1

*RELT like 1* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +18.4, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.03× (z +17.6, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.346× (z -13.9, q 5e-41, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN10]] (+0.58, fdr 1e-05), [[SRGAP2]] (+0.55, fdr 3e-05), [[GRK6]] (+0.54, fdr 4e-05); moves opposite to [[ZNF780B]] (-0.64, fdr 1e-05), [[CLUAP1]] (-0.62, fdr 1e-05), [[NUDT9]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IL1RAP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.09×** | +18.4 | 0e+00 | 45/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +17.6 | 0e+00 | 44/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.95×** | +16.6 | 0e+00 | 42/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +13.5 | 2e-39 | 31/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +10.9 | 2e-25 | 31/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +10.1 | 5e-22 | 39/48 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.43×** | +8.6 | 5e-16 | 29/49 (NCI-H460, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +7.6 | 1e-12 | 35/49 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.32×** | +6.6 | 3e-09 | 28/48 (C32, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +5.4 | 5e-06 | 21/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.47×** | +5.1 | 2e-05 | 20/48 (SW480, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.21×** | +4.8 | 7e-05 | 18/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +4.3 | 6e-04 | 18/49 (Panc 03.27, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.19× | +4.2 | 9e-04 | 15/48 (HT-29, SW480, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.002 | 17/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 13/48 (CFPAC-1, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -13.9 | 5e-41 | 39/49 (HOP62, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.419×** | -11.4 | 1e-27 | 36/48 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.768×** | -6.6 | 7e-09 | 26/48 (SNU-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -6.4 | 2e-08 | 26/48 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.782×** | -6.2 | 8e-08 | 25/48 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.841× | -6.1 | 8e-08 | 23/48 (H4, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -5.8 | 4e-07 | 25/48 (HepG2/C3A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.791×** | -5.6 | 1e-06 | 26/48 (HOP62, LoVo, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.791×** | -5.6 | 2e-06 | 24/48 (HepG2/C3A, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.775×** | -4.8 | 8e-05 | 19/44 (RKO, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.828×** | -4.7 | 1e-04 | 21/48 (HepG2/C3A, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.837× | -4.5 | 4e-04 | 20/48 (HS-578T, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.841× | -4.3 | 6e-04 | 15/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.852× | -4.0 | 0.002 | 16/47 (Panc 03.27, NCI-H1573, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.852× | -4.0 | 0.002 | 21/48 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.855× | -3.9 | 0.003 | 14/47 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.834× | -3.3 | 0.033 | 13/49 (HOP62, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.874× | -3.2 | 0.033 | 14/49 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.885× | -3.1 | 0.056 | 8/48 (SW48, CFPAC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.064 | 10/47 (HCT15, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 195 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.159× (z -16.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.223× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 39.5 | 4 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 64.3 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.89× (z +9.4) | [[Docetaxel (drug)]] 0.05 µM 0.220× (z -13.4) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 31.4 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +13.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.09× (z +12.8) | — |
| [[A498 (line)]] | wt | 81.0 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 1.95× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.86× (z +8.7) | [[TAK-901 (drug)]] 5 µM 0.296× (z -8.9) |
| [[HOP62 (line)]] | alt | 71.8 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.149× (z -12.6) |
| [[LS 180 (line)]] | wt | 35.8 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.78× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.01× (z +9.9) | [[PH-797804 (drug)]] 5 µM 0.149× (z -10.0) |
| [[SW480 (line)]] | alt | 24.5 | 4 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.75× (z +10.5) | — |
| [[KATO III (line)]] | alt | 61.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.169× (z -9.3) |
| [[RKO (line)]] | wt | 53.2 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.8) | [[TAK-901 (drug)]] 5 µM 0.0913× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.87× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 45.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.66× (z +9.4) | — |
| [[A-427 (line)]] | wt | 41.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 53.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 43.5 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.71× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 43.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.94× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 56.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 36.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.63× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 82.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.17× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 68.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 88.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.12× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 55.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.30× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 53.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.5) | — |
| [[H4 (line)]] | wt | 91.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -11.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 48.0 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 58.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.279× (z -8.6) |
| [[AN3 CA (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*21 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN10]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SRGAP2]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[GRK6]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[LPIN2]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[EHD4]] | +0.53 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[ZCCHC24]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[DIAPH1]] | +0.53 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[SRGAP2B]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[POC1A]] | +0.50 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[PAQR4]] | +0.50 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[SRGAP2C]] | +0.50 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[QSOX1]] | +0.49 | +0.45 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*79 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF780B]] | -0.64 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[CLUAP1]] | -0.62 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[NUDT9]] | -0.61 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ZNF383]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ZNF573]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PGGT1B]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[CUL5]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[RBM41]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[LINC00665]] | -0.58 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[RPRD2]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[HIKESHI]] | -0.57 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TCTN1]] | -0.57 | -0.42 / -0.59 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1RAP]] | B | IL1RAP activity raises RELL1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without IL1RAP | 0.011 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[TOP2A]] | B | TOP2A activity lowers RELL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **-** arm (projection on the module's main direction -0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-42.6, 14.0); signed map (-51.7, -25.3). **Vector** length 111, 28.6% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.5 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +17.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.3 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.1 | +16.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +10.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +7.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.6 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.5 | -11.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -7.5 | -6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.4 | -13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.6 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -6.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.7 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | RELT like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:37,590,800-37,686,376 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RELT family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUW5](https://www.uniprot.org/uniprotkb/Q8IUW5) (RELT-like protein 1):

> Induces activation of MAPK14/p38 cascade, when overexpressed. Induces apoptosis, when overexpressed.

**Summary**, from NCBI Gene [768211](https://www.ncbi.nlm.nih.gov/gene/768211):

> Involved in positive regulation of p38MAPK cascade. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27379) · Entrez [768211](https://www.ncbi.nlm.nih.gov/gene/768211) · UniProt [Q8IUW5](https://www.uniprot.org/uniprotkb/Q8IUW5) · Ensembl [ENSG00000181826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181826)

## Data

Gene col 11216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11216); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11216]; `tensor/DDL_lfc|DDL_z.npy` [11216]; `embed/gene_vectors.npy` [11216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11216 or target_col == 11216). Every well: [[RELL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RELL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
