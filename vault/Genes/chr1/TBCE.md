---
symbol: "TBCE"
type: "gene"
col: 16070
ensembl_id: "ENSG00000284770"
name: "tubulin folding cofactor E"
location: "1q42.3"
module: 30
arm: "+"
pooled_cpm: 47.35
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TBCE

*tubulin folding cofactor E* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.39× (z +20.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.752× (z -6.7, q 1e-08, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.136×, KATO III 0.155×, RPMI-7951 0.236×, SK-MEL-2 0.294×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.150×, H4 0.0946×, A-172 0.397×, HepG2/C3A 0.266×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.328×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.239×); [[CP21R7 (drug)]] 5 µM in 1 line (H4 0.0615×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.67, fdr 2e-05), [[TBCB]] (+0.66, fdr 2e-05), [[IFT52]] (+0.65, fdr 1e-05); moves opposite to [[RFX3]] (-0.63, fdr 1e-05), [[BAZ1A]] (-0.61, fdr 3e-05), [[HIVEP1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLSCR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +20.6 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +17.0 | 0e+00 | 46/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +16.9 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +15.6 | 0e+00 | 36/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +12.3 | 2e-32 | 43/48 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +12.1 | 1e-31 | 39/48 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +9.1 | 1e-17 | 39/48 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.6 | 1e-06 | 23/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +5.5 | 2e-06 | 24/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +5.3 | 7e-06 | 27/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +5.2 | 9e-06 | 15/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 1e-04 | 19/48 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +4.4 | 5e-04 | 18/48 (SW1417, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.12× | +3.8 | 0.005 | 17/48 (A-172, SW 900, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.005 | 16/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.014 | 8/47 (RKO, LOX-IMVI, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16070.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.136×, KATO III 0.155×, RPMI-7951 0.236×, SK-MEL-2 0.294×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.150×, H4 0.0946×, A-172 0.397×, HepG2/C3A 0.266×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.328×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.239×); [[CP21R7 (drug)]] 5 µM in 1 line (H4 0.0615×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.752×** | -6.7 | 1e-08 | 27/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **0.798×** | -4.9 | 2e-04 | 23/44 (A-427, KATO III, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.828×** | -4.5 | 0.002 | 23/47 (NCI-H2347, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.846× | -3.7 | 0.036 | 13/47 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.863× | -3.5 | 0.057 | 14/48 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 0.871× | -3.2 | 0.11 | 17/48 (RKO, NCI-H2347, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | 0.878× | -3.1 | 0.17 | 10/47 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.913× | -3.0 | 0.17 | 5/48 (SW 1088, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 40.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +11.8) | [[Lonafarnib (drug)]] 5 µM 0.135× (z -9.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 61.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.6) | — |
| [[Panc 03.27 (line)]] | alt | 34.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 67.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 38.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +18.6) | — |
| [[SW480 (line)]] | alt | 43.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +23.8) | — |
| [[HT-29 (line)]] | alt | 33.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) | — |
| [[LoVo (line)]] | wt | 33.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 36.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.4) | — |
| [[A-427 (line)]] | wt | 67.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[HEC-1-A (line)]] | alt | 41.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +11.0) | — |
| [[KATO III (line)]] | alt | 20.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.27× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[MIA PaCa-2 (line)]] | alt | 90.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.3) | — |
| [[RKO (line)]] | wt | 45.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[H4 (line)]] | wt | 46.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0946× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[CP21R7 (drug)]] 5 µM 0.0615× (z -9.8) |
| [[HCT15 (line)]] | alt | 45.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.2) | [[Thymol (drug)]] 0.5 µM 0.239× (z -10.4) |
| [[Hs 766T (line)]] | wt | 42.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.0) | — |
| [[J82 (line)]] | alt | 40.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 36.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SW 900 (line)]] | alt | 54.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +10.3) | — |
| [[A-172 (line)]] | wt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 56.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.04× (z +8.5) | — |
| [[A549 (line)]] | wt | 45.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 53.6 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.41× (z +8.5) | — |
| [[C32 (line)]] | wt | 44.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.102× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 42.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.20× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 40.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 42.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SNU-1 (line)]] | wt | 42.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.328× (z -11.3) |
| [[SW48 (line)]] | wt | 43.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.67 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TBCB]] | +0.66 | +0.52 / +0.48 | both halves | 2e-05 | pathway: Post-chaperonin tubulin folding pathway; STRING 807 |
| [[IFT52]] | +0.65 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.64 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MGST3]] | +0.64 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ANKRD27]] | +0.64 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[PPIL2]] | +0.63 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[NMRAL1]] | +0.62 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PLD3]] | +0.62 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[CYB5R1]] | +0.62 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[FAM13B]] | +0.60 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CAMKK1]] | +0.59 | +0.53 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3]] | -0.63 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[BAZ1A]] | -0.61 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HIVEP1]] | -0.59 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[IRF2]] | -0.58 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PLSCR2]] | -0.54 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[PSMD6-AS2]] | -0.54 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ASXL2]] | -0.54 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ANXA2R-AS1]] | -0.54 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[NFKB1]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[HIVEP2]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CREBBP]] | -0.53 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[TSC22D1]] | -0.52 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR2]] | B | PLSCR2 activity lowers TBCE's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 1.31× higher at baseline in the lines without PLSCR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[PCED1B]] | B | PCED1B activity lowers TBCE's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 1.10× higher at baseline in the lines without PCED1B | 0.096 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[CLTCL1]] | C | CLTCL1 activity raises TBCE's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 1.54× lower at baseline in the lines without CLTCL1 | 0.078 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.2, -4.2); signed map (-33.9, -2.4). **Vector** length 88.5, 19.4% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +12.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +16.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +20.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tubulin folding cofactor E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:235,367,360-235,452,443 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KCS1, pac2; previously KCS, HRD |
| Reactome | 2 pathways, smallest: Post-chaperonin tubulin folding pathway; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15813](https://www.uniprot.org/uniprotkb/Q15813) (Tubulin-specific chaperone E):

> Tubulin-folding protein; involved in the second step of the tubulin folding pathway and in the regulation of tubulin heterodimer dissociation. Required for correct organization of microtubule cytoskeleton and mitotic splindle, and maintenance of the neuronal microtubule network.

**Summary**, from NCBI Gene [6905](https://www.ncbi.nlm.nih.gov/gene/6905):

> Cofactor E is one of four proteins (cofactors A, D, E, and C) involved in the pathway leading to correctly folded beta-tubulin from folding intermediates. Cofactors A and D are believed to play a role in capturing and stabilizing beta-tubulin intermediates in a quasi-native confirmation. Cofactor E binds to the cofactor D/beta-tubulin complex; interaction with cofactor C then causes the release of beta-tubulin polypeptides that are committed to the native state. Two transcript variants encoding …

**Accessions** — [HGNC:11582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11582) · Entrez [6905](https://www.ncbi.nlm.nih.gov/gene/6905) · UniProt [Q15813](https://www.uniprot.org/uniprotkb/Q15813) · Ensembl [ENSG00000284770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000284770)

## Data

Gene col 16070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16070); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16070]; `tensor/DDL_lfc|DDL_z.npy` [16070]; `embed/gene_vectors.npy` [16070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16070 or target_col == 16070). Every well: [[TBCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
