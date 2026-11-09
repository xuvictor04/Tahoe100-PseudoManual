---
symbol: "GBE1"
type: "gene"
col: 3558
ensembl_id: "ENSG00000114480"
name: "1,4-alpha-glucan branching enzyme 1"
location: "3p12.2"
module: 99
arm: "+"
pooled_cpm: 801.34
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 31
n_dd_up_clean: 8
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# GBE1

*1,4-alpha-glucan branching enzyme 1* — 3p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.70× (z +8.9, q 3e-16, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.251× (z -32.8, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BNIP3]] (+0.65, fdr 1e-05), [[PFKFB3]] (+0.63, fdr 1e-05), [[ENO1]] (+0.63, fdr 7e-06); moves opposite to [[XRCC1]] (-0.45, fdr 1e-04), [[OSGEP]] (-0.43, fdr 4e-05), [[MCCC2]] (-0.42, fdr 1e-04).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +8.9 | 3e-16 | 38/46 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.4 | 5e-08 | 33/46 (SNU-1, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 1e-07 | 29/46 (SNU-1, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.8 | 1e-06 | 31/46 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.76×** | +5.0 | 7e-05 | 34/46 (HOP62, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.37×** | +5.0 | 7e-05 | 29/46 (LoVo, H4, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 6e-04 | 31/45 (NCI-H2030, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.001 | 25/45 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 26/46 (NCI-H1792, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.28×** | +4.0 | 0.004 | 26/45 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.007 | 28/47 (NCI-H2347, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 1.29× | +3.0 | 0.11 | 23/46 (HOP62, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.251×** | -32.8 | 0e+00 | 47/47 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.386×** | -22.6 | 0e+00 | 44/46 (HCT15, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.290×** | -20.0 | 0e+00 | 45/45 (RKO, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.333×** | -17.8 | 0e+00 | 40/42 (SK-MEL-2, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.365×** | -16.9 | 0e+00 | 44/47 (RKO, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.351×** | -16.9 | 0e+00 | 44/45 (SK-MEL-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.368×** | -16.8 | 0e+00 | 36/46 (RKO, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.368×** | -16.1 | 0e+00 | 43/46 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.386×** | -16.0 | 0e+00 | 36/46 (Panc 03.27, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.425×** | -14.4 | 4e-45 | 46/46 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.428×** | -14.3 | 2e-44 | 44/46 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.425×** | -13.8 | 9e-42 | 43/46 (C32, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.477×** | -12.4 | 8e-34 | 37/46 (RKO, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.467×** | -11.8 | 1e-30 | 36/43 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.641×** | -10.6 | 2e-24 | 44/46 (HOP62, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.593×** | -8.8 | 5e-17 | 36/46 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.729×** | -7.5 | 2e-12 | 30/46 (RKO, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.641×** | -7.5 | 2e-12 | 39/46 (RKO, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.657×** | -7.1 | 5e-11 | 36/46 (NCI-H1792, C-33 A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.454×** | -6.9 | 1e-10 | 36/47 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.722×** | -5.3 | 3e-06 | 36/46 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.713×** | -5.2 | 4e-06 | 38/45 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.815×** | -4.8 | 3e-05 | 27/46 (C-33 A, J82, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.590×** | -4.6 | 7e-05 | 32/47 (C32, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 1,329 | 0 | 21 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -31.7) |
| [[HEC-1-A (line)]] | alt | 1,077 | 3 (1 ⚠) | 17 (10 ⚠) | [[Auranofin (drug)]] 5 µM 2.86× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -29.2) |
| [[J82 (line)]] | alt | 1,095 | 1 (1 ⚠) | 19 (10 ⚠) | [[Trametinib (drug)]] 5 µM 1.88× (z +8.8) ⚠ cell-cycle shift, explains ~97% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -31.1) |
| [[LoVo (line)]] | wt | 298 | 8 (3 ⚠) | 12 (6 ⚠) | [[Auranofin (drug)]] 5 µM 4.97× (z +21.9) | [[Panobinostat (drug)]] 5 µM 0.177× (z -23.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.310× (z -15.8) |
| [[SW480 (line)]] | alt | 754 | 3 (1 ⚠) | 15 (10 ⚠) | [[Auranofin (drug)]] 5 µM 2.81× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -24.9) |
| [[LOX-IMVI (line)]] | wt | 615 | 4 (1 ⚠) | 13 (8 ⚠) | [[Trametinib (drug)]] 5 µM 2.68× (z +11.9) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.87× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -18.1) |
| [[HOP62 (line)]] | alt | 1,679 | 2 | 14 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -29.8) |
| [[RKO (line)]] | wt | 750 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -29.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -23.3) |
| [[SNU-423 (line)]] | alt | 1,208 | 0 | 16 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -31.0) |
| [[C32 (line)]] | wt | 1,309 | 2 (1 ⚠) | 13 (7 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 1.89× (z +9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.52× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -37.6) |
| [[NCI-H1573 (line)]] | alt | 781 | 0 | 15 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.188× (z -21.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 747 | 3 (1 ⚠) | 12 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -35.0) |
| [[NCI-H460 (line)]] | wt | 1,354 | 6 (2 ⚠) | 9 (5 ⚠) | [[Trametinib (drug)]] 5 µM 2.25× (z +10.2) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -28.2) |
| [[RPMI-7951 (line)]] | alt | 1,630 | 2 (1 ⚠) | 13 (7 ⚠) | [[Auranofin (drug)]] 5 µM 2.27× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -30.5) |
| [[A-172 (line)]] | wt | 739 | 4 (2 ⚠) | 10 (6 ⚠) | [[Auranofin (drug)]] 5 µM 3.14× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -20.8) |
| [[HepG2_C3A (line)]] | wt | 1,052 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -23.7) |
| [[MIA PaCa-2 (line)]] | alt | 1,541 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -30.2) |
| [[NCI-H23 (line)]] | alt | 514 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -18.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 453 | 1 | 13 (7 ⚠) | [[Auranofin (drug)]] 5 µM 3.75× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.119× (z -27.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -20.3) |
| [[SW 900 (line)]] | alt | 1,605 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -26.5) |
| [[A549 (line)]] | wt | 739 | 3 | 10 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 4.02× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -27.6) |
| [[HS-578T (line)]] | alt | 1,365 | 1 | 12 (7 ⚠) | [[Auranofin (drug)]] 5 µM 2.70× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -25.6) |
| [[hTERT-HPNE (line)]] | wt | 1,219 | 4 (1 ⚠) | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -20.2) |
| [[LS 180 (line)]] | wt | 571 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -17.8) |
| [[PANC-1 (line)]] | alt | 316 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -21.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -21.0) |
| [[SK-MEL-2 (line)]] | alt | 1,571 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -28.1) |
| [[CFPAC-1 (line)]] | alt | 587 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -25.1) |
| [[H4 (line)]] | wt | 1,217 | 2 (1 ⚠) | 10 (6 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.54× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -21.9) |
| [[NCI-H2347 (line)]] | alt | 814 | 2 | 10 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 5.53× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -20.5) |
| [[SNU-1 (line)]] | wt | 699 | 5 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.73× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -17.5) |
| [[SW48 (line)]] | wt | 559 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.6) |
| [[AN3 CA (line)]] | alt | 964 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -21.6) |
| [[AsPC-1 (line)]] | alt | 583 | 1 | 9 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.99× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -18.0) |
| [[CHP-212 (line)]] | wt | 1,111 | 2 | 8 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.48× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -21.9) |
| [[Hs 766T (line)]] | wt | 329 | 3 | 7 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.277× (z -15.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -15.4) |
| [[HCT15 (line)]] | alt | 1,879 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -24.5) |
| [[SHP-77 (line)]] | alt | 773 | 1 | 8 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.82× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -19.5) |
| [[A498 (line)]] | wt | 353 | 2 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.211× (z -18.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -17.9) |
| [[COLO 205 (line)]] | alt | 415 | 2 (2 ⚠) | 6 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.80× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.207× (z -14.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.241× (z -12.9) |
| [[HT-29 (line)]] | alt | 215 | 1 | 6 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.21× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.225× (z -12.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.268× (z -10.6) |
| [[SW1417 (line)]] | alt | 268 | 2 (1 ⚠) | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.78× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.262× (z -16.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 743 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -21.4) |
| [[BT-474 (line)]] | alt | 336 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -11.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -11.2) |
| [[SW 1271 (line)]] | alt | 752 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -14.4) |
| [[NCI-H661 (line)]] | alt | 268 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -10.4) |
| [[SW 1088 (line)]] | alt | 1,002 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -12.8) |
| [[A-427 (line)]] | wt | 119 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 60.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 929 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 996 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BNIP3]] | +0.65 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[PFKFB3]] | +0.63 | +0.68 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[ENO1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 500 |
| [[EFCAB3P1]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[NGLY1]] | +0.58 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[GYS1]] | +0.58 | +0.59 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 999 |
| [[PGK1]] | +0.55 | +0.62 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 551 |
| [[NEAT1]] | +0.55 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[P4HA1]] | +0.54 | +0.64 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[LDHA]] | +0.54 | +0.63 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA; STRING 567 |
| [[FAM162A]] | +0.54 | +0.67 / +0.43 | both halves | 4e-05 | pathway: HALLMARK_HYPOXIA |
| [[FAM210A]] | +0.53 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC1]] | -0.45 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[OSGEP]] | -0.43 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MCCC2]] | -0.42 | -0.52 / -0.36 | both halves | 1e-04 | pathway: Diseases of metabolism |
| [[CDC14A]] | -0.41 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GBE1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[EPIC1]] | B | EPIC1 activity lowers GBE1's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.28× higher at baseline in the lines without EPIC1 | 0.071 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[FAM13A]] | B | FAM13A activity raises GBE1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without FAM13A | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[TOP1]] | B | TOP1 activity raises GBE1's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PAM]] | C | PAM activity raises GBE1's level | lines that do not express PAM (3) vs lines expressing it (47) | 4.31× lower at baseline in the lines without PAM | 0.011 | ⚠ few lines (3 vs 47); across organs; also absent: PARP3, OSBPL3, CRYBG3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, -16.1); signed map (-37.5, 29.0). **Vector** length 134, 56.2% of its response variance represented; |z| ≥ 3 in 2,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +16.0 | +8.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.1 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +7.8 | -16.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.5 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +7.3 | -12.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.8 | +4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.6 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.8 | +5.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.9 | -16.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.5 | -14.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.8 | -20.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -16.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -2.7 | -1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | 1,4-alpha-glucan branching enzyme 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p12.2 — chr3:81,489,703-81,761,645 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | HYPOXIA, ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 6 pathways, smallest: Glycogen synthesis; Glycogen storage diseases; Glycogen metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04446](https://www.uniprot.org/uniprotkb/Q04446) (1,4-alpha-glucan-branching enzyme):

> Glycogen-branching enzyme participates in the glycogen biosynthetic process along with glycogenin and glycogen synthase. Generates alpha-1,6-glucosidic branches from alpha-1,4-linked glucose chains, to increase solubility of the glycogen polymer.

**Summary**, from NCBI Gene [2632](https://www.ncbi.nlm.nih.gov/gene/2632):

> The protein encoded by this gene is a glycogen branching enzyme that catalyzes the transfer of alpha-1,4-linked glucosyl units from the outer end of a glycogen chain to an alpha-1,6 position on the same or a neighboring glycogen chain. Branching of the chains is essential to increase the solubility of the glycogen molecule and, consequently, in reducing the osmotic pressure within cells. Highest level of this enzyme are found in liver and muscle. Mutations in this gene are associated with …

**Accessions** — [HGNC:4180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4180) · Entrez [2632](https://www.ncbi.nlm.nih.gov/gene/2632) · UniProt [Q04446](https://www.uniprot.org/uniprotkb/Q04446) · Ensembl [ENSG00000114480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114480)

## Data

Gene col 3558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3558); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3558]; `tensor/DDL_lfc|DDL_z.npy` [3558]; `embed/gene_vectors.npy` [3558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3558 or target_col == 3558). Every well: [[GBE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
