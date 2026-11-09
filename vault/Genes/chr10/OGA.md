---
symbol: "OGA"
type: "gene"
col: 12586
ensembl_id: "ENSG00000198408"
name: "O-GlcNAcase"
location: "10q24.32"
module: 69
arm: "+"
pooled_cpm: 490.68
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 18
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# OGA

*O-GlcNAcase* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +15.5, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.570× (z -10.2, q 7e-22, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.562× (z -5.5, q 4e-06, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CERT1]] (+0.72, fdr 7e-06), [[EZH1]] (+0.72, fdr 7e-06), [[AAMDC]] (+0.71, fdr 7e-06); moves opposite to [[HNRNPAB]] (-0.66, fdr 7e-06), [[NAA15]] (-0.65, fdr 7e-06), [[WDR4]] (-0.64, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF160]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +15.5 | 0e+00 | 41/48 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +10.5 | 4e-23 | 45/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.0 | 3e-13 | 41/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +6.7 | 2e-09 | 46/48 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.44×** | +6.6 | 4e-09 | 45/49 (HCT15, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.6 | 5e-09 | 34/48 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 4e-08 | 38/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +6.1 | 8e-08 | 40/48 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +5.8 | 3e-07 | 42/48 (C32, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 9e-07 | 31/48 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 4e-04 | 22/48 (NCI-H2030, A-427, …) | all doses, flat | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.001 | 33/49 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 28/48 (HepG2/C3A, HCT15, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.008 | 37/48 (J82, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.013 | 34/48 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.038 | 31/48 (A-427, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.570×** | -10.2 | 7e-22 | 42/49 (RKO, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.581×** | -9.9 | 2e-20 | 48/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.574×** | -9.3 | 2e-18 | 40/45 (A549, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -8.8 | 1e-16 | 38/44 (NCI-H1792, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.562×** | -5.5 | 4e-06 | 45/48 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.598×** | -4.9 | 9e-05 | 43/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.773×** | -4.5 | 5e-04 | 33/47 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.840× | -4.5 | 6e-04 | 19/48 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.789×** | -4.3 | 9e-04 | 33/48 (Panc 03.27, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.636×** | -4.3 | 9e-04 | 43/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.653×** | -4.1 | 0.002 | 35/48 (NCI-H2347, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.655×** | -4.0 | 0.002 | 39/47 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.795×** | -4.0 | 0.002 | 29/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.859× | -3.9 | 0.004 | 14/48 (A-427, Panc 03.27, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.814×** | -3.8 | 0.006 | 27/49 (Panc 03.27, SW48, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.821×** | -3.6 | 0.012 | 26/49 (Panc 03.27, A549, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.014 | 26/48 (Panc 03.27, SW48, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.833×** | -3.3 | 0.025 | 23/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.722×** | -3.1 | 0.052 | 27/48 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.849× | -3.0 | 0.069 | 19/48 (SW480, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 490 | 8 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +23.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.515× (z -10.9) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 488 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +20.7) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 289 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +21.0) | — |
| [[A549 (line)]] | wt | 514 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 584 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -13.9) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 431 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +15.8) | — |
| [[AsPC-1 (line)]] | alt | 725 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 441 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 693 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -12.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 300 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +16.2) | — |
| [[LoVo (line)]] | wt | 343 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +16.6) | — |
| [[NCI-H23 (line)]] | alt | 523 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 555 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.455× (z -12.3) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 463 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +19.8) | — |
| [[A-172 (line)]] | wt | 673 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 321 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +13.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.451× (z -9.8) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 484 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.543× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 479 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -16.4) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 623 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +15.7) | — |
| [[SK-MEL-2 (line)]] | alt | 494 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.422× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.544× (z -9.3) |
| [[BT-474 (line)]] | alt | 323 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 528 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +17.2) | — |
| [[J82 (line)]] | alt | 347 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.0) | — |
| [[LOX-IMVI (line)]] | wt | 421 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.470× (z -11.2) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 566 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.464× (z -10.3) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 480 | 0 | 3 (2 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.350× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 198 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 297 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.00× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 780 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -11.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 835 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 550 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -10.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 337 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 608 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 536 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 450 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 598 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.469× (z -10.8) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 411 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.470× (z -8.7) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 289 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 480 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -11.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 490 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 637 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 467 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 595 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.6) | — |
| [[HOP62 (line)]] | alt | 644 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 429 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 694 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 533 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 433 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 535 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 433 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERT1]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[EZH1]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.71 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CCNG2]] | +0.69 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ZCRB1]] | +0.68 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ATXN3]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[EXOC1]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[WSB1]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GARRE1]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[WDR48]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.66 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[NAA15]] | -0.65 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[WDR4]] | -0.64 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | -0.62 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[URB2]] | -0.61 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[UGGT2]] | -0.61 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[PUS1]] | -0.60 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[PSMD1]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ARMC6]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF160]] | C | ZNF160 activity raises OGA's level | lines that do not express ZNF160 (4) vs lines expressing it (46) | 1.66× lower at baseline in the lines without ZNF160 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF845, TBL1X, ZNF551; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.9, -42.3); signed map (-14.9, 6.9). **Vector** length 129, 55.9% of its response variance represented; |z| ≥ 3 in 1,511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.9 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +8.8 | +6.7 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.5 | +6.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.5 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.7 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.7 | -9.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.0 | -5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.9 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -6.8 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.6 | -4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | O-GlcNAcase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:101,784,443-101,818,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEA5, NCOAT; previously MGEA5 |
| Gene groups (HGNC) | Hexosaminidases |
| Matched by | ensembl_id |

**Function**, from UniProt [O60502](https://www.uniprot.org/uniprotkb/O60502) (Protein O-GlcNAcase):

> [Isoform 1]: Cleaves GlcNAc but not GalNAc from O-glycosylated proteins. Deglycosylates a large and diverse number of proteins, such as CRYAB, ELK1, GSDMD, LMNB1 and TAB1. Can use p-nitrophenyl-beta-GlcNAc and 4-methylumbelliferone-GlcNAc as substrates but not p-nitrophenyl-beta-GalNAc or p-nitrophenyl-alpha-GlcNAc (in vitro). Does not bind acetyl-CoA and does not have histone acetyltransferase activity.; [Isoform 3]: Cleaves GlcNAc but not GalNAc from O-glycosylated proteins. Can use …

**Summary**, from NCBI Gene [10724](https://www.ncbi.nlm.nih.gov/gene/10724):

> The dynamic modification of cytoplasmic and nuclear proteins by O-linked N-acetylglucosamine (O-GlcNAc) addition and removal on serine and threonine residues is catalyzed by OGT (MIM 300255), which adds O-GlcNAc, and MGEA5, a glycosidase that removes O-GlcNAc modifications (Gao et al., 2001 [PubMed 11148210]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:7056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7056) · Entrez [10724](https://www.ncbi.nlm.nih.gov/gene/10724) · UniProt [O60502](https://www.uniprot.org/uniprotkb/O60502) · Ensembl [ENSG00000198408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198408)

## Data

Gene col 12586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12586); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12586]; `tensor/DDL_lfc|DDL_z.npy` [12586]; `embed/gene_vectors.npy` [12586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12586 or target_col == 12586). Every well: [[OGA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
