---
symbol: "XRN1"
type: "gene"
col: 3529
ensembl_id: "ENSG00000114127"
name: "5'-3' exoribonuclease 1"
location: "3q23"
module: 74
arm: "+"
pooled_cpm: 235.49
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# XRN1

*5'-3' exoribonuclease 1* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.57× (z +18.5, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.568× (z -16.2, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.734× (z -12.5, q 1e-33, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP350]] (+0.74, fdr 7e-06), [[NIPBL]] (+0.73, fdr 7e-06), [[NBR1]] (+0.72, fdr 7e-06); moves opposite to [[METAP1]] (-0.63, fdr 1e-05), [[NTAQ1]] (-0.62, fdr 1e-05), [[NBEAL2]] (-0.62, fdr 8e-06).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +18.5 | 0e+00 | 36/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +11.5 | 2e-28 | 32/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +11.4 | 7e-28 | 37/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +9.6 | 1e-19 | 36/49 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +7.3 | 4e-11 | 29/48 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +7.0 | 3e-10 | 32/48 (LoVo, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +6.8 | 6e-10 | 32/47 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +5.4 | 4e-06 | 35/49 (HEC-1-A, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +5.4 | 4e-06 | 24/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.17× | +4.7 | 1e-04 | 20/50 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +4.2 | 0.001 | 11/48 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +4.1 | 0.002 | 18/47 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.002 | 26/50 (LoVo, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.7 | 0.010 | 7/48 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.6 | 0.014 | 10/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.027 | 14/48 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3529.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.568×** | -16.2 | 0e+00 | 48/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.631×** | -12.7 | 2e-34 | 37/44 (NCI-H1573, SNU-1, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.734×** | -12.5 | 1e-33 | 44/48 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.625×** | -12.4 | 2e-33 | 37/45 (NCI-H460, HT-29, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.648×** | -12.4 | 2e-33 | 38/49 (NCI-H1573, A-427, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.661×** | -11.8 | 2e-30 | 37/48 (NCI-H1792, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.680×** | -11.0 | 2e-26 | 36/48 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.704×** | -10.0 | 7e-22 | 32/48 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.722×** | -9.3 | 9e-19 | 42/49 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.816×** | -8.2 | 1e-14 | 26/49 (A549, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -8.2 | 2e-14 | 35/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.584×** | -8.1 | 4e-14 | 45/48 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.594×** | -7.8 | 3e-13 | 45/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.776×** | -7.2 | 2e-11 | 29/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.618×** | -7.2 | 2e-11 | 39/48 (NCI-H460, RKO, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.636×** | -6.8 | 4e-10 | 40/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.705×** | -5.2 | 5e-06 | 33/48 (HEC-1-A, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.790×** | -4.8 | 4e-05 | 24/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.798×** | -4.6 | 1e-04 | 31/49 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.817×** | -4.1 | 9e-04 | 21/48 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.013 | 19/46 (HOP62, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | 0.883× | -3.4 | 0.013 | 5/48 (RKO, NCI-H661, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.847× | -3.4 | 0.014 | 18/48 (SW 1271, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.890× | -3.3 | 0.017 | 9/48 (SHP-77, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 324 | 4 | 11 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -14.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.623× (z -11.5) |
| [[LoVo (line)]] | wt | 294 | 4 | 9 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 3.85× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.626× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 383 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.375× (z -12.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.553× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 282 | 0 | 10 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.322× (z -16.8) ⚠ unreliable plate only · without an alert: [[Tucidinostat (drug)]] 5 µM 0.614× (z -10.2) |
| [[A-427 (line)]] | wt | 242 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.618× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 274 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.500× (z -13.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.593× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 213 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 262 | 0 | 7 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.422× (z -14.2) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.594× (z -8.6) |
| [[SNU-423 (line)]] | alt | 322 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.453× (z -12.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.627× (z -10.4) |
| [[KATO III (line)]] | alt | 308 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 265 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.78× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.394× (z -14.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 159 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 233 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +17.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.321× (z -17.1) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 346 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.18× (z +10.3) | [[Tucidinostat (drug)]] 5 µM 0.606× (z -9.8) |
| [[BT-474 (line)]] | alt | 246 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +19.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 249 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.3) | [[Ponatinib (drug)]] 5 µM 0.532× (z -8.8) |
| [[H4 (line)]] | wt | 269 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 243 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +15.0) | — |
| [[HT-29 (line)]] | alt | 222 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.584× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 191 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +19.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -11.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.650× (z -10.0) |
| [[PANC-1 (line)]] | alt | 212 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +20.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.544× (z -13.0) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 183 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.649× (z -9.0) |
| [[A549 (line)]] | wt | 204 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -17.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 210 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.370× (z -11.2) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 339 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HOP62 (line)]] | alt | 213 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.511× (z -11.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 261 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.446× (z -12.0) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 175 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.8) | — |
| [[SW480 (line)]] | alt | 243 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.538× (z -11.5) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 192 | 0 | 3 (2 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.611× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 251 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +24.3) | [[Dinaciclib (drug)]] 5 µM 0.513× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.560× (z -10.5) |
| [[SNU-1 (line)]] | wt | 216 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 165 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.387× (z -10.1) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 184 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 202 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.488× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[AN3 CA (line)]] | alt | 227 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 298 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 283 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.417× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.474× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 196 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.3) | — |
| [[Panc 03.27 (line)]] | alt | 371 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW1417 (line)]] | alt | 237 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.506× (z -9.3) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 265 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP350]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | STRING 652 |
| [[NIPBL]] | +0.73 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[NBR1]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[LARP7]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[C11orf58]] | +0.70 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[BPTF]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[RSF1]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[BOD1L1]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[IFIT2]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[DCP1A]] | +0.64 | +0.72 / +0.57 | both halves | 9e-06 | same gene group; pathway: Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; STRING 999 |
| [[PAXIP1-AS2]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.63 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[NBEAL2]] | -0.62 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[PALS2]] | -0.62 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ASIC1]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[FAR1]] | -0.60 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[AHCY]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[WASF3]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NSUN5P1]] | -0.58 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[LYPLA1]] | -0.57 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[SEH1L]] | -0.57 | -0.62 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.1, -46.5); signed map (4.3, -15.0). **Vector** length 142, 53.1% of its response variance represented; |z| ≥ 3 in 1,699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +10.7 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.8 | +18.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +9.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.6 | +6.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.1 | +3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.9 | +4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +7.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.9 | -16.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -10.3 | -12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.2 | -9.3 |
|  | [[EX229 (drug)]] 5 µM |  | -6.9 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.2 | -7.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.1 | -8.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | 5'-3' exoribonuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:142,306,607-142,448,062 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEP1 |
| Gene groups (HGNC) | RNA decapping and exonuclease complex subunits |
| Reactome | 9 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; Tristetraprolin (TTP, ZFP36) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZH2](https://www.uniprot.org/uniprotkb/Q8IZH2) (5'-3' exoribonuclease 1):

> Major 5'-3' exoribonuclease involved in mRNA decay. Required for the 5'-3'-processing of the G4 tetraplex-containing DNA and RNA substrates (By similarity). The kinetic of hydrolysis is faster for G4 RNA tetraplex than for G4 DNA tetraplex and monomeric RNA tetraplex (By similarity). Plays a role in replication-dependent histone mRNA degradation. May act as a tumor suppressor protein in osteogenic sarcoma (OGS).

**Summary**, from NCBI Gene [54464](https://www.ncbi.nlm.nih.gov/gene/54464):

> This gene encodes a member of the 5'-3' exonuclease family. The encoded protein may be involved in replication-dependent histone mRNA degradation, and interacts directly with the enhancer of mRNA-decapping protein 4. In addition to mRNA metabolism, a similar protein in yeast has been implicated in a variety of nuclear and cytoplasmic functions, including homologous recombination, meiosis, telomere maintenance, and microtubule assembly. Mutations in this gene are associated with osteosarcoma, …

**Accessions** — [HGNC:30654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30654) · Entrez [54464](https://www.ncbi.nlm.nih.gov/gene/54464) · UniProt [Q8IZH2](https://www.uniprot.org/uniprotkb/Q8IZH2) · Ensembl [ENSG00000114127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114127)

## Data

Gene col 3529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3529); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3529]; `tensor/DDL_lfc|DDL_z.npy` [3529]; `embed/gene_vectors.npy` [3529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3529 or target_col == 3529). Every well: [[XRN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
