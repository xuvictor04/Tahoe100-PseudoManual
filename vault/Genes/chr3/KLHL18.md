---
symbol: "KLHL18"
type: "gene"
col: 3571
ensembl_id: "ENSG00000114648"
name: "kelch like family member 18"
location: "3p21.31"
module: 36
arm: "+"
pooled_cpm: 45.23
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# KLHL18

*kelch like family member 18* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.15× (z +15.5, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.556× (z -8.5, q 1e-14, down in 29 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.704× (z -5.1, q 7e-05, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLK]] (+0.60, fdr 1e-05), [[RRP12]] (+0.58, fdr 1e-05), [[ZNF787]] (+0.57, fdr 1e-05); moves opposite to [[P2RX4]] (-0.52, fdr 2e-05), [[NOTCH2NLC]] (-0.52, fdr 4e-05), [[SCYL3]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.15×** | +15.5 | 0e+00 | 49/49 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.28×** | +11.5 | 4e-28 | 42/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.72×** | +8.2 | 5e-14 | 40/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.65×** | +7.3 | 4e-11 | 33/47 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.59×** | +7.1 | 2e-10 | 35/48 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.59×** | +7.0 | 2e-10 | 37/48 (LS 180, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.53×** | +6.5 | 9e-09 | 34/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.49×** | +6.0 | 1e-07 | 32/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +5.5 | 3e-06 | 33/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +5.3 | 8e-06 | 31/48 (HCT15, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.2 | 9e-06 | 31/48 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 9e-05 | 23/48 (Hs 766T, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 3e-04 | 25/48 (MIA PaCa-2, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.30×** | +4.0 | 0.002 | 20/48 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.003 | 22/48 (KATO III, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.007 | 16/48 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.16× | +3.1 | 0.048 | 11/48 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.073 | 15/47 (SW48, SW1417, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.078 | 9/48 (MIA PaCa-2, A-172, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -8.5 | 1e-14 | 29/42 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.632×** | -6.9 | 1e-09 | 28/47 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.704×** | -5.1 | 7e-05 | 30/47 (LOX-IMVI, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.800×** | -4.7 | 3e-04 | 26/48 (AsPC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.747×** | -4.4 | 0.001 | 24/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.767×** | -4.0 | 0.006 | 25/48 (HS-578T, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.765×** | -3.9 | 0.008 | 23/47 (MIA PaCa-2, RKO, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.774×** | -3.9 | 0.008 | 21/48 (SHP-77, KATO III, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.837× | -3.7 | 0.012 | 19/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.032 | 20/48 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.787×** | -3.3 | 0.046 | 16/48 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.810×** | -3.2 | 0.074 | 17/49 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.095 | 21/49 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 28.1 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +10.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.7× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 66.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.66× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 72.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.15× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -14.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 46.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.96× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -24.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 72.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.71× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -19.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 46.4 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.45× (z +9.1) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 45.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.80× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 37.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.13× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 42.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.72× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 63.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -15.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 65.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.75× (z +10.0) | — |
| [[SW480 (line)]] | alt | 58.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +13.6) | — |
| [[A-172 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.2) |
| [[C32 (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0792× (z -19.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 19.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0895× (z -11.1) ⚠ toxic |
| [[HT-29 (line)]] | alt | 43.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.18× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -11.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 27.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.8× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 44.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.32× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.31× (z +8.8) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 49.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.54× (z +9.0) | — |
| [[NCI-H661 (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 45.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 46.9 | 0 | 1 | — | [[Posaconazole (drug)]] 0.5 µM 0.0513× (z -9.6) |
| [[SW48 (line)]] | wt | 53.9 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.82× (z +10.4) | — |
| [[A498 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLK]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RRP12]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ZNF787]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[DOK3]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CCDC138]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[MRPS28]] | +0.55 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[RRP7BP]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[NOP2]] | +0.54 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[RRP7BP-1]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[CHERP]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[GFOD2]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[HIRA]] | +0.53 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RX4]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NOTCH2NLC]] | -0.52 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SCYL3]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[BBS7]] | -0.49 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[HMGN2]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[BPNT1]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[RC3H2]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[STAG2]] | -0.48 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[STXBP3]] | -0.47 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[TNKS2]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[HACD2]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[FAM117A]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (35.1, -27.5); signed map (-49.1, -22.1). **Vector** length 110, 32.0% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +7.6 | +7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +15.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.7 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.4 | +2.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.8 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.3 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,282,917-47,346,816 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0795, FLJ13703 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O94889](https://www.uniprot.org/uniprotkb/O94889) (Kelch-like protein 18):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex required for mitotic progression and cytokinesis. The BCR(KLHL18) E3 ubiquitin ligase complex mediates the ubiquitination of AURKA leading to its activation at the centrosome which is required for initiating mitotic entry. Regulates light-and dark-dependent alpha-transducin localization changes in rod photoreceptors through UNC119 ubiquitination and degradation (By similarity). Preferentially ubiquitinates …

**Summary**, from NCBI Gene [23276](https://www.ncbi.nlm.nih.gov/gene/23276):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Involved in positive regulation of mitotic cell cycle phase transition and protein ubiquitination. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29120](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29120) · Entrez [23276](https://www.ncbi.nlm.nih.gov/gene/23276) · UniProt [O94889](https://www.uniprot.org/uniprotkb/O94889) · Ensembl [ENSG00000114648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114648)

## Data

Gene col 3571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3571); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3571]; `tensor/DDL_lfc|DDL_z.npy` [3571]; `embed/gene_vectors.npy` [3571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3571 or target_col == 3571). Every well: [[KLHL18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
