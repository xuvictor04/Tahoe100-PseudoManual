---
symbol: "PHF3"
type: "gene"
col: 3992
ensembl_id: "ENSG00000118482"
name: "PHD finger protein 3"
location: "6q12"
module: 74
arm: "+"
pooled_cpm: 331.39
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 40
n_dd_up_clean: 8
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# PHF3

*PHD finger protein 3* — 6q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.56× (z +6.0, q 1e-06, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (21 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.532× (z -16.4, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.537× (z -8.4, q 3e-15, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2A]] (+0.68, fdr 7e-06), [[IK]] (+0.65, fdr 7e-06), [[ZNF292]] (+0.64, fdr 7e-06); moves opposite to [[NCLN]] (-0.58, fdr 1e-05), [[MAD1L1]] (-0.58, fdr 1e-05), [[LRP8]] (-0.58, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +6.0 | 1e-06 | 34/49 (LoVo, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +4.9 | 2e-04 | 28/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.9 | 2e-04 | 24/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.8 | 2e-04 | 17/48 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.42×** | +4.7 | 3e-04 | 38/50 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +4.4 | 0.001 | 30/49 (LoVo, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.19× | +4.1 | 0.003 | 20/50 (LoVo, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.22×** | +4.1 | 0.003 | 27/49 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.006 | 30/49 (HEC-1-A, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.021 | 17/48 (HOP62, NCI-H2347, …) | two highest doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.032 | 22/49 (HEC-1-A, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.051 | 23/48 (KATO III, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.058 | 6/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 26 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3992.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.532×** | -16.4 | 0e+00 | 48/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.560×** | -15.0 | 0e+00 | 43/49 (COLO 205, SW 1271, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.554×** | -14.7 | 0e+00 | 46/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.583×** | -13.4 | 5e-39 | 41/44 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.702×** | -13.0 | 3e-36 | 39/49 (A549, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.618×** | -12.5 | 9e-34 | 41/48 (SNU-423, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.684×** | -9.1 | 8e-18 | 34/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.714×** | -8.7 | 2e-16 | 36/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.721×** | -8.4 | 2e-15 | 34/48 (SNU-1, C32, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.537×** | -8.4 | 3e-15 | 46/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.541×** | -8.3 | 6e-15 | 45/48 (NCI-H1792, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.544×** | -8.2 | 1e-14 | 46/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.723×** | -8.1 | 3e-14 | 36/50 (SNU-423, C32, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.551×** | -8.0 | 4e-14 | 44/48 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.729×** | -7.9 | 1e-13 | 36/48 (SNU-423, SK-MEL-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.571×** | -7.5 | 1e-12 | 44/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -7.4 | 3e-12 | 30/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.669×** | -7.0 | 7e-11 | 46/48 (SW48, SW 1271, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.681×** | -6.7 | 6e-10 | 45/48 (SW48, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -6.6 | 1e-09 | 30/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.697×** | -6.3 | 9e-09 | 46/49 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.677×** | -5.2 | 3e-06 | 38/46 (NCI-H460, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.810×** | -5.1 | 5e-06 | 28/48 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.765×** | -4.7 | 6e-05 | 33/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.712×** | -4.6 | 9e-05 | 36/47 (SW48, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.829×** | -4.6 | 9e-05 | 25/48 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 287 | 1 | 11 (10 ⚠) | [[PH-797804 (drug)]] 5 µM 4.30× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -13.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.485× (z -11.4) |
| [[SNU-423 (line)]] | alt | 595 | 0 | 12 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -15.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.652× (z -10.0) |
| [[SW480 (line)]] | alt | 298 | 0 | 11 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -16.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 354 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[EX229 (drug)]] 5 µM 0.340× (z -9.2) |
| [[SNU-1 (line)]] | wt | 437 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.452× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.646× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 667 | 0 | 9 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.298× (z -17.2) ⚠ toxic |
| [[SW 900 (line)]] | alt | 304 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[COLO 205 (line)]] | alt | 1,202 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HEC-1-A (line)]] | alt | 378 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -18.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.658× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 396 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HOP62 (line)]] | alt | 335 | 2 (1 ⚠) | 5 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.78× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.68× (z +8.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.564× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 481 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[CHP-212 (line)]] | wt | 455 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.256× (z -13.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 612 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[hTERT-HPNE (line)]] | wt | 325 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 305 | 4 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.490× (z -13.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 280 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.609× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[H4 (line)]] | wt | 424 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 235 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.436× (z -12.0) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 354 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -17.4) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 347 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.396× (z -14.3) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 242 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 207 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.385× (z -12.6) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 333 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.423× (z -11.3) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 295 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 259 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[C-33 A (line)]] | alt | 386 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.457× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[LoVo (line)]] | wt | 364 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.461× (z -13.9) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 414 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.530× (z -11.4) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 232 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.495× (z -14.1) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 247 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.407× (z -14.5) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 320 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.01× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -14.8) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 241 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -24.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 483 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.515× (z -8.6) |
| [[PANC-1 (line)]] | alt | 285 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.536× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[RKO (line)]] | wt | 417 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.430× (z -13.9) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 301 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SHP-77 (line)]] | alt | 262 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.581× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW 1271 (line)]] | alt | 462 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A498 (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.508× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[HS-578T (line)]] | alt | 221 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.506× (z -10.5) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 337 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 2.81× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.486× (z -10.0) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 434 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HCT15 (line)]] | alt | 446 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2A]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 | same gene group |
| [[IK]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[ZNF292]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 | STRING 413 |
| [[NBR1]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[DHX40]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CIR1]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CRNKL1]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TNRC6B]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SF3B1]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SYF2]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCLN]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[LRP8]] | -0.58 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[MYO19]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[CAPN15]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.53 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[FAM20B]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[DHRS11]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[TTL]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[UBE2G2]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CAMKK2]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers PHF3's level | compounds that target MTOR: 4 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Sapanisertib) | 50% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |
| [[TOP2A]] | B | TOP2A activity raises PHF3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.3, -47.7); signed map (-16.8, 7.4). **Vector** length 144, 58.3% of its response variance represented; |z| ≥ 3 in 1,960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.3 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.1 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.6 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.3 | -16.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.1 | -8.3 |
|  | [[EX229 (drug)]] 5 µM |  | -8.0 | -8.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.9 | -8.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.9 | -8.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -7.0 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q12 — chr6:63,635,802-63,779,336 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PHD finger proteins |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

UniProt [Q92576](https://www.uniprot.org/uniprotkb/Q92576) carries no function annotation.

**Summary**, from NCBI Gene [23469](https://www.ncbi.nlm.nih.gov/gene/23469):

> This gene encodes a member of a PHD finger-containing gene family. This gene may function as a transcription factor and may be involved in glioblastomas development. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:8921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8921) · Entrez [23469](https://www.ncbi.nlm.nih.gov/gene/23469) · UniProt [Q92576](https://www.uniprot.org/uniprotkb/Q92576) · Ensembl [ENSG00000118482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118482)

## Data

Gene col 3992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3992); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3992]; `tensor/DDL_lfc|DDL_z.npy` [3992]; `embed/gene_vectors.npy` [3992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3992 or target_col == 3992). Every well: [[PHF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
