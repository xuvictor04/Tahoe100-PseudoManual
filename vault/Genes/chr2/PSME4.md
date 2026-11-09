---
symbol: "PSME4"
type: "gene"
col: 902
ensembl_id: "ENSG00000068878"
name: "proteasome activator subunit 4"
location: "2p16.2"
module: 94
arm: "+"
pooled_cpm: 256.83
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# PSME4

*proteasome activator subunit 4* — 2p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.29× (z +12.9, q 2e-35, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.556× (z -8.8, q 6e-16, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.737× (z -4.8, q 2e-04, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3KBP1]] (+0.61, fdr 1e-05), [[ELOVL5]] (+0.58, fdr 1e-05), [[DAP3]] (+0.58, fdr 2e-05); moves opposite to [[ZNF563]] (-0.59, fdr 2e-05), [[ZNF442]] (-0.58, fdr 3e-05), [[ZNF616]] (-0.57, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GYPC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.29×** | +12.9 | 2e-35 | 48/48 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +12.1 | 2e-31 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +11.9 | 2e-30 | 43/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.12×** | +11.1 | 3e-26 | 48/48 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.03×** | +11.0 | 3e-26 | 48/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +10.0 | 9e-22 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +9.7 | 4e-20 | 44/47 (COLO 205, SHP-77, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +9.0 | 2e-17 | 45/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +8.3 | 7e-15 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +7.8 | 3e-13 | 45/49 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.92×** | +7.3 | 2e-11 | 46/49 (COLO 205, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +7.1 | 8e-11 | 40/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +6.8 | 5e-10 | 44/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +6.4 | 7e-09 | 39/48 (COLO 205, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.4 | 2e-06 | 39/45 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +5.2 | 7e-06 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +4.7 | 7e-05 | 29/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 9e-04 | 27/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 902.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -8.8 | 6e-16 | 40/44 (SW 900, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.591×** | -8.2 | 6e-14 | 40/49 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.732×** | -6.9 | 1e-09 | 40/48 (AsPC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.737×** | -4.8 | 2e-04 | 40/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.738×** | -4.8 | 2e-04 | 30/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.742×** | -4.7 | 3e-04 | 36/48 (KATO III, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.735×** | -4.5 | 7e-04 | 31/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.772×** | -4.0 | 0.004 | 28/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.707×** | -3.9 | 0.007 | 37/48 (Hs 766T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.734×** | -3.4 | 0.032 | 30/48 (HS-578T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.806×** | -3.4 | 0.037 | 29/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.823× | -3.1 | 0.11 | 23/47 (SW480, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 294 | 12 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.82× (z +17.6) | — |
| [[SW480 (line)]] | alt | 261 | 12 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 116 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +18.0) | — |
| [[NCI-H23 (line)]] | alt | 218 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.1) | — |
| [[C32 (line)]] | wt | 168 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -11.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 265 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.93× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 480 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 223 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 326 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.439× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 180 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 251 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.01× (z +13.0) | — |
| [[RKO (line)]] | wt | 521 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -20.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 516 | 5 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.63× (z +13.1) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.12× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 160 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.8) | — |
| [[BT-474 (line)]] | alt | 229 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 145 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.80× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 160 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.8) | — |
| [[KATO III (line)]] | alt | 194 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.64× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 310 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.13× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 236 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 237 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.08× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 298 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 311 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.31× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 229 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 131 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 215 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +18.3) | — |
| [[NCI-H2347 (line)]] | alt | 229 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -12.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 379 | 1 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.10× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -14.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 343 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 254 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.32× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 295 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.81× (z +15.6) | — |
| [[A-172 (line)]] | wt | 192 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 332 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 291 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -13.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 277 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -13.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 316 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 208 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.5) | — |
| [[J82 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.16× (z +8.7) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 312 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 240 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 222 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 236 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 230 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3KBP1]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ELOVL5]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DAP3]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[EVI5]] | +0.57 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[PLAA]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 | same gene group |
| [[PSMD1]] | +0.54 | +0.45 / +0.63 | both halves | 3e-05 | same gene group; pathway: Proteasome assembly; STRING 818 |
| [[SNX29]] | +0.54 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[NAPG]] | +0.54 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[KLHL25]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[GCKR]] | +0.52 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[TRAPPC10]] | +0.52 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[TMEM41B]] | +0.52 | +0.51 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF563]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[ZNF442]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ZNF616]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[DNAJC27]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZNF44]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[THAP6]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ZNF441]] | -0.56 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ARRDC3]] | -0.53 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[YY1AP1]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CLN5]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CLK4]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ATP6V1C1]] | -0.52 | -0.57 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GYPC]] | B | GYPC activity lowers PSME4's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.21× higher at baseline in the lines without GYPC | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[ZNF44]] | C | ZNF44 activity strengthens PSME4's drug response | lines that do not express ZNF44 (3) vs lines expressing it (44) | the lines without ZNF44 respond 0.97× as strongly (z diff +0.91); strongest at Bortezomib 0.05 µM: 1.68x vs 2.22x (z diff +3.8) | 0.081 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1; target measured in part of the lines; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction -0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.9, 24.2); signed map (-49.8, 31.5). **Vector** length 86.0, 37.5% of its response variance represented; |z| ≥ 3 in 1,607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +12.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +11.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +7.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -9.4 | -6.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.5 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.5 | +12.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | +7.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | +0.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | proteasome activator subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.2 — chr2:53,864,069-53,970,993 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PA200, KIAA0077 |
| Gene groups (HGNC) | Proteasome; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14997](https://www.uniprot.org/uniprotkb/Q14997) (Proteasome activator complex subunit 4):

> Associated component of the proteasome that specifically recognizes acetylated histones and promotes ATP- and ubiquitin-independent degradation of core histones during spermatogenesis and DNA damage response. Recognizes and binds acetylated histones via its bromodomain-like (BRDL) region and activates the proteasome by opening the gated channel for substrate entry. Binds to the core proteasome via its C-terminus, which occupies the same binding sites as the proteasomal ATPases, opening the …

**Summary**, from NCBI Gene [23198](https://www.ncbi.nlm.nih.gov/gene/23198):

> Predicted to enable peptidase activator activity. Predicted to be involved in DNA repair; proteasomal ubiquitin-independent protein catabolic process; and sperm DNA condensation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20635) · Entrez [23198](https://www.ncbi.nlm.nih.gov/gene/23198) · UniProt [Q14997](https://www.uniprot.org/uniprotkb/Q14997) · Ensembl [ENSG00000068878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068878)

## Data

Gene col 902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 902); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 902]; `tensor/DDL_lfc|DDL_z.npy` [902]; `embed/gene_vectors.npy` [902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 902 or target_col == 902). Every well: [[PSME4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSME4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
