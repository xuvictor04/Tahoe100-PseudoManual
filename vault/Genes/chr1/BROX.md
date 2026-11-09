---
symbol: "BROX"
type: "gene"
col: 8585
ensembl_id: "ENSG00000162819"
name: "BRO1 domain and CAAX motif containing"
location: "1q41"
module: 130
arm: "+"
pooled_cpm: 60.84
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# BROX

*BRO1 domain and CAAX motif containing* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +14.0, q 2e-41, up in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.38× (z +10.8, q 6e-25, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.604× (z -12.0, q 1e-30, down in 39 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.667× (z -9.7, q 1e-19, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAG2]] (+0.74, fdr 7e-06), [[RIMOC1]] (+0.73, fdr 7e-06), [[MAT2B]] (+0.72, fdr 7e-06); moves opposite to [[HIRA]] (-0.59, fdr 1e-05), [[MYO19]] (-0.58, fdr 1e-05), [[FOXK2]] (-0.58, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +14.0 | 2e-41 | 44/48 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +12.2 | 7e-32 | 30/41 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +10.8 | 6e-25 | 37/48 (PANC-1, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +6.8 | 2e-09 | 34/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +5.3 | 2e-05 | 26/44 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +5.0 | 5e-05 | 22/47 (RKO, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.15× | +4.7 | 2e-04 | 22/48 (NCI-H23, SK-MEL-2, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.46×** | +4.6 | 3e-04 | 26/47 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.5 | 4e-04 | 11/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +4.4 | 7e-04 | 18/49 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 18/49 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.0 | 0.003 | 20/48 (KATO III, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.6 | 0.015 | 16/49 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.4 | 0.025 | 17/48 (J82, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.029 | 10/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.077 | 7/48 (KATO III, C32, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.085 | 11/48 (LoVo, HEC-1-A, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.089 | 13/48 (SW480, SW 900, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.604×** | -12.0 | 1e-30 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -9.7 | 1e-19 | 38/48 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -9.6 | 2e-19 | 41/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -8.8 | 1e-16 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.713×** | -8.1 | 8e-14 | 36/48 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.626×** | -5.7 | 1e-06 | 30/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.727×** | -5.4 | 5e-06 | 27/48 (NCI-H1792, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.797×** | -5.4 | 5e-06 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.804×** | -5.2 | 1e-05 | 22/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.660×** | -5.0 | 3e-05 | 26/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.812×** | -5.0 | 3e-05 | 24/48 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.747×** | -5.0 | 3e-05 | 25/49 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.817×** | -4.8 | 7e-05 | 25/48 (PANC-1, NCI-H1792, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.823×** | -4.6 | 1e-04 | 21/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.762×** | -4.6 | 1e-04 | 22/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.825×** | -4.6 | 2e-04 | 22/48 (HCT15, A-172, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.686×** | -4.5 | 2e-04 | 23/48 (NCI-H460, RKO, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.819×** | -4.5 | 2e-04 | 21/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.693×** | -4.4 | 3e-04 | 19/48 (RKO, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.705×** | -4.2 | 7e-04 | 21/48 (NCI-H460, AsPC-1, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 60.0 | 2 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.28× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.62× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.432× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.539× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 73.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.392× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.522× (z -9.4) |
| [[SW480 (line)]] | alt | 55.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +9.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.453× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.454× (z -11.0) |
| [[A-427 (line)]] | wt | 46.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 87.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 54.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 83.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.468× (z -10.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 74.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.436× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.466× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 59.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 79.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 52.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +10.1) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 53.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.33× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 38.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.248× (z -8.5) |
| [[A-172 (line)]] | wt | 74.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -11.2) ⚠ cell-cycle shift, explains ~1% of this change |
| [[COLO 205 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -13.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.321× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +10.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 67.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 52.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.9) ⚠ cell-cycle shift, explains ~1% of this change | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 1 | 0 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 2.22× (z +497.8) | — |
| [[SK-MEL-2 (line)]] | alt | 59.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.4) ⚠ cell-cycle shift, explains ~1% of this change | — |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.254× (z -9.4) |
| [[SNU-423 (line)]] | alt | 76.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG2]] | +0.74 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[RIMOC1]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[MAT2B]] | +0.72 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[SF3B1]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CREBL2]] | +0.65 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[PLEKHA3]] | +0.64 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[FBXO8]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TDP2]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[VPS26A]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[CRNKL1]] | +0.61 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[RMND5A]] | +0.61 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[HINT3]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIRA]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[MYO19]] | -0.58 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[FOXK2]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[ZMYND19]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ZNF544]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TOMM5]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ATP5MC1]] | -0.57 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SDF2L1]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ANKS6]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[PAQR4]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[P3H4]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity lowers BROX's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.48× higher at baseline in the lines without NT5M | 0.042 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-20.0, 7.2); signed map (8.6, -27.9). **Vector** length 121, 32.8% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.0 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +14.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +6.3 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +6.2 | +5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.8 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.9 | -9.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -12.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.1 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -8.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -9.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.3 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | BRO1 domain and CAAX motif containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:222,712,553-222,735,196 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32421; previously C1orf58 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VW32](https://www.uniprot.org/uniprotkb/Q5VW32) (BRO1 domain-containing protein BROX):

> Nuclear envelope-associated factor that is involved in the nuclear envelope ruptures during interphase (NERDI) repair, where it is locally recruited by CHMP5 and reduces cytoskeletal stress through its action on SYN2 to help reseal the ruptured membrane.

**Summary**, from NCBI Gene [148362](https://www.ncbi.nlm.nih.gov/gene/148362):

> Involved in mitotic nuclear membrane reassembly. Located in nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26512) · Entrez [148362](https://www.ncbi.nlm.nih.gov/gene/148362) · UniProt [Q5VW32](https://www.uniprot.org/uniprotkb/Q5VW32) · Ensembl [ENSG00000162819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162819)

## Data

Gene col 8585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8585); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8585]; `tensor/DDL_lfc|DDL_z.npy` [8585]; `embed/gene_vectors.npy` [8585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8585 or target_col == 8585). Every well: [[BROX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BROX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
