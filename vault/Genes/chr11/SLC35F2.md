---
symbol: "SLC35F2"
type: "gene"
col: 3152
ensembl_id: "ENSG00000110660"
name: "solute carrier family 35 member F2"
location: "11q22.3"
module: 1
arm: "+"
pooled_cpm: 49.04
n_lines_expressing: 47
n_dd_up: 34
n_dd_down: 23
n_dd_up_clean: 20
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SLC35F2

*solute carrier family 35 member F2* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.39× (z +35.1, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.546× (z -12.3, q 5e-32, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCFC2]] (+0.64, fdr 1e-05), [[ZNF121]] (+0.63, fdr 1e-05), [[POGLUT1]] (+0.61, fdr 1e-05); moves opposite to [[CBFA2T2]] (-0.55, fdr 3e-05), [[GNB2]] (-0.55, fdr 2e-05), [[RAB5B]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANKRD18A]] → it (grade B ⚠); 4 go from it, the strongest it → [[ABCE1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.39×** | +35.1 | 0e+00 | 39/44 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.77×** | +20.8 | 0e+00 | 34/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.78×** | +20.0 | 0e+00 | 42/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.79×** | +11.8 | 6e-30 | 33/44 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +11.4 | 3e-28 | 35/43 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.69×** | +10.7 | 1e-24 | 30/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +10.6 | 2e-24 | 33/44 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +10.6 | 2e-24 | 30/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.63×** | +9.9 | 2e-21 | 31/43 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.63×** | +9.5 | 1e-19 | 24/39 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +9.5 | 1e-19 | 32/46 (PANC-1, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.58×** | +9.3 | 5e-19 | 30/44 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +9.2 | 2e-18 | 31/44 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +8.4 | 1e-15 | 29/44 (SW48, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +6.7 | 1e-09 | 25/45 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 4e-06 | 22/44 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.59×** | +4.9 | 3e-05 | 20/45 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 3e-05 | 20/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +4.8 | 4e-05 | 20/44 (MIA PaCa-2, AsPC-1, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +4.8 | 5e-05 | 19/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.55×** | +4.7 | 7e-05 | 17/44 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 8e-05 | 17/44 (HOP62, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3152.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.546×** | -12.3 | 5e-32 | 31/45 (RKO, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.600×** | -10.4 | 8e-23 | 31/45 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.679×** | -8.0 | 3e-13 | 28/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -7.3 | 5e-11 | 6/45 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.752×** | -7.1 | 2e-10 | 30/45 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.704×** | -6.9 | 6e-10 | 22/44 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.723×** | -6.7 | 2e-09 | 25/45 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.761×** | -6.5 | 4e-09 | 26/45 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.739×** | -6.1 | 5e-08 | 24/44 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.819×** | -5.7 | 6e-07 | 20/45 (RKO, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.752×** | -5.6 | 1e-06 | 23/44 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.762×** | -5.5 | 2e-06 | 22/44 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.748×** | -5.4 | 2e-06 | 21/44 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.771×** | -5.3 | 5e-06 | 22/44 (MIA PaCa-2, LoVo, …) | two highest doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.812×** | -5.2 | 7e-06 | 21/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.628×** | -4.9 | 3e-05 | 16/44 (AsPC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.796×** | -4.6 | 1e-04 | 21/45 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 150 | 8 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +30.7) | [[Panobinostat (drug)]] 5 µM 0.459× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 70.4 | 3 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +20.2) | [[Adagrasib (drug)]] 0.05 µM 0.618× (z -16.6) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.374× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 83.1 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +17.4) | [[Adagrasib (drug)]] 0.05 µM 0.491× (z -20.5) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.333× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 33.9 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +23.0) | — |
| [[RKO (line)]] | wt | 124 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -17.9) |
| [[NCI-H460 (line)]] | wt | 38.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +21.2) | — |
| [[A-427 (line)]] | wt | 45.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +25.4) | — |
| [[KATO III (line)]] | alt | 62.5 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -9.0) |
| [[LS 180 (line)]] | wt | 56.4 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.311× (z -11.3) |
| [[SW480 (line)]] | alt | 70.4 | 3 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.21× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.366× (z -13.1) |
| [[A549 (line)]] | wt | 40.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +19.8) | — |
| [[Hs 766T (line)]] | wt | 29.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +18.3) | [[Selinexor (drug)]] 5 µM 0.329× (z -10.3) ⚠ cell-cycle shift, explains ~79% of this change |
| [[LoVo (line)]] | wt | 32.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +15.5) | — |
| [[SW48 (line)]] | wt | 69.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 33.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +15.9) | — |
| [[HEC-1-A (line)]] | alt | 83.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -11.6) |
| [[HOP62 (line)]] | alt | 16.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +16.8) | — |
| [[HT-29 (line)]] | alt | 42.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +15.3) | — |
| [[LOX-IMVI (line)]] | wt | 48.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +19.3) | [[Selinexor (drug)]] 5 µM 0.516× (z -8.8) ⚠ cell-cycle shift, explains ~79% of this change |
| [[NCI-H1792 (line)]] | alt | 38.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 72.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +15.4) | — |
| [[Panc 03.27 (line)]] | alt | 49.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +15.2) | — |
| [[CFPAC-1 (line)]] | alt | 34.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +21.0) | — |
| [[NCI-H2347 (line)]] | alt | 40.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.8) | — |
| [[SNU-423 (line)]] | alt | 29.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +19.0) | — |
| [[SW1417 (line)]] | alt | 50.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +15.7) | — |
| [[A498 (line)]] | wt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 32.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 87.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -8.8) |
| [[H4 (line)]] | wt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 47.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -9.3) |
| [[SW 900 (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.9) | — |
| [[A-172 (line)]] | wt | 9.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZNF121]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[DCAF17]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ZNF485]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TMA16]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[NOC3L]] | +0.60 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MAK16]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ATIC]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.55 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[GNB2]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[RAB5B]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[RETREG2]] | -0.52 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[RAB2A]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FTL]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[TMUB2]] | -0.52 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[HDAC6]] | -0.51 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TOM1]] | -0.51 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[PBXIP1]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TULP3]] | -0.51 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[MOSPD3]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD18A]] | B | ANKRD18A activity raises SLC35F2's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without ANKRD18A | 0.047 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[MAP2K1]] | B | MAP2K1 activity raises SLC35F2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCE1]] | C | SLC35F2 activity raises ABCE1's level | lines that do not express SLC35F2 (3) vs lines expressing it (47) | 1.67× lower at baseline in the lines without SLC35F2 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, TMEM132A, POLR3G; maybe low, not absent; its own permutation p |
| [[PBXIP1]] | C | SLC35F2 activity lowers PBXIP1's level | lines that do not express SLC35F2 (3) vs lines expressing it (47) | 1.39× higher at baseline in the lines without SLC35F2 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, TMEM132A, POLR3G; maybe low, not absent |
| [[CEP83]] | C | SLC35F2 activity raises CEP83's level | lines that do not express SLC35F2 (3) vs lines expressing it (47) | 1.79× lower at baseline in the lines without SLC35F2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, TMEM132A, POLR3G; maybe low, not absent; its own permutation p |
| [[E2F5]] | C | SLC35F2 activity raises E2F5's level | lines that do not express SLC35F2 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without SLC35F2 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, TMEM132A, POLR3G; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.4, -36.8); signed map (2.8, -42.9). **Vector** length 106, 31.3% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +35.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +20.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +20.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.0 | +9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +4.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.9 | -7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -10.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -6.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.5 | -8.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -4.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member F2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:107,790,991-107,928,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13018 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXU6](https://www.uniprot.org/uniprotkb/Q8IXU6) (Queuine/queuosine transporter SLC35F2):

> High affinity plasma membrane importer of the nucleobase queuine (q) and its nucleoside queuosine (Q), two bacterially derived micronutrients acquired from the gut microbiome and diet. Following cellular uptake, queuosine is incorporated at the wobble base (position 34) of tRNAs that decode histidine, tyrosine, aspartate, and asparagine codons, which is important for efficient translation. Also involved in choline transport, although the underlying transport mechanism remains to be elucidated.

**Summary**, from NCBI Gene [54733](https://www.ncbi.nlm.nih.gov/gene/54733):

> Enables choline transmembrane transporter activity. Involved in choline transport and tRNA queuosine(34) biosynthetic process from salvaged queuine. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23615) · Entrez [54733](https://www.ncbi.nlm.nih.gov/gene/54733) · UniProt [Q8IXU6](https://www.uniprot.org/uniprotkb/Q8IXU6) · Ensembl [ENSG00000110660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110660)

## Data

Gene col 3152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3152); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3152]; `tensor/DDL_lfc|DDL_z.npy` [3152]; `embed/gene_vectors.npy` [3152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3152 or target_col == 3152). Every well: [[SLC35F2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35F2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
