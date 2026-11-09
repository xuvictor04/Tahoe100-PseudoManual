---
symbol: "MAT2B"
type: "gene"
col: 451
ensembl_id: "ENSG00000038274"
name: "methionine adenosyltransferase 2 non-catalytic beta subunit"
location: "5q34"
module: 130
arm: "+"
pooled_cpm: 33.13
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# MAT2B

*methionine adenosyltransferase 2 non-catalytic beta subunit* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.08× (z +10.9, q 5e-25, up in 28 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.42× (z +7.8, q 1e-12, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.528× (z -9.9, q 2e-20, down in 43 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.435× (z -6.8, q 4e-09, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BROX]] (+0.72, fdr 7e-06), [[PLEKHA3]] (+0.69, fdr 7e-06), [[NBR1]] (+0.68, fdr 7e-06); moves opposite to [[MPP3]] (-0.58, fdr 1e-05), [[MYO19]] (-0.57, fdr 1e-05), [[GARNL3]] (-0.55, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02985]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +10.9 | 5e-25 | 28/36 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +10.4 | 9e-23 | 38/45 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +7.8 | 1e-12 | 34/48 (SK-MEL-2, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.66×** | +7.6 | 5e-12 | 35/48 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.1 | 2e-10 | 36/48 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.32×** | +6.1 | 1e-07 | 26/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.41×** | +5.3 | 9e-06 | 30/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.8 | 1e-04 | 23/46 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +4.5 | 5e-04 | 21/47 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.005 | 19/48 (LoVo, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.008 | 20/48 (A549, A-427, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.011 | 18/48 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.019 | 17/47 (AsPC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.039 | 20/48 (SK-MEL-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.061 | 16/48 (C32, SNU-423, …) | inconsistent across doses | position effect removed |
| [[DTP3 (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.071 | 16/47 (hTERT-HPNE, LS 180, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.528×** | -9.9 | 2e-20 | 43/48 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.435×** | -6.8 | 4e-09 | 36/48 (AsPC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -6.5 | 2e-08 | 32/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -5.5 | 4e-06 | 27/48 (NCI-H460, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.723×** | -5.1 | 4e-05 | 26/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.723×** | -5.0 | 4e-05 | 29/47 (HCT15, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.564×** | -4.7 | 3e-04 | 23/48 (RPMI-7951, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.574×** | -4.5 | 4e-04 | 29/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.749×** | -4.5 | 4e-04 | 25/48 (AsPC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.609×** | -4.3 | 0.001 | 20/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.596×** | -4.2 | 0.001 | 23/48 (AsPC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.609×** | -4.0 | 0.003 | 20/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.776×** | -3.7 | 0.008 | 20/48 (Hs 766T, C-33 A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.800×** | -3.5 | 0.021 | 18/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.027 | 20/48 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.047 | 18/48 (HT-29, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.9) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.409× (z -9.4) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 45.9 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -10.1) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.364× (z -9.1) |
| [[J82 (line)]] | alt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.23× (z +9.2) | — |
| [[SW480 (line)]] | alt | 34.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 36.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.2) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[A549 (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +8.6) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[H4 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.173× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HCT15 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -9.8) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.8) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.400× (z -9.6) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.191× (z -8.8) |
| [[SNU-423 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.25× (z +9.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0870× (z -9.0) |
| [[SW1417 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.397× (z -8.7) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BROX]] | +0.72 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[PLEKHA3]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[NBR1]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[FBXO8]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[SEPSECS]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TRMT1L]] | +0.62 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CRNKL1]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[FMR1]] | +0.61 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[RBM22]] | +0.61 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[CREBL2]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[CILK1]] | +0.61 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[CDKN1B]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[MYO19]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[GARNL3]] | -0.55 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[CAPN15]] | -0.54 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ITGB1BP1]] | -0.54 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[CORO7]] | -0.53 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[RABEPK]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NCLN]] | -0.53 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[BUD23]] | -0.52 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[ST6GALNAC6-1]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[DAP3]] | -0.51 | -0.56 / -0.40 | both halves | 5e-05 | STRING 484 |
| [[CTC-338M12.4]] | -0.50 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02985]] | B | LINC02985 activity lowers MAT2B's level | lines that do not express LINC02985 (15) vs lines expressing it (35) | 1.39× higher at baseline in the lines without LINC02985 | 0.005 | ⚠ within organs, on part of the lines; also absent: GXYLT2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.5, -47.2); signed map (8.6, -27.3). **Vector** length 104, 26.7% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.9 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +7.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.7 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.8 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | +0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.9 | -9.9 |
|  | [[EX229 (drug)]] 5 µM |  | -6.2 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.6 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.1 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | methionine adenosyltransferase 2 non-catalytic beta subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:163,503,114-163,519,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MATIIbeta, SDR23E1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 5 pathways, smallest: Methylation; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZL9](https://www.uniprot.org/uniprotkb/Q9NZL9) (Methionine adenosyltransferase 2 subunit beta):

> Regulatory subunit of S-adenosylmethionine synthetase 2, an enzyme that catalyzes the formation of S-adenosylmethionine from methionine and ATP. Regulates MAT2A catalytic activity by changing its kinetic properties, increasing its affinity for L-methionine. Can bind NADP (in vitro).

**Summary**, from NCBI Gene [27430](https://www.ncbi.nlm.nih.gov/gene/27430):

> The protein encoded by this gene belongs to the methionine adenosyltransferase (MAT) family. MAT catalyzes the biosynthesis of S-adenosylmethionine from methionine and ATP. This protein is the regulatory beta subunit of MAT. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:6905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6905) · Entrez [27430](https://www.ncbi.nlm.nih.gov/gene/27430) · UniProt [Q9NZL9](https://www.uniprot.org/uniprotkb/Q9NZL9) · Ensembl [ENSG00000038274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038274)

## Data

Gene col 451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 451); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 451]; `tensor/DDL_lfc|DDL_z.npy` [451]; `embed/gene_vectors.npy` [451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 451 or target_col == 451). Every well: [[MAT2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAT2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
