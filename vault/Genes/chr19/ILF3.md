---
symbol: "ILF3"
type: "gene"
col: 4967
ensembl_id: "ENSG00000129351"
name: "interleukin enhancer binding factor 3"
location: "19p13.2"
module: 3
arm: "-"
pooled_cpm: 161.0
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ILF3

*interleukin enhancer binding factor 3* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.50× (z +24.6, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.18× (z +8.0, q 1e-13, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.590× (z -10.4, q 2e-22, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUPT16H]] (+0.74, fdr 7e-06), [[SRSF1]] (+0.70, fdr 7e-06), [[EWSR1]] (+0.70, fdr 7e-06); moves opposite to [[CIAO2B]] (-0.74, fdr 7e-06), [[COMMD6]] (-0.72, fdr 7e-06), [[PLIN3]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Futibatinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.50×** | +24.6 | 0e+00 | 49/49 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +22.5 | 0e+00 | 44/44 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +16.7 | 0e+00 | 44/45 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +12.3 | 2e-32 | 39/48 (NCI-H460, SNU-423, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.74×** | +10.9 | 2e-25 | 45/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.57×** | +8.5 | 2e-15 | 42/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +8.0 | 1e-13 | 46/49 (COLO 205, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.49×** | +7.8 | 5e-13 | 37/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +7.6 | 2e-12 | 38/48 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +7.4 | 8e-12 | 39/48 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.40×** | +6.6 | 3e-09 | 38/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +6.3 | 2e-08 | 38/48 (PANC-1, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-08 | 34/48 (AN3 CA, BT-474, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.9 | 1e-07 | 39/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.33×** | +5.6 | 1e-06 | 34/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.006 | 25/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.010 | 24/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.016 | 27/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.024 | 31/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.088 | 21/48 (CFPAC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4967.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -10.4 | 2e-22 | 42/48 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.621×** | -9.4 | 2e-18 | 41/48 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.629×** | -9.1 | 1e-17 | 40/48 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.723×** | -6.4 | 2e-08 | 36/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -5.4 | 7e-06 | 26/48 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.769×** | -5.2 | 2e-05 | 35/49 (LS 180, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.815×** | -4.0 | 0.004 | 26/48 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.682×** | -3.9 | 0.006 | 30/49 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.2 | 0.088 | 18/48 (LS 180, AN3 CA, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.855× | -3.1 | 0.11 | 10/49 (HEC-1-A, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 129 | 13 (13 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +23.7) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 5 µM 0.450× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 108 | 10 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +22.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 2.86× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 187 | 6 (6 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +19.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.449× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 96.4 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +20.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 149 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +18.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -13.6) |
| [[SW480 (line)]] | alt | 216 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +19.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -11.1) |
| [[C32 (line)]] | wt | 109 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 5.31× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 72.2 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +14.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 113 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +17.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 185 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +24.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.493× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 253 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +16.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.439× (z -10.8) |
| [[SNU-423 (line)]] | alt | 121 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +20.2) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +9.0) | — |
| [[A-172 (line)]] | wt | 158 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +20.1) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[A-427 (line)]] | wt | 226 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +15.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.423× (z -12.3) |
| [[A498 (line)]] | wt | 137 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +19.5) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[AsPC-1 (line)]] | alt | 112 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.3) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 0.5 µM 0.497× (z -8.7) |
| [[C-33 A (line)]] | alt | 299 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -14.9) |
| [[COLO 205 (line)]] | alt | 118 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.13× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 148 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.5) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[KATO III (line)]] | alt | 125 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +15.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 137 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +16.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.488× (z -9.2) |
| [[LS 180 (line)]] | wt | 159 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +16.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 208 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +17.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.382× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 145 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.1) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[RPMI-7951 (line)]] | alt | 157 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.4) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[A549 (line)]] | wt | 115 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +17.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 134 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 180 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +14.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.552× (z -8.6) |
| [[Hs 766T (line)]] | wt | 102 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +12.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +12.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 160 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +15.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 136 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.46× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 112 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 264 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.433× (z -9.1) |
| [[BT-474 (line)]] | alt | 241 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 1.92× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.527× (z -8.9) |
| [[HT-29 (line)]] | alt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +19.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 168 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 189 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +15.2) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 182 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.260× (z -10.4) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HCT15 (line)]] | alt | 263 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 255 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +14.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 222 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 183 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 320 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.57× (z +9.8) | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPT16H]] | +0.74 | +0.76 / +0.67 | both halves | 7e-06 | STRING 438 |
| [[SRSF1]] | +0.70 | +0.58 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 787 |
| [[EWSR1]] | +0.70 | +0.60 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 704 |
| [[U2AF2]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 | STRING 799 |
| [[SNX5]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[HNRNPM]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 | STRING 970 |
| [[CAPRIN1]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 | STRING 523 |
| [[DARS2]] | +0.67 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 | STRING 994 |
| [[HNRNPL]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 | STRING 995 |
| [[XRCC5]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 | STRING 676 |
| [[IPO5]] | +0.66 | +0.56 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2B]] | -0.74 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.72 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[PLIN3]] | -0.68 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[ARID3A]] | -0.67 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[CDKN2D]] | -0.67 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[POLD4]] | -0.66 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[RNF181]] | -0.65 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[MIEN1]] | -0.65 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[WIPF2]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[PIGH]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[GUK1]] | -0.65 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[DUSP18]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ILF3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ILF3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CIB1]] | C | CIB1 activity lowers ILF3's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.52× higher at baseline in the lines without CIB1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Futibatinib (drug)]] 0.05 µM | C | ILF3's natural level raises the cells' numbers under Futibatinib 0.05 µM (protects the cells) | ILF3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.268 over the table, 0.024 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | ILF3's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | ILF3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.60 | 0.471 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | ILF3's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | ILF3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.2, -25.7); signed map (14.9, -38.0). **Vector** length 104, 39.4% of its response variance represented; |z| ≥ 3 in 1,461 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.57 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.57 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.56 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +7.4 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +16.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +22.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +24.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | +3.9 | +8.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.7 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.0 | -9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -10.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | interleukin enhancer binding factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,654,304-10,692,400 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NF90, MPHOSPH4, MPP4, NFAR-1, NFAR110, NFAR-2, TCP110, NF110 |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 12 pathways, smallest: Regulation of CDH11 gene transcription; Regulation of CDH11 Expression and Function; Regulation of Expression and Function of Type II Classical Cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12906](https://www.uniprot.org/uniprotkb/Q12906) (Interleukin enhancer-binding factor 3):

> RNA-binding protein that plays an essential role in the biogenesis of circular RNAs (circRNAs) which are produced by back-splicing circularization of pre-mRNAs. Within the nucleus, promotes circRNAs processing by stabilizing the regulatory elements residing in the flanking introns of the circularized exons. Plays thereby a role in the back-splicing of a subset of circRNAs. As a consequence, participates in a wide range of transcriptional and post-transcriptional processes. Binds to poly-U …

**Summary**, from NCBI Gene [3609](https://www.ncbi.nlm.nih.gov/gene/3609):

> This gene encodes a double-stranded RNA (dsRNA) binding protein that complexes with other proteins, dsRNAs, small noncoding RNAs, and mRNAs to regulate gene expression and stabilize mRNAs. This protein (NF90, ILF3) forms a heterodimer with a 45 kDa transcription factor (NF45, ILF2) required for T-cell expression of interleukin 2. This complex has been shown to affect the redistribution of nuclear mRNA to the cytoplasm. Knockdown of NF45 or NF90 protein retards cell growth, possibly by …

**Accessions** — [HGNC:6038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6038) · Entrez [3609](https://www.ncbi.nlm.nih.gov/gene/3609) · UniProt [Q12906](https://www.uniprot.org/uniprotkb/Q12906) · Ensembl [ENSG00000129351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129351)

## Data

Gene col 4967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4967); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4967]; `tensor/DDL_lfc|DDL_z.npy` [4967]; `embed/gene_vectors.npy` [4967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4967 or target_col == 4967). Every well: [[ILF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
