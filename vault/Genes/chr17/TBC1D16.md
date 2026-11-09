---
symbol: "TBC1D16"
type: "gene"
col: 9448
ensembl_id: "ENSG00000167291"
name: "TBC1 domain family member 16"
location: "17q25.3"
module: 97
arm: "+"
pooled_cpm: 51.79
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# TBC1D16

*TBC1 domain family member 16* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 3.84× (z +27.8, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.428× (z -16.8, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDLRAD3]] (+0.65, fdr 7e-06), [[ERGIC1]] (+0.64, fdr 1e-05), [[ST6GALNAC4]] (+0.63, fdr 5e-05); moves opposite to [[LINC02100]] (-0.68, fdr 1e-05), [[C3orf38]] (-0.63, fdr 3e-05), [[MIR181A2HG]] (-0.62, fdr 6e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.84×** | +27.8 | 0e+00 | 47/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.26×** | +24.4 | 0e+00 | 46/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.92×** | +22.2 | 0e+00 | 47/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +10.1 | 8e-22 | 39/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +8.5 | 2e-15 | 34/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +7.4 | 1e-11 | 37/47 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +6.3 | 2e-08 | 31/47 (KATO III, NCI-H2347, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.62×** | +5.2 | 1e-05 | 27/46 (KATO III, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +5.1 | 2e-05 | 24/47 (A498, A-172, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +5.1 | 2e-05 | 25/47 (A498, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.5 | 3e-04 | 16/47 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.8 | 0.006 | 9/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.7 | 0.010 | 17/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.046 | 5/47 (HS-578T, SW 900, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.060 | 19/46 (A498, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.0 | 0.075 | 17/47 (A498, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.428×** | -16.8 | 0e+00 | 40/47 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.534×** | -12.9 | 1e-35 | 39/47 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.541×** | -12.6 | 2e-34 | 39/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -12.1 | 1e-31 | 37/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -10.8 | 6e-25 | 44/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.385×** | -10.3 | 9e-23 | 36/47 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.634×** | -9.4 | 7e-19 | 30/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.645×** | -9.0 | 1e-17 | 33/47 (PANC-1, A-427, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -7.9 | 2e-13 | 33/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -7.0 | 1e-10 | 27/47 (SW48, A-172, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.824×** | -5.6 | 1e-06 | 25/47 (A-427, PANC-1, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.774×** | -5.0 | 2e-05 | 25/46 (LoVo, NCI-H23, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.0 | 0.003 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -4.0 | 0.003 | 15/47 (KATO III, J82, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.811×** | -4.0 | 0.003 | 20/46 (NCI-H460, NCI-H661, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.833×** | -3.7 | 0.007 | 19/47 (HT-29, KATO III, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.889× | -3.4 | 0.024 | 14/47 (A-427, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 48.3 | 14 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +15.8) | — |
| [[KATO III (line)]] | alt | 135 | 6 (3 ⚠) | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.45× (z +19.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.410× (z -11.7) |
| [[HT-29 (line)]] | alt | 77.4 | 3 | 8 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.53× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -11.5) |
| [[PANC-1 (line)]] | alt | 55.0 | 3 | 8 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.75× (z +18.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -15.5) |
| [[SW480 (line)]] | alt | 72.8 | 3 | 8 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +15.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -17.6) |
| [[LS 180 (line)]] | wt | 62.4 | 3 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +14.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.345× (z -11.5) |
| [[A549 (line)]] | wt | 44.7 | 4 (1 ⚠) | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.77× (z +15.0) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.235× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 37.3 | 3 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.69× (z +16.6) | [[Digitoxin (drug)]] 5 µM 0.203× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.250× (z -14.8) |
| [[LoVo (line)]] | wt | 66.3 | 1 | 7 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +10.2) | [[Harringtonine (drug)]] 5 µM 0.190× (z -18.3) |
| [[A-427 (line)]] | wt | 50.1 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -25.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0889× (z -24.9) |
| [[SHP-77 (line)]] | alt | 93.9 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.315× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -10.0) |
| [[A-172 (line)]] | wt | 54.9 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.66× (z +16.2) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.358× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 19.2 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 6.57× (z +15.3) | [[Harringtonine (drug)]] 0.5 µM 0.316× (z -9.3) |
| [[HOP62 (line)]] | alt | 57.1 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +13.6) | [[PH-797804 (drug)]] 5 µM 0.149× (z -10.1) |
| [[J82 (line)]] | alt | 52.9 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +11.3) | [[Harringtonine (drug)]] 5 µM 0.247× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 43.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +20.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 5.03× (z +13.0) | — |
| [[RKO (line)]] | wt | 48.9 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +8.5) | [[Harringtonine (drug)]] 0.5 µM 0.222× (z -13.0) |
| [[SW1417 (line)]] | alt | 45.0 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.46× (z +13.9) | [[Digitoxin (drug)]] 5 µM 0.347× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -8.9) |
| [[COLO 205 (line)]] | alt | 75.2 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.46× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.221× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -11.8) |
| [[HS-578T (line)]] | alt | 41.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.68× (z +13.3) | [[Harringtonine (drug)]] 5 µM 0.355× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 60.6 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 4.67× (z +10.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 42.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.02× (z +13.0) | [[Harringtonine (drug)]] 5 µM 0.352× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 67.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.57× (z +14.1) | [[Harringtonine (drug)]] 5 µM 0.409× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 53.3 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +10.1) | [[Harringtonine (drug)]] 5 µM 0.191× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 55.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.396× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 17.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.39× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 52.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 27.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.88× (z +14.1) | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.71× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.39× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 52.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.47× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 42.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.63× (z +11.3) | — |
| [[H4 (line)]] | wt | 62.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.99× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 46.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0871× (z -8.5) |
| [[SW48 (line)]] | wt | 56.9 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.222× (z -10.1) |
| [[AN3 CA (line)]] | alt | 72.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0914× (z -12.8) |
| [[BT-474 (line)]] | alt | 60.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 61.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.345× (z -9.3) |
| [[CHP-212 (line)]] | wt | 106 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.73× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 47.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 96.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.66× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | — |
| [[CFPAC-1 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDLRAD3]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ERGIC1]] | +0.64 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.63 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[LMBR1]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.61 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RPS6KA2]] | +0.61 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ST6GALNAC6]] | +0.61 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[TCF3]] | +0.60 | +0.37 / +0.50 | both halves | 7e-05 |  |
| [[SKI]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MLXIP]] | +0.57 | +0.40 / +0.44 | both halves | 4e-05 |  |
| [[TRABD]] | +0.57 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[FBRSL1]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02100]] | -0.68 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[C3orf38]] | -0.63 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MIR181A2HG]] | -0.62 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[MR1]] | -0.61 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[RBM43]] | -0.59 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[EFCAB5]] | -0.59 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[BTN3A3]] | -0.59 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PATL2]] | -0.58 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[AHI1-DT]] | -0.58 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[TLR1]] | -0.57 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[FAM111A-DT]] | -0.57 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[PLEKHF2]] | -0.56 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TBC1D16's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.3, 10.7); signed map (-19.1, 43.2). **Vector** length 103, 29.2% of its response variance represented; |z| ≥ 3 in 1,382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.9 | +22.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +27.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +24.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +10.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | +5.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.1 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.0 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.7 | -12.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -16.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.0 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:79,932,343-80,035,872 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC25062, FLJ20748 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBP0](https://www.uniprot.org/uniprotkb/Q8TBP0) (TBC1 domain family member 16):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [125058](https://www.ncbi.nlm.nih.gov/gene/125058):

> Enables GTPase activator activity. Involved in regulation of receptor recycling. Located in cytosol and early endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28356) · Entrez [125058](https://www.ncbi.nlm.nih.gov/gene/125058) · UniProt [Q8TBP0](https://www.uniprot.org/uniprotkb/Q8TBP0) · Ensembl [ENSG00000167291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167291)

## Data

Gene col 9448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9448); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9448]; `tensor/DDL_lfc|DDL_z.npy` [9448]; `embed/gene_vectors.npy` [9448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9448 or target_col == 9448). Every well: [[TBC1D16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
