---
symbol: "COQ8A"
type: "gene"
col: 8624
ensembl_id: "ENSG00000163050"
name: "coenzyme Q8A"
location: "1q42.13"
module: 76
arm: "+"
pooled_cpm: 14.88
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 28
n_dd_up_clean: 21
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# COQ8A

*coenzyme Q8A* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.32× (z +16.8, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.225× (z -20.8, q 0e+00, down in 47 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.254× (z -10.0, q 4e-21, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AUH]] (+0.73, fdr 7e-06), [[HACL1]] (+0.67, fdr 1e-05), [[SPSB3]] (+0.65, fdr 2e-05); moves opposite to [[DESI1]] (-0.51, fdr 6e-05), [[CYCS]] (-0.51, fdr 4e-05), [[MYH15]] (-0.50, fdr 8e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FRG1CP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.32×** | +16.8 | 0e+00 | 46/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.07×** | +15.7 | 0e+00 | 45/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.65×** | +13.6 | 6e-40 | 42/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +7.3 | 3e-11 | 30/47 (C32, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +7.0 | 3e-10 | 32/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.7 | 1e-06 | 28/48 (NCI-H460, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.3 | 8e-06 | 18/44 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 5e-05 | 19/47 (KATO III, HOP62, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +4.6 | 2e-04 | 16/46 (SK-MEL-2, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.37×** | +4.4 | 7e-04 | 15/47 (KATO III, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 7e-04 | 14/46 (HepG2/C3A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.006 | 16/48 (C32, hTERT-HPNE, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.010 | 6/48 (SK-MEL-2, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.6 | 0.013 | 12/48 (LOX-IMVI, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +3.6 | 0.013 | 11/46 (A-427, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.013 | 11/48 (KATO III, SNU-423, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.025 | 10/48 (NCI-H2347, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.225×** | -20.8 | 0e+00 | 47/47 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.254×** | -10.0 | 4e-21 | 41/45 (KATO III, HOP62, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.272×** | -9.5 | 4e-19 | 40/46 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.323×** | -8.2 | 3e-14 | 35/45 (A498, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.429×** | -8.0 | 1e-13 | 34/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.336×** | -7.9 | 2e-13 | 32/45 (NCI-H1792, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.346×** | -7.7 | 8e-13 | 31/44 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.625×** | -6.5 | 5e-09 | 26/47 (HCT15, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.616×** | -6.4 | 1e-08 | 27/48 (Hs 766T, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.638×** | -6.2 | 2e-08 | 22/40 (KATO III, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -5.9 | 2e-07 | 26/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.672×** | -5.5 | 2e-06 | 23/47 (SW480, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -5.3 | 5e-06 | 22/47 (SNU-423, RKO, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.717×** | -4.6 | 2e-04 | 19/47 (HS-578T, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.713×** | -4.4 | 3e-04 | 16/47 (SHP-77, C-33 A, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.656×** | -4.0 | 0.002 | 13/47 (NCI-H661, CHP-212, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.750×** | -4.0 | 0.002 | 16/46 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0868× (z -16.1) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.0867× (z -9.3) |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.131× (z -15.2) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 17.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.08× (z +11.8) | [[Digitoxin (drug)]] 5 µM 0.345× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[SW1417 (line)]] | alt | 21.7 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.12× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -15.6) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 16.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.0428× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.13× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.115× (z -12.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 31.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.0) ⚠ cell-cycle shift, explains ~3% of this change | [[Dinaciclib (drug)]] 5 µM 0.117× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 14.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.89× (z +9.6) | — |
| [[A498 (line)]] | wt | 15.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0903× (z -14.9) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0675× (z -8.7) |
| [[HT-29 (line)]] | alt | 12.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.93× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -10.3) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 13.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.53× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 16.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0603× (z -14.7) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 11.8 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.7) ⚠ cell-cycle shift, explains ~3% of this change | [[Harringtonine (drug)]] 0.5 µM 0.219× (z -9.5) |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 31.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.73× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -10.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 7.40 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +8.6) ⚠ cell-cycle shift, explains ~3% of this change | — |
| [[A549 (line)]] | wt | 7.58 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +9.1) ⚠ cell-cycle shift, explains ~3% of this change | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -12.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 7.98 | 0 | 1 | — | [[TAK-733 (drug)]] 5 µM 0.0259× (z -9.1) |
| [[Hs 766T (line)]] | wt | 7.74 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0727× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 9.14 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0617× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 6.92 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.04× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -10.9) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0887× (z -9.5) |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -9.2) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -9.1) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -8.5) ⚠ cell-cycle shift, explains ~3% of this change |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AUH]] | +0.73 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[HACL1]] | +0.67 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.65 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[YPEL3]] | +0.64 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[CCDC28A]] | +0.64 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[MARCHF8]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CBX7]] | +0.63 | +0.39 / +0.71 | both halves | 5e-05 |  |
| [[TFDP2]] | +0.62 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ELP2]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[KLHDC3]] | +0.61 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[EXOSC5]] | +0.61 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[FBXO25]] | +0.61 | +0.43 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DESI1]] | -0.51 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[CYCS]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MYH15]] | -0.50 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[AKIRIN1]] | -0.50 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[ERCC6L2]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LIG4]] | -0.49 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[ACTR2]] | -0.49 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1CP]] | B | FRG1CP activity lowers COQ8A's level | lines that do not express FRG1CP (15) vs lines expressing it (35) | 1.40× higher at baseline in the lines without FRG1CP | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000291100, BDNF, GUCY1B1 |
| [[C2orf27A]] | B | C2orf27A activity raises COQ8A's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without C2orf27A | 0.088 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.4, -46.3); signed map (-19.0, 8.8). **Vector** length 116, 31.0% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +16.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +2.9 |
|  | [[NG25 (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +7.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +4.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.3 | -20.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.3 | -10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.7 | -9.5 |
|  | [[EX229 (drug)]] 5 µM |  | -6.4 | -8.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.4 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q8A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:226,940,286-226,987,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COQ8, SCAR9; previously CABC1, ADCK3 |
| Gene groups (HGNC) | ADCK family |
| Hallmark sets | KRAS_SIGNALING_DN, P53_PATHWAY |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI60](https://www.uniprot.org/uniprotkb/Q8NI60) (Atypical kinase COQ8A, mitochondrial):

> Atypical kinase involved in the biosynthesis of coenzyme Q, also named ubiquinone, an essential lipid-soluble electron transporter for aerobic cellular respiration. Its substrate specificity is still unclear: may act as a protein kinase that mediates phosphorylation of COQ3 (By similarity). According to other reports, acts as a small molecule kinase, possibly a lipid kinase that phosphorylates a prenyl lipid in the ubiquinone biosynthesis pathway, as suggested by its ability to bind coenzyme Q …

**Summary**, from NCBI Gene [56997](https://www.ncbi.nlm.nih.gov/gene/56997):

> This gene encodes a mitochondrial protein similar to yeast ABC1, which functions in an electron-transferring membrane protein complex in the respiratory chain. It is not related to the family of ABC transporter proteins. Expression of this gene is induced by the tumor suppressor p53 and in response to DNA damage, and inhibiting its expression partially suppresses p53-induced apoptosis. Alternatively spliced transcript variants have been found; however, their full-length nature has not been …

**Accessions** — [HGNC:16812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16812) · Entrez [56997](https://www.ncbi.nlm.nih.gov/gene/56997) · UniProt [Q8NI60](https://www.uniprot.org/uniprotkb/Q8NI60) · Ensembl [ENSG00000163050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163050)

## Data

Gene col 8624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8624); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8624]; `tensor/DDL_lfc|DDL_z.npy` [8624]; `embed/gene_vectors.npy` [8624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8624 or target_col == 8624). Every well: [[COQ8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
