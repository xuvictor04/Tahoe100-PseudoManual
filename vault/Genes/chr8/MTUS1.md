---
symbol: "MTUS1"
type: "gene"
col: 4971
ensembl_id: "ENSG00000129422"
name: "microtubule associated scaffold protein 1"
location: "8p22"
module: 8
arm: "+"
pooled_cpm: 90.71
n_lines_expressing: 33
n_dd_up: 24
n_dd_down: 36
n_dd_up_clean: 21
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 61
direction_downstream: 60
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MTUS1

*microtubule associated scaffold protein 1* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.55× (z +6.8, q 7e-09, up in 23 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (19 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.372× (z -15.8, q 0e+00, down in 25 of 31 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.427× (z -13.6, q 4e-40, down in 26 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD12]] (+0.68, fdr 7e-06), [[FRK]] (+0.63, fdr 7e-06), [[SAMD12-AS1]] (+0.63, fdr 7e-06); moves opposite to [[PLEKHG5]] (-0.55, fdr 3e-05), [[PDLIM7]] (-0.54, fdr 2e-05), [[STK10]] (-0.52, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 61 arrows point to it, the strongest [[SIDT1]] → it (grade B ⚠); 60 go from it, the strongest it → [[PLEKHA7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +6.8 | 7e-09 | 23/30 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +6.2 | 1e-07 | 23/30 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.58×** | +6.1 | 2e-07 | 23/33 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +5.9 | 5e-07 | 22/32 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 1e-06 | 18/31 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +5.6 | 2e-06 | 21/31 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +5.5 | 4e-06 | 20/31 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +5.4 | 5e-06 | 19/32 (COLO 205, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.42×** | +5.0 | 4e-05 | 19/31 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 2e-04 | 17/32 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.10×** | +4.5 | 3e-04 | 21/33 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +4.4 | 4e-04 | 19/30 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.96×** | +4.1 | 0.002 | 21/31 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.003 | 17/32 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.90×** | +3.9 | 0.004 | 18/30 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.008 | 16/31 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4971.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.372×** | -15.8 | 0e+00 | 25/31 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.380×** | -15.5 | 0e+00 | 26/31 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.407×** | -13.8 | 3e-41 | 26/30 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.426×** | -13.6 | 4e-40 | 22/31 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.427×** | -13.6 | 4e-40 | 26/31 (SW48, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.576×** | -12.5 | 8e-34 | 23/32 (SW48, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.456×** | -12.1 | 1e-31 | 21/26 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.481×** | -11.7 | 1e-29 | 23/31 (SW48, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -10.9 | 6e-26 | 23/31 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.513×** | -10.7 | 8e-25 | 23/31 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.532×** | -10.1 | 3e-22 | 27/31 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.559×** | -9.3 | 7e-19 | 24/31 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.467×** | -9.1 | 3e-18 | 21/28 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.540×** | -8.8 | 7e-17 | 22/31 (COLO 205, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -8.7 | 1e-16 | 20/31 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.658×** | -6.7 | 9e-10 | 22/31 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.747×** | -4.6 | 9e-05 | 18/30 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.749×** | -4.4 | 3e-04 | 16/31 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.691×** | -4.2 | 6e-04 | 18/31 (LoVo, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.526×** | -3.9 | 0.002 | 15/31 (LoVo, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.735×** | -3.5 | 0.009 | 12/32 (HepG2/C3A, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.741×** | -3.4 | 0.013 | 14/32 (SW48, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.817×** | -3.2 | 0.022 | 9/31 (HT-29, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.62 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 377 | 0 | 21 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -25.9) |
| [[SW48 (line)]] | wt | 515 | 0 | 14 (10 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -19.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.179× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 136 | 12 (1 ⚠) | 1 | [[Trametinib (drug)]] 0.5 µM 4.65× (z +12.0) | [[Auranofin (drug)]] 5 µM 0.257× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 90.8 | 6 (1 ⚠) | 7 (4 ⚠) | [[Binimetinib (drug)]] 0.05 µM 2.68× (z +10.2) | [[Ixazomib citrate (drug)]] 0.5 µM 0.240× (z -11.2) |
| [[SW1417 (line)]] | alt | 177 | 0 | 13 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -19.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.268× (z -14.1) |
| [[COLO 205 (line)]] | alt | 187 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -21.0) |
| [[Panc 03.27 (line)]] | alt | 178 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -16.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.375× (z -14.4) |
| [[HT-29 (line)]] | alt | 127 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -18.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 83.2 | 0 | 11 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.130× (z -15.9) |
| [[LS 180 (line)]] | wt | 139 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -19.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.330× (z -12.3) |
| [[A549 (line)]] | wt | 171 | 2 | 7 (5 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 3.36× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -15.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -10.1) |
| [[BT-474 (line)]] | alt | 152 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -18.5) |
| [[KATO III (line)]] | alt | 494 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0908× (z -23.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -8.9) |
| [[LoVo (line)]] | wt | 241 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -18.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.236× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 163 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.4) |
| [[SNU-423 (line)]] | alt | 73.6 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -12.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.5) |
| [[A498 (line)]] | wt | 84.8 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.3) | [[Ixazomib citrate (drug)]] 5 µM 0.317× (z -9.1) |
| [[SW480 (line)]] | alt | 32.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -11.6) |
| [[A-172 (line)]] | wt | 33.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +23.2) | — |
| [[AN3 CA (line)]] | alt | 271 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.8) |
| [[A-427 (line)]] | wt | 32.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 189 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SHP-77 (line)]] | alt | 226 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.6) |
| [[SW 900 (line)]] | alt | 81.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 74.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SNU-1 (line)]] | wt | 37.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.165× (z -9.8) |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD12]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[FRK]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SAMD12-AS1]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SHROOM3]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 | same gene group |
| [[RBM47]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 | same gene group |
| [[TOX3]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[FAAH2]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[FGL1]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CCSER1]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MMP7]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HNF4G]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHG5]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[PDLIM7]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[STK10]] | -0.52 | -0.51 / -0.49 | both halves | 2e-05 |  |
| [[S100A16]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PPP4R1L]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PARVB]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[LINC00941]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ITGB1BP1]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 49, C 12. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIDT1]] | B | SIDT1 activity raises MTUS1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 4.07× lower at baseline in the lines without SIDT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[CLIC5]] | B | CLIC5 activity raises MTUS1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.98× lower at baseline in the lines without CLIC5 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[PLSCR4]] | B | PLSCR4 activity raises MTUS1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without PLSCR4 | 0.006 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[RAPGEF5]] | B | RAPGEF5 activity raises MTUS1's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.81× lower at baseline in the lines without RAPGEF5 | 0.007 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[TNFRSF21]] | B | TNFRSF21 activity raises MTUS1's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 4.16× lower at baseline in the lines without TNFRSF21 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[TMPRSS2]] | B | TMPRSS2 activity raises MTUS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.06× lower at baseline in the lines without TMPRSS2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[FGL1]] | B | FGL1 activity raises MTUS1's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 4.59× lower at baseline in the lines without FGL1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[RBM47]] | B | RBM47 activity raises MTUS1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 3.50× lower at baseline in the lines without RBM47 | 0.008 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[PROM1]] | B | PROM1 activity raises MTUS1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 4.48× lower at baseline in the lines without PROM1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[FGG]] | B | FGG activity raises MTUS1's level | lines that do not express FGG (42) vs lines expressing it (8) | 3.88× lower at baseline in the lines without FGG | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |
| [[SYNPR-AS1]] | B | SYNPR-AS1 activity raises MTUS1's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.38× lower at baseline in the lines without SYNPR-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[PBX1]] | B | PBX1 activity raises MTUS1's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.97× lower at baseline in the lines without PBX1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |

### Downstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 48, C 12. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA7]] | B | MTUS1 activity raises PLEKHA7's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.74× lower at baseline in the lines without MTUS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[USP6NL]] | B | MTUS1 activity raises USP6NL's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 1.96× lower at baseline in the lines without MTUS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[DAPK2]] | B | MTUS1 activity raises DAPK2's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without MTUS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[TMC5]] | B | MTUS1 activity raises TMC5's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.55× lower at baseline in the lines without MTUS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[ZNF703]] | B | MTUS1 activity raises ZNF703's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.24× lower at baseline in the lines without MTUS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[ERBB3]] | B | MTUS1 activity raises ERBB3's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.59× lower at baseline in the lines without MTUS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[TNFRSF21]] | B | MTUS1 activity raises TNFRSF21's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.84× lower at baseline in the lines without MTUS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[EPS8]] | B | MTUS1 activity raises EPS8's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.22× lower at baseline in the lines without MTUS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[SLC44A3-AS1]] | B | MTUS1 activity raises SLC44A3-AS1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.30× lower at baseline in the lines without MTUS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[GAREM1]] | B | MTUS1 activity raises GAREM1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.81× lower at baseline in the lines without MTUS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[CLIC5]] | B | MTUS1 activity raises CLIC5's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.71× lower at baseline in the lines without MTUS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[ST14]] | B | MTUS1 activity raises ST14's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 4.71× lower at baseline in the lines without MTUS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 51.4); signed map (57.9, 1.4). **Vector** length 126, 39.1% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +5.1 | +6.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.9 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +5.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.0 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +4.4 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -10.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated scaffold protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,643,795-17,801,094 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MTSG1, KIAA1288, DKFZp586D1519, FLJ14295, ATIP1, MP44, ATBP, ICIS |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULD2](https://www.uniprot.org/uniprotkb/Q9ULD2) (Microtubule-associated tumor suppressor 1):

> Cooperates with AGTR2 to inhibit ERK2 activation and cell proliferation. May be required for AGTR2 cell surface expression. Together with PTPN6, induces UBE2V2 expression upon angiotensin-II stimulation. Isoform 1 inhibits breast cancer cell proliferation, delays the progression of mitosis by prolonging metaphase and reduces tumor growth.

**Summary**, from NCBI Gene [57509](https://www.ncbi.nlm.nih.gov/gene/57509):

> This gene encodes a protein which contains a C-terminal domain able to interact with the angiotension II (AT2) receptor and a large coiled-coil region allowing dimerization. Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. One of the transcript variants has been shown to encode a mitochondrial protein that acts as a tumor suppressor and partcipates in AT2 signaling pathways. Other variants may encode nuclear or transmembrane proteins …

**Accessions** — [HGNC:29789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29789) · Entrez [57509](https://www.ncbi.nlm.nih.gov/gene/57509) · UniProt [Q9ULD2](https://www.uniprot.org/uniprotkb/Q9ULD2) · Ensembl [ENSG00000129422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129422)

## Data

Gene col 4971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4971); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4971]; `tensor/DDL_lfc|DDL_z.npy` [4971]; `embed/gene_vectors.npy` [4971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4971 or target_col == 4971). Every well: [[MTUS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTUS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
