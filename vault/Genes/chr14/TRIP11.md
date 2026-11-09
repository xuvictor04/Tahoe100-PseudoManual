---
symbol: "TRIP11"
type: "gene"
col: 2028
ensembl_id: "ENSG00000100815"
name: "thyroid hormone receptor interactor 11"
location: "14q32.12"
module: 28
arm: "+"
pooled_cpm: 134.05
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TRIP11

*thyroid hormone receptor interactor 11* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.54× (z +28.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.482× (z -15.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSRP1]] (+0.84, fdr 7e-06), [[SNW1]] (+0.79, fdr 7e-06), [[BPTF]] (+0.79, fdr 7e-06); moves opposite to [[COLGALT1]] (-0.70, fdr 7e-06), [[PLBD2]] (-0.68, fdr 7e-06), [[MFSD14B]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.54×** | +28.4 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.70×** | +21.4 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +16.7 | 0e+00 | 47/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +14.4 | 6e-45 | 46/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.76×** | +12.2 | 6e-32 | 48/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.9 | 8e-05 | 25/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.6 | 4e-04 | 28/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +3.9 | 0.006 | 22/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.13× | +3.7 | 0.014 | 3/48 (A549, NCI-H1792, …) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.031 | 5/48 (LS 180, COLO 205, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.053 | 20/47 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | 1.10× | +3.0 | 0.12 | 2/48 (SNU-1, C-33 A) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.482×** | -15.7 | 0e+00 | 48/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -15.0 | 0e+00 | 47/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.531×** | -13.6 | 7e-40 | 47/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.514×** | -13.2 | 8e-38 | 39/45 (hTERT-HPNE, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.694×** | -7.9 | 4e-13 | 33/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.698×** | -7.7 | 1e-12 | 36/48 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -6.7 | 1e-09 | 31/48 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.732×** | -6.7 | 1e-09 | 31/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.736×** | -6.6 | 3e-09 | 29/49 (A-427, RKO, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.768×** | -5.7 | 9e-07 | 34/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -5.4 | 3e-06 | 31/48 (HT-29, HCT15, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.779×** | -5.3 | 4e-06 | 30/48 (KATO III, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | **0.794×** | -4.7 | 9e-05 | 29/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.662×** | -4.6 | 1e-04 | 23/38 (C32, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.823×** | -4.2 | 0.001 | 25/48 (hTERT-HPNE, HCT15, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.824×** | -4.2 | 0.001 | 24/49 (SW480, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.711×** | -3.8 | 0.004 | 25/49 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.792×** | -3.6 | 0.010 | 24/48 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.893× | -3.4 | 0.016 | 1/48 (COLO 205) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.897× | -3.3 | 0.025 | 7/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.870× | -2.9 | 0.087 | 11/48 (SW 900, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 131 | 5 | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +24.9) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -13.2) |
| [[LoVo (line)]] | wt | 181 | 5 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 177 | 5 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +27.2) | [[Panobinostat (drug)]] 5 µM 0.405× (z -13.3) |
| [[HCT15 (line)]] | alt | 226 | 3 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.385× (z -11.6) |
| [[KATO III (line)]] | alt | 159 | 3 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.352× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 150 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +19.3) | [[Panobinostat (drug)]] 5 µM 0.302× (z -14.5) |
| [[PANC-1 (line)]] | alt | 111 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +28.0) | [[Digitoxin (drug)]] 5 µM 0.404× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.485× (z -12.5) |
| [[RKO (line)]] | wt | 142 | 6 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.441× (z -9.8) |
| [[SW480 (line)]] | alt | 148 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +26.7) | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -14.2) |
| [[HT-29 (line)]] | alt | 108 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 129 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +19.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.446× (z -10.2) |
| [[HOP62 (line)]] | alt | 146 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +18.1) | [[Panobinostat (drug)]] 5 µM 0.401× (z -14.3) |
| [[LS 180 (line)]] | wt | 124 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.489× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 177 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -10.1) |
| [[A498 (line)]] | wt | 112 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.432× (z -10.4) |
| [[A549 (line)]] | wt | 114 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.480× (z -10.1) |
| [[C32 (line)]] | wt | 110 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +18.6) | [[Lonafarnib (drug)]] 5 µM 0.0513× (z -16.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 161 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.380× (z -9.8) |
| [[H4 (line)]] | wt | 173 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.341× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 131 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.526× (z -9.1) |
| [[HS-578T (line)]] | alt | 98.1 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.1) | [[Belinostat (drug)]] 5 µM 0.416× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 96.3 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +17.8) | [[Panobinostat (drug)]] 0.5 µM 0.477× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 123 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +19.7) | — |
| [[Panc 03.27 (line)]] | alt | 160 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.4) | [[Panobinostat (drug)]] 0.5 µM 0.518× (z -8.7) |
| [[SW48 (line)]] | wt | 141 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.331× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 95.8 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.510× (z -8.8) |
| [[A-427 (line)]] | wt | 120 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 113 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.9) | [[Lonafarnib (drug)]] 5 µM 0.0583× (z -13.6) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.371× (z -9.1) |
| [[SW 900 (line)]] | alt | 196 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.433× (z -10.0) |
| [[Hs 766T (line)]] | wt | 128 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.417× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 144 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.9) | [[Digitoxin (drug)]] 5 µM 0.382× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 137 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.5) | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 107 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -10.8) |
| [[BT-474 (line)]] | alt | 129 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +17.5) | — |
| [[C-33 A (line)]] | alt | 67.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 149 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +17.0) | — |
| [[HepG2_C3A (line)]] | wt | 114 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 275 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +19.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~56% of this change |
| [[NCI-H23 (line)]] | alt | 114 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SNU-423 (line)]] | alt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +17.4) | — |
| [[AsPC-1 (line)]] | alt | 82.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.3) | — |
| [[SHP-77 (line)]] | alt | 84.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +10.0) | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM 0.0671× (z -12.1) |
| [[CHP-212 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 171 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | +0.84 | +0.85 / +0.84 | both halves | 7e-06 |  |
| [[SNW1]] | +0.79 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[BPTF]] | +0.79 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[CEP350]] | +0.76 | +0.78 / +0.77 | both halves | 7e-06 | STRING 677 |
| [[CCDC174]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.76 | +0.82 / +0.57 | both halves | 1e-05 |  |
| [[ZNF764]] | +0.76 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[NME6]] | +0.76 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[LZIC]] | +0.75 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[THAP5]] | +0.75 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.74 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[LARP7]] | +0.74 | +0.78 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLGALT1]] | -0.70 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[PLBD2]] | -0.68 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[MFSD14B]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[HDAC1]] | -0.68 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[RPA1]] | -0.66 | -0.67 / -0.57 | both halves | 8e-06 |  |
| [[NUTF2]] | -0.66 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[SMG1P2]] | -0.66 | -0.71 / -0.60 | both halves | 7e-06 |  |
| [[NPDC1]] | -0.65 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[IGSF8]] | -0.65 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.65 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[METAP1]] | -0.65 | -0.75 / -0.46 | both halves | 3e-05 |  |
| [[ABCA2]] | -0.65 | -0.67 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.7, 7.3); signed map (5.0, -16.5). **Vector** length 162, 58.8% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +19.3 | +21.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +16.5 | +28.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +15.2 | +14.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +14.9 | +16.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +11.8 | +12.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +6.1 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +4.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.2 | -13.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.7 | -15.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.2 | -15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -13.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -6.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor interactor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:91,965,991-92,040,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEV14, Trip230, GMAP-210, GMAP210 |
| Gene groups (HGNC) | Golgins |
| Reactome | 11 pathways, smallest: Signaling by FLT3 fusion proteins; FLT3 signaling in disease; Intra-Golgi traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15643](https://www.uniprot.org/uniprotkb/Q15643) (Thyroid receptor-interacting protein 11):

> Is a membrane tether required for vesicle tethering to Golgi. Has an essential role in the maintenance of Golgi structure and function. It is required for efficient anterograde and retrograde trafficking in the early secretory pathway, functioning at both the ER-to-Golgi intermediate compartment (ERGIC) and Golgi complex. Binds the ligand binding domain of the thyroid receptor (THRB) in the presence of triiodothyronine and enhances THRB-modulated transcription.

**Summary**, from NCBI Gene [9321](https://www.ncbi.nlm.nih.gov/gene/9321):

> This gene was identified based on the interaction of its protein product with thyroid hormone receptor beta. This protein is associated with the Golgi apparatus. The N-terminal region of the protein binds Golgi membranes and the C-terminal region binds the minus ends of microtubules; thus, the protein is thought to play a role in assembly and maintenance of the Golgi ribbon structure around the centrosome. Mutations in this gene cause achondrogenesis type IA.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:12305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12305) · Entrez [9321](https://www.ncbi.nlm.nih.gov/gene/9321) · UniProt [Q15643](https://www.uniprot.org/uniprotkb/Q15643) · Ensembl [ENSG00000100815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100815)

## Data

Gene col 2028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2028); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2028]; `tensor/DDL_lfc|DDL_z.npy` [2028]; `embed/gene_vectors.npy` [2028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2028 or target_col == 2028). Every well: [[TRIP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
