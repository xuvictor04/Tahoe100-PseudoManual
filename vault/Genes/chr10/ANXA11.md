---
symbol: "ANXA11"
type: "gene"
col: 4329
ensembl_id: "ENSG00000122359"
name: "annexin A11"
location: "10q22.3"
module: 31
arm: "+"
pooled_cpm: 145.47
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 40
direction_downstream: 2
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ANXA11

*annexin A11* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.50× (z +9.7, q 1e-19, up in 26 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 2.08×, A-427 2.88×, C-33 A 4.52×, SNU-1 3.79×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 2.37×, MIA PaCa-2 2.43×, A498 2.21×, PANC-1 1.92×, …; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 2.71×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.440× (z -27.8, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L1]] (+0.67, fdr 7e-06), [[ACTN4]] (+0.67, fdr 7e-06), [[ST14]] (+0.63, fdr 7e-06); moves opposite to [[ST3GAL3]] (-0.65, fdr 7e-06), [[CREM]] (-0.57, fdr 2e-05), [[C10orf88]] (-0.55, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[INAVA]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4329.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 2.08×, A-427 2.88×, C-33 A 4.52×, SNU-1 3.79×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 2.37×, MIA PaCa-2 2.43×, A498 2.21×, PANC-1 1.92×, …; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 2.71×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +9.7 | 1e-19 | 26/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +8.7 | 1e-15 | 19/40 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +4.5 | 0.001 | 19/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.21×** | +4.2 | 0.004 | 21/44 (hTERT-HPNE, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +4.1 | 0.004 | 5/47 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.13 | 7/47 (AsPC-1, A-427, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.13 | 11/46 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.13× | +3.0 | 0.17 | 8/48 (KATO III, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.440×** | -27.8 | 0e+00 | 45/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.356×** | -24.7 | 0e+00 | 44/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -14.6 | 0e+00 | 40/47 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.578×** | -13.1 | 3e-37 | 40/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.660×** | -10.0 | 3e-21 | 39/47 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.771×** | -8.8 | 2e-16 | 24/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.682×** | -8.7 | 2e-16 | 32/46 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.695×** | -8.7 | 3e-16 | 31/47 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -8.3 | 7e-15 | 34/47 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -8.1 | 2e-14 | 32/47 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -7.1 | 7e-11 | 29/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.758×** | -6.6 | 2e-09 | 24/47 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.753×** | -6.4 | 5e-09 | 27/47 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.769×** | -6.3 | 2e-08 | 26/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.855× | -5.3 | 5e-06 | 18/47 (SW480, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -5.3 | 5e-06 | 23/47 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.671×** | -5.0 | 2e-05 | 21/48 (CFPAC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.825×** | -4.6 | 1e-04 | 22/47 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.728×** | -4.0 | 0.002 | 19/47 (KATO III, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.749×** | -3.6 | 0.006 | 18/47 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.860× | -3.6 | 0.007 | 19/47 (LoVo, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 351 | 0 | 17 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -24.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -18.7) |
| [[LoVo (line)]] | wt | 367 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -24.8) |
| [[AsPC-1 (line)]] | alt | 332 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -14.7) |
| [[KATO III (line)]] | alt | 332 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -20.2) |
| [[Panc 03.27 (line)]] | alt | 368 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -17.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 266 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -16.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -15.7) |
| [[HT-29 (line)]] | alt | 432 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.0) |
| [[SW480 (line)]] | alt | 176 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -14.4) |
| [[C32 (line)]] | wt | 63.5 | 2 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -19.9) |
| [[MIA PaCa-2 (line)]] | alt | 76.1 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.43× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -18.6) |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -25.0) |
| [[NCI-H2347 (line)]] | alt | 193 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -19.4) |
| [[NCI-H460 (line)]] | wt | 58.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -17.1) |
| [[PANC-1 (line)]] | alt | 80.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -22.6) |
| [[SNU-1 (line)]] | wt | 55.2 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -19.8) |
| [[SW1417 (line)]] | alt | 343 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.563× (z -8.9) |
| [[A-172 (line)]] | wt | 109 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -16.1) |
| [[Hs 766T (line)]] | wt | 210 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -17.4) |
| [[LS 180 (line)]] | wt | 297 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -11.0) |
| [[A498 (line)]] | wt | 74.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -10.1) |
| [[COLO 205 (line)]] | alt | 210 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -14.2) |
| [[HOP62 (line)]] | alt | 48.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 42.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 57.3 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.220× (z -12.8) |
| [[SW48 (line)]] | wt | 346 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.0) |
| [[A549 (line)]] | wt | 83.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +9.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 62.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 63.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 49.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 73.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -17.5) |
| [[SW 900 (line)]] | alt | 94.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -12.3) |
| [[A-427 (line)]] | wt | 58.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 78.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.3) |
| [[C-33 A (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 56.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -8.8) |
| [[HS-578T (line)]] | alt | 47.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -10.8) |
| [[J82 (line)]] | alt | 54.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 50.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.344× (z -9.6) |
| [[RKO (line)]] | wt | 64.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -11.7) |
| [[SNU-423 (line)]] | alt | 85.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -11.2) |
| [[SW 1271 (line)]] | alt | 59.5 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0570× (z -10.1) |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L1]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ACTN4]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ST14]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[INAVA]] | +0.62 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DLG3]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[JUP]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[MYRF]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TJP2]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MAL2]] | +0.57 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[PCDH1]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.57 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[SLC35A3]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.65 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[CREM]] | -0.57 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[C10orf88]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ZNF397]] | -0.53 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.51 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[TRPC1]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TRIP11]] | -0.49 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[POLI]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[DDX50]] | -0.49 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FBXO28]] | -0.49 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[RBX1]] | -0.49 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[AK6]] | -0.49 | -0.54 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 39, C 1. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INAVA]] | B | INAVA activity raises ANXA11's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.24× lower at baseline in the lines without INAVA | 4e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[ST14]] | B | ST14 activity raises ANXA11's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.64× lower at baseline in the lines without ST14 | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[CLIC5]] | B | CLIC5 activity raises ANXA11's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.84× lower at baseline in the lines without CLIC5 | 1e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[CDH1]] | B | CDH1 activity raises ANXA11's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.38× lower at baseline in the lines without CDH1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[B3GNT3]] | B | B3GNT3 activity raises ANXA11's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without B3GNT3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[TC2N]] | B | TC2N activity raises ANXA11's level | lines that do not express TC2N (28) vs lines expressing it (22) | 3.02× lower at baseline in the lines without TC2N | 3e-04 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[ITGB4]] | B | ITGB4 activity raises ANXA11's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.16× lower at baseline in the lines without ITGB4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises ANXA11's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.22× lower at baseline in the lines without TMPRSS2 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[PADI1]] | B | PADI1 activity raises ANXA11's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.98× lower at baseline in the lines without PADI1 | 1e-03 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[TTC28]] | B | TTC28 activity lowers ANXA11's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.83× higher at baseline in the lines without TTC28 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[MAL2]] | B | MAL2 activity raises ANXA11's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without MAL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[MYO5B]] | B | MYO5B activity raises ANXA11's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | C | ANXA11's natural level lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | ANXA11's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.073 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Filgotinib (drug)]] 0.05 µM | C | ANXA11's natural level lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | ANXA11's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.287 over the table, 0.060 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.3, 56.7); signed map (-12.2, 36.6). **Vector** length 120, 37.4% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +5.0 | -4.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | -0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.9 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.6 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -24.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -5.5 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -13.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -27.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -8.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | annexin A11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:80,150,889-80,205,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ANX11 |
| Gene groups (HGNC) | Annexins |
| Matched by | ensembl_id |

**Function**, from UniProt [P50995](https://www.uniprot.org/uniprotkb/P50995) (Annexin A11):

> Binds specifically to calcyclin in a calcium-dependent manner (By similarity). Required for midbody formation and completion of the terminal phase of cytokinesis.

**Summary**, from NCBI Gene [311](https://www.ncbi.nlm.nih.gov/gene/311):

> This gene encodes a member of the annexin family, a group of calcium-dependent phospholipid-binding proteins. Annexins have unique N-terminal domains and conserved C-terminal domains, which contain calcium-dependent phospholipid-binding sites. The encoded protein is a 56-kD antigen recognized by sera from patients with various autoimmune diseases. Several transcript variants encoding two different isoforms have been identified. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:535) · Entrez [311](https://www.ncbi.nlm.nih.gov/gene/311) · UniProt [P50995](https://www.uniprot.org/uniprotkb/P50995) · Ensembl [ENSG00000122359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122359)

## Data

Gene col 4329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4329); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4329]; `tensor/DDL_lfc|DDL_z.npy` [4329]; `embed/gene_vectors.npy` [4329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4329 or target_col == 4329). Every well: [[ANXA11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
