---
symbol: "TMCO3"
type: "gene"
col: 7432
ensembl_id: "ENSG00000150403"
name: "solute carrier family 9 member D1"
location: "13q34"
module: 37
arm: "+"
pooled_cpm: 102.37
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TMCO3

*solute carrier family 9 member D1* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.41× (z +8.2, q 2e-13, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.641× (z -15.0, q 0e+00, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TICAM2]] (+0.64, fdr 7e-06), [[GOLGA3]] (+0.58, fdr 1e-05), [[PCGF3-AS1]] (+0.57, fdr 1e-05); moves opposite to [[CYP2J2]] (-0.53, fdr 4e-05), [[THEM6]] (-0.52, fdr 1e-05), [[MRPL57]] (-0.51, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DAB2IP]] → it (grade C ⚠); 1 goes from it, the strongest it → [[DCUN1D2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +8.2 | 2e-13 | 31/48 (SHP-77, A498, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +7.9 | 6e-13 | 38/47 (SHP-77, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +7.1 | 3e-10 | 28/48 (SHP-77, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +6.5 | 1e-08 | 23/49 (LS 180, SHP-77, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +6.4 | 2e-08 | 33/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +6.2 | 5e-08 | 26/47 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +5.9 | 3e-07 | 27/47 (SHP-77, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +5.3 | 8e-06 | 25/48 (LS 180, SHP-77, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +5.0 | 3e-05 | 15/48 (Panc 03.27, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 2e-04 | 21/47 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +4.2 | 0.001 | 18/48 (SW480, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.7 | 0.008 | 18/48 (RKO, SW480, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.20× | +3.7 | 0.009 | 20/50 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.016 | 18/47 (HepG2/C3A, PANC-1, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.016 | 17/48 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.077 | 12/49 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Neratinib (drug)]] 5 µM |  | 1.13× | +3.0 | 0.077 | 9/48 (SW 900, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.077 | 3/49 (NCI-H1573, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -15.0 | 0e+00 | 33/48 (hTERT-HPNE, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -14.2 | 2e-43 | 39/48 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.623×** | -11.3 | 3e-27 | 41/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.641×** | -10.6 | 4e-24 | 41/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.741×** | -10.1 | 5e-22 | 34/48 (SNU-423, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.663×** | -9.8 | 1e-20 | 36/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -9.2 | 2e-18 | 32/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.722×** | -7.8 | 5e-13 | 33/48 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.557×** | -7.0 | 2e-10 | 34/49 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.738×** | -7.0 | 2e-10 | 27/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.748×** | -6.9 | 2e-10 | 26/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -5.2 | 1e-05 | 22/48 (HOP62, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.810×** | -5.0 | 2e-05 | 22/48 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.814×** | -4.9 | 3e-05 | 21/48 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.815×** | -4.9 | 4e-05 | 25/49 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.826×** | -4.6 | 2e-04 | 23/48 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.840× | -4.0 | 0.002 | 22/48 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.725×** | -3.9 | 0.003 | 18/49 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.851× | -3.9 | 0.003 | 18/48 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.729×** | -3.8 | 0.003 | 16/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.007 | 18/48 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.744×** | -3.5 | 0.008 | 20/48 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 173 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -19.2) |
| [[HS-578T (line)]] | alt | 97.9 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -13.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.475× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 359 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -14.3) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.410× (z -9.4) |
| [[HOP62 (line)]] | alt | 142 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -14.5) |
| [[SNU-423 (line)]] | alt | 103 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -18.4) |
| [[hTERT-HPNE (line)]] | wt | 144 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -20.8) |
| [[PANC-1 (line)]] | alt | 111 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.415× (z -15.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.613× (z -8.5) |
| [[C32 (line)]] | wt | 67.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -19.7) |
| [[SW 900 (line)]] | alt | 90.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.321× (z -11.6) |
| [[A498 (line)]] | wt | 91.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 88.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -14.1) |
| [[SNU-1 (line)]] | wt | 228 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 62.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.321× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 93.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.415× (z -10.1) |
| [[RKO (line)]] | wt | 82.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 106 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 57.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 80.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.7) |
| [[Hs 766T (line)]] | wt | 139 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -12.0) |
| [[LS 180 (line)]] | wt | 119 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.02× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 83.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.515× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0696× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 52.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -14.5) |
| [[SW480 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.473× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 129 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TICAM2]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[GOLGA3]] | +0.58 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[PCGF3-AS1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DNHD1]] | +0.55 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[DCUN1D2]] | +0.55 | +0.54 / +0.61 | both halves | 1e-05 | STRING 495; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[WDR49]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TMED7-TICAM2]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SMG1P7]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TNXB]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[KLRA1P]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CCDC92]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[PSMD6-AS2]] | +0.52 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[TTC28-AS1]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP2J2]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[THEM6]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MRPL57]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DNPH1]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MCAT]] | -0.48 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[DIP2B]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CHIC1]] | -0.47 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[CKMT1B]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MEIS1]] | -0.47 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[INPP4B]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ATP5MC3]] ⚠ | -0.47 | -0.32 / -0.55 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18A]] | -0.47 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[IQGAP2]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAB2IP]] | C | DAB2IP activity lowers TMCO3's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.69× higher at baseline in the lines without DAB2IP | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCUN1D2]] | C | TMCO3's natural level strengthens DCUN1D2's drug response | TMCO3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.39; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.8, -27.8); signed map (11.4, 1.7). **Vector** length 127, 39.0% of its response variance represented; |z| ≥ 3 in 1,406 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +8.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.2 | +6.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.5 | +7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +6.0 | +5.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.9 | +6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.6 | +5.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.0 | +4.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.8 | -10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -14.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,491,021-113,554,590 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20623; previously C13orf11, TMCO3 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWJ1](https://www.uniprot.org/uniprotkb/Q6UWJ1) (Solute carrier family 9 member D1):

> Probable Na(+):H(+) or K(+):H(+) antiporter (Probable). Upon IGF1-dependent phosphorylation, facilitates the membrane translocation and activation of AKT1.

**Summary**, from NCBI Gene [55002](https://www.ncbi.nlm.nih.gov/gene/55002):

> This gene encodes a member of the monovalent cation:proton antiporter 2 (CPA2) family of transporter proteins. Members of this family typically couple the export of monovalent cations, such as potassium or sodium, to the import of protons across cellular membranes. Mutations in this gene have been identified in patients with a rare inherited vision defect, cornea guttata with anterior polar cataract. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:20329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20329) · Entrez [55002](https://www.ncbi.nlm.nih.gov/gene/55002) · UniProt [Q6UWJ1](https://www.uniprot.org/uniprotkb/Q6UWJ1) · Ensembl [ENSG00000150403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150403)

## Data

Gene col 7432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7432); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7432]; `tensor/DDL_lfc|DDL_z.npy` [7432]; `embed/gene_vectors.npy` [7432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7432 or target_col == 7432). Every well: [[TMCO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMCO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
