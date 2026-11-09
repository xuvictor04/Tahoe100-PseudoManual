---
symbol: "AP3B1"
type: "gene"
col: 5383
ensembl_id: "ENSG00000132842"
name: "adaptor related protein complex 3 subunit beta 1"
location: "5q14.1"
module: 56
arm: "+"
pooled_cpm: 356.65
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# AP3B1

*adaptor related protein complex 3 subunit beta 1* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 1.39× (z +9.6, q 4e-19, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Selinexor (drug)]] 0.05 µM: 1.35× (z +8.9, q 1e-16, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.627× (z -19.4, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RARS2]] (+0.58, fdr 2e-05), [[PIK3C2A]] (+0.58, fdr 1e-05), [[PMS2P4-1]] (+0.57, fdr 1e-05); moves opposite to [[AKIRIN1]] (-0.46, fdr 3e-05), [[CHTOP]] (-0.45, fdr 6e-05), [[VEZF1]] (-0.45, fdr 2e-04).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.39×** | +9.6 | 4e-19 | 41/48 (SW480, HT-29, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +9.5 | 4e-19 | 28/48 (NCI-H460, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.35×** | +8.9 | 1e-16 | 39/49 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +6.2 | 8e-08 | 28/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.30×** | +5.5 | 5e-06 | 34/48 (A549, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.19× | +5.0 | 4e-05 | 21/48 (C-33 A, SHP-77, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.27×** | +3.7 | 0.016 | 24/45 (NCI-H1573, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.026 | 26/49 (A498, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.026 | 8/48 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.4 | 0.038 | 16/50 (RKO, Panc 03.27, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.4 | 0.039 | 16/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.074 | 3/48 (CFPAC-1, SW 1088, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.12× | +3.1 | 0.077 | 7/49 (HepG2/C3A, A498, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.081 | 18/48 (HOP62, A549, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5383.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.627×** | -19.4 | 0e+00 | 37/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -16.0 | 0e+00 | 46/47 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.632×** | -13.5 | 4e-39 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.639×** | -12.2 | 7e-32 | 39/45 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.673×** | -11.7 | 2e-29 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -11.3 | 1e-27 | 32/49 (A549, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.683×** | -11.2 | 3e-27 | 47/48 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.685×** | -11.1 | 8e-27 | 35/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.695×** | -10.7 | 6e-25 | 36/49 (NCI-H23, SNU-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.706×** | -10.2 | 8e-23 | 42/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.717×** | -9.4 | 3e-19 | 33/44 (C-33 A, AsPC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.759×** | -8.1 | 2e-14 | 31/48 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -6.1 | 5e-08 | 28/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.879× | -5.4 | 3e-06 | 10/48 (NCI-H2347, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.834× | -5.3 | 3e-06 | 24/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.840× | -4.9 | 3e-05 | 21/48 (J82, SK-MEL-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.871× | -4.0 | 0.001 | 8/49 (A549, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.910× | -3.9 | 0.002 | 7/48 (A549, CFPAC-1, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.004 | 25/49 (NCI-H2347, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.920× | -3.5 | 0.011 | 4/48 (A549, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 404 | 1 (1 ⚠) | 11 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.52× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -24.9) |
| [[CFPAC-1 (line)]] | alt | 323 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -19.5) |
| [[KATO III (line)]] | alt | 311 | 1 (1 ⚠) | 8 (2 ⚠) | [[Selinexor (drug)]] 0.5 µM 1.58× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -19.4) |
| [[RPMI-7951 (line)]] | alt | 368 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -22.6) |
| [[SW480 (line)]] | alt | 393 | 3 (2 ⚠) | 6 (2 ⚠) | [[Selinexor (drug)]] 0.5 µM 1.69× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 1.56× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -15.5) |
| [[C-33 A (line)]] | alt | 383 | 4 (2 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.56× (z +11.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Osimertinib (mesylate) (drug)]] 5 µM 1.68× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.595× (z -9.1) |
| [[H4 (line)]] | wt | 491 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 354 | 3 (2 ⚠) | 5 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.53× (z +12.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 1.67× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -28.7) |
| [[AsPC-1 (line)]] | alt | 424 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.458× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.479× (z -13.1) |
| [[HCT15 (line)]] | alt | 446 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.8) |
| [[hTERT-HPNE (line)]] | wt | 465 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 310 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -26.9) |
| [[NCI-H2347 (line)]] | alt | 451 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.496× (z -12.6) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.576× (z -10.3) |
| [[LoVo (line)]] | wt | 511 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -24.6) |
| [[SW 900 (line)]] | alt | 428 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.432× (z -14.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.546× (z -10.7) |
| [[A549 (line)]] | wt | 372 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -21.8) |
| [[COLO 205 (line)]] | alt | 468 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.291× (z -16.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.360× (z -14.0) |
| [[HS-578T (line)]] | alt | 382 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -17.8) |
| [[HT-29 (line)]] | alt | 242 | 4 (3 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.53× (z +11.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 1.59× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.558× (z -10.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 425 | 2 (1 ⚠) | 3 | [[Selinexor (drug)]] 0.5 µM 1.63× (z +9.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 1.59× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.521× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 307 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 389 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.621× (z -12.5) |
| [[PANC-1 (line)]] | alt | 346 | 3 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Docetaxel (drug)]] 0.05 µM 0.617× (z -10.8) ⚠ transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 342 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -18.1) |
| [[AN3 CA (line)]] | alt | 546 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.543× (z -10.0) |
| [[C32 (line)]] | wt | 314 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -22.3) |
| [[HEC-1-A (line)]] | alt | 281 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 0.5 µM 1.54× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.568× (z -12.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.594× (z -11.6) |
| [[Hs 766T (line)]] | wt | 331 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -14.2) |
| [[J82 (line)]] | alt | 336 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -23.1) |
| [[NCI-H2030 (line)]] | alt | 293 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -17.0) |
| [[SHP-77 (line)]] | alt | 285 | 2 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 0.05 µM 1.82× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.566× (z -9.9) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.618× (z -8.7) |
| [[SNU-423 (line)]] | alt | 333 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -24.1) |
| [[SW1417 (line)]] | alt | 213 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.594× (z -8.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.613× (z -8.7) |
| [[A498 (line)]] | wt | 292 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -18.4) |
| [[LS 180 (line)]] | wt | 384 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 257 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -17.6) |
| [[SNU-1 (line)]] | wt | 389 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 318 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.537× (z -10.3) ⚠ toxic |
| [[RKO (line)]] | wt | 385 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.551× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.611× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 226 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.61× (z +9.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 430 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 327 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 417 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 640 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 427 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 319 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARS2]] | +0.58 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[PIK3C2A]] | +0.58 | +0.68 / +0.49 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis; STRING 509 |
| [[PMS2P4-1]] | +0.57 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[COPA]] | +0.55 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[PDSS2]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SRP54]] | +0.53 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[APAF1]] | +0.53 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[METTL15]] | +0.52 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[ANO10]] | +0.52 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SLC39A9]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SEC23A]] | +0.51 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[PPME1]] | +0.51 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKIRIN1]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CHTOP]] | -0.45 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[VEZF1]] | -0.45 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[CSRNP1]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[CUEDC1]] | -0.44 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[MAFK]] | -0.43 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[SOCS3]] | -0.42 | -0.55 / -0.29 | both halves | 3e-04 |  |
| [[KAT6A]] | -0.42 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SMURF1]] | -0.42 | -0.12 / -0.45 | ⚠ not reproduced | 0.002 |  |
| [[RANGAP1]] | -0.42 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.3, -19.3); signed map (-43.9, 14.6). **Vector** length 125, 46.4% of its response variance represented; |z| ≥ 3 in 1,427 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +16.3 | +9.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +12.0 | +9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.9 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.8 | +3.4 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +7.4 | +8.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.3 | +5.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.5 | +5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +3.1 |
|  | [[EX229 (drug)]] 0.05 µM |  | +3.6 | +3.5 |
|  | [[EX229 (drug)]] 0.5 µM |  | +3.6 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.3 | -16.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -19.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.6 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 3 subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:78,000,522-78,294,762 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADTB3A, HPS2 |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 3 |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 7 pathways, smallest: Golgi Associated Vesicle Biogenesis; Signaling by BRAF and RAF1 fusions; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [O00203](https://www.uniprot.org/uniprotkb/O00203) (AP-3 complex subunit beta-1):

> Subunit of non-clathrin- and clathrin-associated adaptor protein complex 3 (AP-3) that plays a role in protein sorting in the late-Golgi/trans-Golgi network (TGN) and/or endosomes. The AP complexes mediate both the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules. AP-3 appears to be involved in the sorting of a subset of transmembrane proteins targeted to lysosomes and lysosome-related organelles. In concert …

**Summary**, from NCBI Gene [8546](https://www.ncbi.nlm.nih.gov/gene/8546):

> This gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. The encoded protein is part of the heterotetrameric AP-3 protein complex which interacts with the scaffolding protein clathrin. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 2. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:566) · Entrez [8546](https://www.ncbi.nlm.nih.gov/gene/8546) · UniProt [O00203](https://www.uniprot.org/uniprotkb/O00203) · Ensembl [ENSG00000132842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132842)

## Data

Gene col 5383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5383); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5383]; `tensor/DDL_lfc|DDL_z.npy` [5383]; `embed/gene_vectors.npy` [5383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5383 or target_col == 5383). Every well: [[AP3B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP3B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
