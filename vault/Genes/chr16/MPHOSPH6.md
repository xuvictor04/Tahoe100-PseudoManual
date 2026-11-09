---
symbol: "MPHOSPH6"
type: "gene"
col: 5743
ensembl_id: "ENSG00000135698"
name: "M-phase phosphoprotein 6"
location: "16q23.3"
module: 1
arm: "+"
pooled_cpm: 28.38
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 18
n_dd_up_clean: 15
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MPHOSPH6

*M-phase phosphoprotein 6* — 16q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.29× (z +11.0, q 2e-25, up in 27 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.00× (z +9.6, q 2e-19, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.471× (z -14.7, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGK]] (+0.70, fdr 7e-06), [[EIF2B3]] (+0.70, fdr 7e-06), [[PPIL1]] (+0.68, fdr 7e-06); moves opposite to [[GNAS]] (-0.68, fdr 1e-05), [[PCMTD1]] (-0.68, fdr 7e-06), [[YPEL5]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.29×** | +11.0 | 2e-25 | 27/33 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **2.14×** | +10.5 | 2e-23 | 35/44 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.00×** | +9.6 | 2e-19 | 41/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.87×** | +8.3 | 2e-14 | 37/47 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +7.6 | 3e-12 | 37/45 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +7.4 | 1e-11 | 39/48 (LOX-IMVI, HS-578T, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +6.9 | 3e-10 | 36/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.62×** | +6.1 | 6e-08 | 32/44 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.9 | 2e-07 | 31/47 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.58×** | +5.9 | 3e-07 | 23/41 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.52×** | +5.8 | 4e-07 | 29/48 (A498, NCI-H1792, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.44×** | +5.1 | 2e-05 | 29/48 (A498, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.28×** | +4.8 | 7e-05 | 21/47 (HT-29, A498, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +4.6 | 2e-04 | 24/48 (A498, NCI-H1792, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.4 | 3e-04 | 24/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.3 | 6e-04 | 24/48 (SNU-423, A498, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.74×** | +4.0 | 0.002 | 20/44 (MIA PaCa-2, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +3.8 | 0.004 | 17/48 (A498, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.005 | 20/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.011 | 16/45 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.015 | 14/46 (SW480, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.021 | 11/45 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.034 | 5/45 (NCI-H23, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.089 | 7/47 (J82, A-172, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.48×** | +2.8 | 0.097 | 9/44 (NCI-H460, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.471×** | -14.7 | 0e+00 | 43/47 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.633×** | -6.0 | 7e-07 | 32/48 (LoVo, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.515×** | -4.8 | 3e-04 | 27/47 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.713×** | -4.5 | 0.001 | 24/47 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.544×** | -4.4 | 0.001 | 23/47 (LOX-IMVI, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.747×** | -4.4 | 0.001 | 25/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.745×** | -3.9 | 0.007 | 17/47 (SNU-1, HOP62, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -3.9 | 0.008 | 22/46 (SNU-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.740×** | -3.8 | 0.008 | 22/48 (LoVo, C32, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.761×** | -3.8 | 0.009 | 20/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.755×** | -3.7 | 0.009 | 17/47 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.792×** | -3.6 | 0.013 | 19/48 (LoVo, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.789×** | -3.6 | 0.013 | 19/48 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.627×** | -3.4 | 0.030 | 17/46 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.634×** | -3.3 | 0.037 | 15/48 (Hs 766T, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.836× | -3.2 | 0.050 | 18/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.796×** | -3.2 | 0.053 | 20/47 (A549, RPMI-7951, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.81× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HT-29 (line)]] | alt | 23.8 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.5) ⚠ cell-cycle shift, explains ~93% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.5) |
| [[PANC-1 (line)]] | alt | 21.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.5) |
| [[RKO (line)]] | wt | 54.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -15.2) |
| [[SW480 (line)]] | alt | 92.6 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 2.18× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.6) |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -13.9) |
| [[LoVo (line)]] | wt | 27.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 35.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.7) |
| [[A-172 (line)]] | wt | 23.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -9.8) |
| [[A-427 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.6) |
| [[Hs 766T (line)]] | wt | 28.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -11.3) |
| [[J82 (line)]] | alt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 25.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -9.0) |
| [[LS 180 (line)]] | wt | 30.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.6) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -9.6) |
| [[SW1417 (line)]] | alt | 30.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -11.7) |
| [[SW48 (line)]] | wt | 23.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -11.9) |
| [[A549 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGK]] | +0.70 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.68 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[EEFSEC]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TAF1B]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[BMS1]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 411 |
| [[RBM28]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |
| [[MAK16]] | +0.66 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[FARSB]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[NOC3L]] | +0.65 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[THOP1]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 | STRING 420 |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.68 | -0.57 / -0.73 | both halves | 1e-05 |  |
| [[PCMTD1]] | -0.68 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[YPEL5]] | -0.67 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.65 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[LAPTM4A]] | -0.64 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[C2]] | -0.63 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[DNASE2]] | -0.62 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[KIAA2026]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[KLRD1]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[CDK19]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[MKRN1]] | -0.59 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.59 | -0.57 / -0.70 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MPHOSPH6's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.5, -42.3); signed map (-2.4, -42.2). **Vector** length 112, 30.8% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.7 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.8 | -14.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.0 | -6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.0 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | M-phase phosphoprotein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.3 — chr16:82,147,798-82,170,224 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MPP6 |
| Reactome | 9 pathways, smallest: Nuclear RNA decay; Somatic hypermutation of immunoglobulin genes; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99547](https://www.uniprot.org/uniprotkb/Q99547) (M-phase phosphoprotein 6):

> RNA-binding protein that associates with the RNA exosome complex. Involved in the 3'-processing of the 7S pre-RNA to the mature 5.8S rRNA and play a role in recruiting the RNA exosome complex to pre-rRNA; this function may include C1D.

**Summary**, from NCBI Gene [10200](https://www.ncbi.nlm.nih.gov/gene/10200):

> Predicted to enable RNA binding activity. Involved in maturation of 5.8S rRNA. Located in nuclear exosome (RNase complex) and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7214) · Entrez [10200](https://www.ncbi.nlm.nih.gov/gene/10200) · UniProt [Q99547](https://www.uniprot.org/uniprotkb/Q99547) · Ensembl [ENSG00000135698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135698)

## Data

Gene col 5743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5743); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5743]; `tensor/DDL_lfc|DDL_z.npy` [5743]; `embed/gene_vectors.npy` [5743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5743 or target_col == 5743). Every well: [[MPHOSPH6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPHOSPH6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
