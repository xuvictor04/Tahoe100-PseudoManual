---
symbol: "TNRC6B"
type: "gene"
col: 1938
ensembl_id: "ENSG00000100354"
name: "trinucleotide repeat containing adaptor 6B"
location: "22q13.1"
module: 225
arm: "+"
pooled_cpm: 298.8
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# TNRC6B

*trinucleotide repeat containing adaptor 6B* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.26× (z +9.9, q 2e-20, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.310× (z -48.7, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.528× (z -19.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.71, fdr 7e-06), [[CNNM2]] (+0.68, fdr 7e-06), [[CREBRF]] (+0.68, fdr 7e-06); moves opposite to [[NIPAL1]] (-0.57, fdr 1e-05), [[F3]] (-0.55, fdr 1e-05), [[C3orf52]] (-0.55, fdr 3e-05).
> It is in [[Module 225]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +9.9 | 2e-20 | 33/48 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +7.2 | 1e-10 | 19/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.10× | +6.0 | 4e-07 | 9/48 (A-172, LoVo, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.08× | +4.9 | 1e-04 | 2/49 (KATO III, Hs 766T) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.12× | +4.9 | 1e-04 | 8/48 (HOP62, KATO III, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.09× | +4.3 | 0.001 | 9/49 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.11× | +4.3 | 0.001 | 8/48 (KATO III, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.09× | +4.3 | 0.001 | 9/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.10× | +4.1 | 0.002 | 3/49 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.07× | +4.1 | 0.002 | 1/48 (J82) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.10× | +3.7 | 0.010 | 16/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.14× | +3.7 | 0.010 | 16/50 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | 1.13× | +3.7 | 0.010 | 8/48 (LS 180, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 1.09× | +3.6 | 0.015 | 0/48 | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.09× | +3.5 | 0.016 | 5/48 (RKO, A-427, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.021 | 11/50 (HEC-1-A, AsPC-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.08× | +3.3 | 0.035 | 11/49 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.035 | 16/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.08× | +3.2 | 0.035 | 3/48 (J82, BT-474, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1938.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.310×** | -48.7 | 0e+00 | 48/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.605×** | -21.3 | 0e+00 | 42/49 (A-427, COLO 205, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.528×** | -19.3 | 0e+00 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.654×** | -17.3 | 0e+00 | 34/44 (LS 180, SNU-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.659×** | -16.4 | 0e+00 | 37/45 (NCI-H2030, NCI-H1573, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -16.3 | 0e+00 | 39/47 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.372×** | -12.7 | 3e-35 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.658×** | -12.7 | 5e-35 | 47/49 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.744×** | -12.1 | 1e-31 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.756×** | -11.9 | 1e-30 | 30/48 (MIA PaCa-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.430×** | -10.9 | 9e-26 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.431×** | -10.8 | 1e-25 | 44/48 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.705×** | -10.6 | 2e-24 | 43/48 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.444×** | -10.5 | 5e-24 | 43/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.843× | -10.2 | 6e-23 | 22/48 (SNU-423, PANC-1, …) | two highest doses | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.461×** | -10.0 | 7e-22 | 46/48 (PANC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.800×** | -9.5 | 9e-20 | 26/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.723×** | -8.8 | 6e-17 | 36/48 (RKO, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.822×** | -8.0 | 3e-14 | 24/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.880× | -7.7 | 5e-13 | 12/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.847× | -7.1 | 4e-11 | 20/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.794×** | -7.0 | 6e-11 | 32/48 (SK-MEL-2, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 348 | 0 | 12 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.161× (z -35.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.456× (z -15.6) |
| [[SNU-1 (line)]] | wt | 448 | 0 | 12 (10 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.214× (z -23.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.455× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 210 | 0 | 11 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.220× (z -29.3) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.466× (z -10.8) |
| [[A549 (line)]] | wt | 237 | 0 | 9 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -25.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.511× (z -13.5) |
| [[A498 (line)]] | wt | 242 | 0 | 8 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -31.0) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.428× (z -13.0) |
| [[C32 (line)]] | wt | 541 | 0 | 8 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -26.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.575× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 467 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.587× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 405 | 0 | 8 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -25.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.515× (z -13.8) |
| [[PANC-1 (line)]] | alt | 306 | 0 | 8 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -34.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.574× (z -15.0) |
| [[SW 900 (line)]] | alt | 361 | 0 | 8 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.212× (z -29.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.566× (z -10.9) |
| [[LS 180 (line)]] | wt | 385 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -27.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 395 | 0 | 7 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.226× (z -25.4) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.435× (z -10.4) |
| [[SW48 (line)]] | wt | 262 | 0 | 6 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.190× (z -18.4) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 347 | 0 | 6 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.338× (z -24.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.621× (z -10.9) |
| [[C-33 A (line)]] | alt | 409 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.245× (z -22.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.474× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 340 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.326× (z -25.1) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.554× (z -9.6) |
| [[HS-578T (line)]] | alt | 354 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.257× (z -27.1) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 229 | 1 | 4 (4 ⚠) | [[Ponatinib (drug)]] 5 µM 1.58× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -20.9) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 364 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -24.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 299 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -27.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.495× (z -10.3) |
| [[CHP-212 (line)]] | wt | 461 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HepG2_C3A (line)]] | wt | 387 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.330× (z -18.0) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 332 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.378× (z -15.1) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 271 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -32.6) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.449× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 243 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.314× (z -21.4) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 339 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -24.1) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.471× (z -9.4) |
| [[SHP-77 (line)]] | alt | 439 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.234× (z -24.3) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 304 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 196 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -14.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.540× (z -8.8) |
| [[COLO 205 (line)]] | alt | 435 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.601× (z -9.8) |
| [[HOP62 (line)]] | alt | 195 | 2 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.79× (z +9.5) ⚠ toxic; cell-cycle shift, explains ~99% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -17.2) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 277 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -23.8) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 234 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.472× (z -11.0) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 298 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -19.7) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 208 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -19.2) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.505× (z -11.3) |
| [[SW 1271 (line)]] | alt | 447 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.218× (z -14.4) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 253 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.83× (z +8.5) ⚠ cell-cycle shift, explains ~87% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.258× (z -18.7) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 420 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.335× (z -16.5) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 313 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.219× (z -24.0) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.469× (z -8.7) |
| [[J82 (line)]] | alt | 176 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.73× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~99% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -22.3) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 202 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -16.3) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 0.5 µM 0.459× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 222 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.471× (z -14.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 164 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.390× (z -15.1) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 376 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.335× (z -11.1) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -13.1) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.437× (z -11.1) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 487 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.368× (z -8.8) ⚠ toxic |
| [[NCI-H2122 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 317 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[BCAS3]] | +0.64 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[FBXL20]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[JMY]] | +0.63 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[AUH]] | +0.63 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[WDR48]] | +0.63 | +0.38 / +0.69 | both halves | 6e-05 |  |
| [[PAN3]] | +0.63 | +0.45 / +0.58 | both halves | 3e-05 | STRING 464 |
| [[RSBN1L]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[HBP1]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[PHF3]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPAL1]] | -0.57 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[F3]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[C3orf52]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PVR]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[CAPN2]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[CYCS]] | -0.52 | -0.34 / -0.53 | both halves | 1e-04 | pathway: Organelle biogenesis and maintenance |
| [[DESI1]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TBILA]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TTPAL]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CYFIP1]] | -0.50 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[LRRC59]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[STK10]] | -0.50 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.8, -42.8); signed map (-15.6, 11.6). **Vector** length 134, 47.8% of its response variance represented; |z| ≥ 3 in 1,879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +9.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -2.1 |
|  | [[crizotinib (drug)]] 5 µM |  | +3.4 | +2.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Ixazomib (drug)]] 5 µM |  | +2.7 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -16.2 | -48.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.6 | -10.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -9.3 | -10.9 |
|  | [[EX229 (drug)]] 5 µM |  | -8.6 | -10.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.5 | -12.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -8.3 | -10.0 |

## What is on record

|  |  |
|---|---|
| Name | trinucleotide repeat containing adaptor 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:40,044,817-40,335,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1093 |
| Gene groups (HGNC) | Armadillo like helical domain containing; TNRC6 adaptor family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 63 pathways, smallest: Post-transcriptional silencing by small RNAs; Regulation of NPAS4 mRNA translation; Regulation of CDH11 mRNA translation by microRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPQ9](https://www.uniprot.org/uniprotkb/Q9UPQ9) (Trinucleotide repeat-containing gene 6B protein):

> Plays a role in RNA-mediated gene silencing by both micro-RNAs (miRNAs) and short interfering RNAs (siRNAs). Required for miRNA-dependent translational repression and siRNA-dependent endonucleolytic cleavage of complementary mRNAs by argonaute family proteins. As scaffolding protein associates with argonaute proteins bound to partially complementary mRNAs and simultaneously can recruit CCR4-NOT and PAN deadenylase complexes.

**Summary**, from NCBI Gene [23112](https://www.ncbi.nlm.nih.gov/gene/23112):

> Enables RNA binding activity. Involved in positive regulation of nuclear-transcribed mRNA catabolic process, deadenylation-dependent decay; positive regulation of nuclear-transcribed mRNA poly(A) tail shortening; and regulatory ncRNA-mediated gene silencing. Acts upstream of with a positive effect on miRNA-mediated gene silencing by inhibition of translation. Predicted to be located in cytosol. Predicted to be active in P-body and nucleoplasm. Implicated in subserous uterine fibroid and uterine …

**Accessions** — [HGNC:29190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29190) · Entrez [23112](https://www.ncbi.nlm.nih.gov/gene/23112) · UniProt [Q9UPQ9](https://www.uniprot.org/uniprotkb/Q9UPQ9) · Ensembl [ENSG00000100354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100354)

## Data

Gene col 1938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1938); `tables/drug_effects.parquet` (91 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1938]; `tensor/DDL_lfc|DDL_z.npy` [1938]; `embed/gene_vectors.npy` [1938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1938 or target_col == 1938). Every well: [[TNRC6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNRC6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
