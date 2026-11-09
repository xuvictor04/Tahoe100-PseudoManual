---
symbol: "MAST2"
type: "gene"
col: 1450
ensembl_id: "ENSG00000086015"
name: "microtubule associated serine/threonine kinase 2"
location: "1p34.1"
module: 163
arm: "+"
pooled_cpm: 107.09
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# MAST2

*microtubule associated serine/threonine kinase 2* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.62× (z +9.4, q 3e-18, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.543× (z -12.1, q 8e-31, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.795× (z -4.6, q 7e-04, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (A-427 0.0667×, C-33 A 0.141×, HEC-1-A 0.260×, SNU-1 0.180×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (AN3 CA 0.0652×, SNU-1 0.228×, A-172 0.286×, NCI-H661 0.0927×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.254×, NCI-H2030 0.294×, SW480 0.429×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.517×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP4A]] (+0.70, fdr 1e-05), [[SRPK2]] (+0.68, fdr 7e-06), [[FAR1]] (+0.66, fdr 7e-06); moves opposite to [[MYSM1]] (-0.59, fdr 3e-05), [[HELQ]] (-0.59, fdr 8e-05), [[NBR1]] (-0.58, fdr 2e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +9.4 | 3e-18 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +9.2 | 1e-17 | 42/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.9 | 5e-13 | 36/47 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +7.8 | 7e-13 | 39/48 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +7.4 | 1e-11 | 34/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +7.1 | 1e-10 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 7e-09 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +6.1 | 9e-08 | 32/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.31×** | +5.2 | 1e-05 | 30/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +4.9 | 5e-05 | 26/47 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 2e-04 | 28/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.5 | 4e-04 | 24/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 4e-04 | 26/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.25×** | +4.3 | 6e-04 | 26/48 (LoVo, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +4.1 | 0.002 | 22/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.002 | 25/48 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.003 | 15/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.015 | 19/49 (CFPAC-1, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.015 | 19/48 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.021 | 21/48 (NCI-H460, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.023 | 14/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1450.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (A-427 0.0667×, C-33 A 0.141×, HEC-1-A 0.260×, SNU-1 0.180×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (AN3 CA 0.0652×, SNU-1 0.228×, A-172 0.286×, NCI-H661 0.0927×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.254×, NCI-H2030 0.294×, SW480 0.429×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.517×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.543×** | -12.1 | 8e-31 | 39/49 (C-33 A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.584×** | -9.9 | 2e-20 | 39/45 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -7.9 | 4e-13 | 33/44 (AN3 CA, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -4.6 | 7e-04 | 23/48 (LoVo, A-172, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.011 | 24/49 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.873× | -3.8 | 0.011 | 8/48 (J82, SW 1271, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.838× | -3.4 | 0.052 | 22/47 (HepG2/C3A, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.845× | -3.4 | 0.052 | 14/48 (A498, SNU-423, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | 0.846× | -3.3 | 0.052 | 21/48 (J82, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.773× | -3.0 | 0.14 | 16/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 139 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -14.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 138 | 1 | 4 (3 ⚠) | [[Belumosudil (drug)]] 5 µM 1.97× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.517× (z -9.1) |
| [[PANC-1 (line)]] | alt | 124 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 192 | 2 | 3 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.84× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -15.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 132 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 126 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.06× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -10.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 61.4 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.04× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0667× (z -34.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 193 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -20.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -16.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 65.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 84.6 | 1 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.12× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 72.0 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.53× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 81.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.03× (z +9.1) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -9.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 111 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +11.7) | — |
| [[A549 (line)]] | wt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0652× (z -18.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 94.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.27× (z +10.8) ⚠ unreliable plate only | — |
| [[LOX-IMVI (line)]] | wt | 82.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0927× (z -12.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.490× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 157 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 78.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP4A]] | +0.70 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[SRPK2]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[FAR1]] | +0.66 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[RNF38]] | +0.65 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[MFSD14B]] | +0.64 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.63 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[VKORC1L1]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CYTH3]] | +0.63 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[STIM1]] | +0.62 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[PALS2]] | +0.61 | +0.74 / +0.47 | both halves | 2e-05 | same gene group |
| [[EPS15]] | +0.61 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[UBE2G1]] | +0.61 | +0.68 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYSM1]] | -0.59 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[HELQ]] | -0.59 | -0.71 / -0.37 | both halves | 8e-05 |  |
| [[NBR1]] | -0.58 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[GOSR1]] | -0.58 | -0.67 / -0.46 | both halves | 3e-05 |  |
| [[PAN2]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[HMG20A]] | -0.56 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[RBM23]] | -0.56 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[SRGAP3]] | -0.54 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[OCIAD1]] | -0.54 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[THAP2]] | -0.54 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[FAM200A]] | -0.53 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[LGALS8]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises MAST2's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without STARD9 | 0.010 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises MAST2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without GNAZ | 0.014 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[GFOD1]] | B | GFOD1 activity raises MAST2's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without GFOD1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[DNMT3B]] | C | DNMT3B activity raises MAST2's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.58× lower at baseline in the lines without DNMT3B | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[GARNL3]] | C | GARNL3 activity raises MAST2's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without GARNL3 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.3, -7.5); signed map (-44.6, -6.6). **Vector** length 119, 38.2% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +9.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.2 | +7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +7.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +4.5 | +3.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.3 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.5 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.2 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated serine/threonine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,786,987-46,036,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAST205, KIAA0807 |
| Gene groups (HGNC) | PDZ domain containing; Microtubule associated serine/threonine kinase family |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P0Q8](https://www.uniprot.org/uniprotkb/Q6P0Q8) (Microtubule-associated serine/threonine-protein kinase 2):

> Appears to link the dystrophin/utrophin network with microtubule filaments via the syntrophins. Phosphorylation of DMD or UTRN may modulate their affinities for associated proteins. Functions in a multi-protein complex in spermatid maturation. Regulates lipopolysaccharide-induced IL-12 synthesis in macrophages by forming a complex with TRAF6, resulting in the inhibition of TRAF6 NF-kappa-B activation (By similarity).

**Summary**, from NCBI Gene [23139](https://www.ncbi.nlm.nih.gov/gene/23139):

> Enables phosphatase binding activity. Predicted to be involved in several processes, including protein phosphorylation; regulation of interleukin-12 production; and spermatid differentiation. Predicted to be located in cytoplasm; cytoskeleton; and plasma membrane. Predicted to be active in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19035) · Entrez [23139](https://www.ncbi.nlm.nih.gov/gene/23139) · UniProt [Q6P0Q8](https://www.uniprot.org/uniprotkb/Q6P0Q8) · Ensembl [ENSG00000086015](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086015)

## Data

Gene col 1450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1450); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1450]; `tensor/DDL_lfc|DDL_z.npy` [1450]; `embed/gene_vectors.npy` [1450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1450 or target_col == 1450). Every well: [[MAST2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAST2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
