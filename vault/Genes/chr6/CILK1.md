---
symbol: "CILK1"
type: "gene"
col: 3325
ensembl_id: "ENSG00000112144"
name: "ciliogenesis associated kinase 1"
location: "6p12.1"
module: 28
arm: "+"
pooled_cpm: 21.5
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 29
n_dd_up_clean: 18
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CILK1

*ciliogenesis associated kinase 1* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +10.8, q 2e-24, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.475× (z -11.1, q 5e-26, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF436]] (+0.70, fdr 7e-06), [[ZXDA]] (+0.69, fdr 2e-05), [[AASDHPPT]] (+0.68, fdr 1e-05); moves opposite to [[TMEM120B]] (-0.64, fdr 1e-05), [[LMBR1]] (-0.64, fdr 1e-05), [[MYO9B]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +10.8 | 2e-24 | 31/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +10.2 | 3e-22 | 37/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.5 | 1e-11 | 30/48 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +7.0 | 3e-10 | 34/48 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.2 | 5e-08 | 23/42 (SK-MEL-2, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 4e-05 | 21/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.8 | 2e-04 | 21/46 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 4e-04 | 19/48 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.33×** | +4.4 | 6e-04 | 18/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.002 | 17/48 (HOP62, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.34×** | +4.1 | 0.002 | 15/48 (NCI-H23, RKO, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.003 | 14/47 (SW 900, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.005 | 13/48 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.19× | +3.8 | 0.006 | 19/48 (A-427, RKO, …) | top dose only | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.006 | 12/48 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.006 | 15/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.006 | 15/48 (CFPAC-1, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.011 | 11/48 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -11.1 | 5e-26 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.476×** | -11.1 | 5e-26 | 42/48 (SW48, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.491×** | -10.6 | 6e-24 | 41/46 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -9.8 | 2e-20 | 40/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.544×** | -9.1 | 1e-17 | 36/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.544×** | -9.1 | 1e-17 | 38/46 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.569×** | -8.4 | 3e-15 | 35/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.572×** | -7.9 | 3e-13 | 31/47 (SW480, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -7.6 | 2e-12 | 35/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.601×** | -7.6 | 2e-12 | 32/48 (C32, SNU-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.466×** | -5.7 | 5e-07 | 24/46 (PANC-1, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.479×** | -5.5 | 1e-06 | 30/47 (AsPC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.706×** | -5.2 | 1e-05 | 25/47 (SW480, C32, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.618×** | -5.1 | 1e-05 | 24/48 (Hs 766T, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.518×** | -5.0 | 3e-05 | 25/46 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.533×** | -4.7 | 7e-05 | 18/46 (SK-MEL-2, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.764×** | -4.0 | 0.002 | 19/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.704×** | -3.7 | 0.005 | 14/48 (KATO III, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.704×** | -3.7 | 0.005 | 15/48 (NCI-H460, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.610×** | -3.7 | 0.005 | 16/46 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.6 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -10.9) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.245× (z -10.4) |
| [[SW480 (line)]] | alt | 62.2 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -13.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.214× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.135× (z -12.5) |
| [[C32 (line)]] | wt | 43.4 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.213× (z -10.7) |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 2 (1 ⚠) | — | [[BAY1125976 (drug)]] 0.5 µM 0.0392× (z -10.1) |
| [[J82 (line)]] | alt | 12.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.151× (z -9.2) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -10.4) |
| [[A498 (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.0) | — |
| [[A549 (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 56.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -12.6) |
| [[HCT15 (line)]] | alt | 18.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.133× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.03× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 9.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +14.6) | — |
| [[RKO (line)]] | wt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 25.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.153× (z -9.0) |
| [[SNU-423 (line)]] | alt | 39.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -8.9) |
| [[SW48 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0831× (z -11.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF436]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZXDA]] | +0.69 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[AASDHPPT]] | +0.68 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[CFL2]] | +0.68 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[ZXDB]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BMI1]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ARMT1]] | +0.65 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[MED12]] | +0.65 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[CDKN1B]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[NFIX]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | -0.64 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[LMBR1]] | -0.64 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.63 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[TPST2]] | -0.63 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.62 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[TOMM5]] | -0.62 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TMEM41B]] | -0.61 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CORO7]] | -0.60 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[DIP2A]] | -0.60 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[SLC37A3]] | -0.60 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[DRD4]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[GNA12]] | -0.58 | -0.59 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CILK1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.7, 2.6); signed map (16.2, -30.9). **Vector** length 107, 26.8% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +10.4 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +6.6 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +3.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.4 | -9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.3 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -11.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.8 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -7.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.9 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | ciliogenesis associated kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:53,001,279-53,061,824 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRK, LCK2, KIAA0936, MGC46090; previously ICK |
| Gene groups (HGNC) | CILK1, MAK, MOK protein kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPZ9](https://www.uniprot.org/uniprotkb/Q9UPZ9) (Serine/threonine-protein kinase ICK):

> Required for ciliogenesis. Phosphorylates KIF3A (By similarity). Involved in the control of ciliary length. Regulates the ciliary localization of SHH pathway components as well as the localization of IFT components at ciliary tips (By similarity). May play a key role in the development of multiple organ systems and particularly in cardiac development (By similarity). Regulates intraflagellar transport (IFT) speed and negatively regulates cilium length in a cAMP and mTORC1 signaling-dependent …

**Summary**, from NCBI Gene [22858](https://www.ncbi.nlm.nih.gov/gene/22858):

> Eukaryotic protein kinases are enzymes that belong to a very extensive family of proteins which share a conserved catalytic core common with both serine/threonine and tyrosine protein kinases. This gene encodes an intestinal serine/threonine kinase harboring a dual phosphorylation site found in mitogen-activating protein (MAP) kinases. The protein localizes to the intestinal crypt region and is thought to be important in intestinal epithelial cell proliferation and differentiation. Alternative …

**Accessions** — [HGNC:21219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21219) · Entrez [22858](https://www.ncbi.nlm.nih.gov/gene/22858) · UniProt [Q9UPZ9](https://www.uniprot.org/uniprotkb/Q9UPZ9) · Ensembl [ENSG00000112144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112144)

## Data

Gene col 3325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3325); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3325]; `tensor/DDL_lfc|DDL_z.npy` [3325]; `embed/gene_vectors.npy` [3325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3325 or target_col == 3325). Every well: [[CILK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CILK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
