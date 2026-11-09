---
symbol: "ZCWPW2"
type: "gene"
col: 13049
ensembl_id: "ENSG00000206559"
name: "zinc finger CW-type and PWWP domain containing 2"
location: "3p24.1"
module: 23
arm: "+"
pooled_cpm: 17.66
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 30
n_dd_up_clean: 18
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ZCWPW2

*zinc finger CW-type and PWWP domain containing 2* — 3p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +12.4, q 1e-32, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.465× (z -11.5, q 1e-27, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.602× (z -7.6, q 2e-12, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKL3]] (+0.74, fdr 9e-06), [[ALOX12-AS1]] (+0.70, fdr 7e-06), [[ZNF546]] (+0.70, fdr 7e-06); moves opposite to [[SDHAF3]] (-0.63, fdr 1e-05), [[SLC29A1]] (-0.62, fdr 3e-05), [[FXN]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +12.4 | 1e-32 | 37/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.7 | 4e-04 | 18/48 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.7 | 4e-04 | 20/47 (LS 180, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.38×** | +4.6 | 5e-04 | 16/47 (RKO, RPMI-7951, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.5 | 8e-04 | 15/47 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 8e-04 | 19/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.003 | 9/48 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +4.0 | 0.003 | 15/47 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.30×** | +4.0 | 0.003 | 9/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.8 | 0.007 | 22/47 (LoVo, NCI-H1792, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.009 | 16/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.009 | 8/48 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.010 | 8/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.018 | 13/47 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.050 | 7/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.055 | 16/48 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.055 | 10/47 (C32, A-427, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.055 | 9/48 (KATO III, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.055 | 7/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.465×** | -11.5 | 1e-27 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.466×** | -11.0 | 1e-25 | 31/45 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.482×** | -10.9 | 2e-25 | 42/47 (PANC-1, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.530×** | -9.5 | 3e-19 | 37/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.539×** | -9.3 | 2e-18 | 35/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.554×** | -8.9 | 8e-17 | 37/48 (SW 900, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.584×** | -7.7 | 8e-13 | 28/47 (SW480, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -7.6 | 2e-12 | 27/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.508×** | -5.3 | 7e-06 | 20/48 (A-427, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.709×** | -5.1 | 2e-05 | 22/48 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.536×** | -4.9 | 5e-05 | 19/46 (LS 180, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.540×** | -4.8 | 7e-05 | 18/45 (RKO, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.542×** | -4.8 | 7e-05 | 16/48 (SNU-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.740×** | -4.5 | 3e-04 | 22/44 (NCI-H1573, HepG2/C3A, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.759×** | -4.1 | 0.001 | 19/48 (SW 900, C-33 A, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.753×** | -4.1 | 0.002 | 11/48 (C32, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Silodosin (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.002 | 10/47 (SW 1271, Panc 03.27, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.767×** | -4.0 | 0.002 | 10/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -3.9 | 0.003 | 21/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.785×** | -3.6 | 0.008 | 9/48 (NCI-H661, A-427, …) | inconsistent across doses |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.791×** | -3.5 | 0.012 | 10/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.014 | 11/48 (A498, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -3.4 | 0.020 | 14/48 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.668×** | -3.2 | 0.036 | 5/47 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.813×** | -3.0 | 0.064 | 8/48 (SW 1271, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.8 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.353× (z -8.8) |
| [[LoVo (line)]] | wt | 15.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.00× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.288× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 36.2 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 5.86× (z +11.0) | [[XRK3F2 (drug)]] 0.5 µM 0.118× (z -9.5) |
| [[A-427 (line)]] | wt | 22.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0637× (z -17.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.207× (z -10.4) |
| [[C32 (line)]] | wt | 25.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 14.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.142× (z -11.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 23.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0786× (z -15.2) ⚠ transcription drop; cell-cycle shift, explains ~84% of this change |
| [[SW48 (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Drospirenone (drug)]] 0.5 µM 0.0911× (z -9.3) |
| [[A549 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0623× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0966× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.04× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.132× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.293× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL3]] | +0.74 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[ALOX12-AS1]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[ZNF546]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[NIFK-AS1]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[PSMD7-DT]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TBCE-1]] | +0.67 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[HAVCR2]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CFAP43]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.66 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.66 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.63 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[SLC29A1]] | -0.62 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[FXN]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PTPN3]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[GNPTAB]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[CASP2]] | -0.58 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ACTR5]] | -0.58 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[METAP1]] | -0.58 | -0.67 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ZCWPW2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (9.6, 18.2); signed map (23.4, -2.2). **Vector** length 73.3, 14.1% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CW-type and PWWP domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.1 — chr3:28,348,721-28,538,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZCW2 |
| Gene groups (HGNC) | Zinc fingers CW-type; PWWP domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q504Y3](https://www.uniprot.org/uniprotkb/Q504Y3) (Zinc finger CW-type PWWP domain protein 2):

> Histone methylation reader which binds to non-methylated (H3K4me0), monomethylated (H3K4me1), dimethylated (H3K4me2) and trimethylated (H3K4me3) 'Lys-4' on histone H3. The order of binding preference is H3K4me3 > H3K4me2 > H3K4me1 > H3K4me0.

**Summary**, from NCBI Gene [152098](https://www.ncbi.nlm.nih.gov/gene/152098):

> Enables histone H3K4me3 reader activity. Predicted to be involved in chromatin organization. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23574) · Entrez [152098](https://www.ncbi.nlm.nih.gov/gene/152098) · UniProt [Q504Y3](https://www.uniprot.org/uniprotkb/Q504Y3) · Ensembl [ENSG00000206559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206559)

## Data

Gene col 13049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13049); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13049]; `tensor/DDL_lfc|DDL_z.npy` [13049]; `embed/gene_vectors.npy` [13049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13049 or target_col == 13049). Every well: [[ZCWPW2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCWPW2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
