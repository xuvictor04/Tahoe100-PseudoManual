---
symbol: "MYLK"
type: "gene"
col: 792
ensembl_id: "ENSG00000065534"
name: "myosin light chain kinase"
location: "3q21.1"
module: 66
arm: "+"
pooled_cpm: 45.72
n_lines_expressing: 30
n_dd_up: 20
n_dd_down: 29
n_dd_up_clean: 14
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 17
direction_downstream: 7
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# MYLK

*myosin light chain kinase* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.83× (z +16.4, q 0e+00, up in 22 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.66× (z +11.3, q 2e-27, up in 20 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.425× (z -13.4, q 3e-38, down in 24 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPM1]] (+0.67, fdr 7e-06), [[MYH9]] (+0.64, fdr 2e-05), [[ANXA8]] (+0.61, fdr 1e-05); moves opposite to [[IL17RA]] (-0.55, fdr 3e-05), [[TMEM101]] (-0.54, fdr 9e-05), [[RP9P]] (-0.50, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 7 go from it, the strongest it → [[TPM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.83×** | +16.4 | 0e+00 | 22/26 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +15.4 | 0e+00 | 22/24 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +11.3 | 2e-27 | 20/28 (A-172, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +10.1 | 7e-22 | 19/24 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +7.5 | 7e-12 | 18/28 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.7 | 3e-04 | 13/28 (H4, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 3e-04 | 16/27 (C32, H4, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +4.6 | 3e-04 | 11/28 (C32, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 3e-04 | 13/28 (SK-MEL-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +4.5 | 4e-04 | 9/28 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +4.3 | 9e-04 | 12/28 (A-172, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 12/27 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.002 | 11/28 (H4, C32, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.002 | 12/28 (C32, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.011 | 11/28 (H4, LoVo, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.6 | 0.013 | 8/28 (HOP62, A549, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.013 | 9/28 (HepG2/C3A, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.035 | 10/28 (H4, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.425×** | -13.4 | 3e-38 | 24/28 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.440×** | -12.9 | 2e-35 | 25/28 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.496×** | -11.0 | 8e-26 | 24/28 (PANC-1, AN3 CA, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.522×** | -10.2 | 4e-22 | 24/28 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.554×** | -9.2 | 2e-18 | 21/28 (PANC-1, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -9.2 | 2e-18 | 22/28 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.689×** | -8.2 | 2e-14 | 16/28 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.619×** | -7.1 | 1e-10 | 18/28 (H4, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.642×** | -6.9 | 3e-10 | 16/28 (H4, J82, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -6.5 | 5e-09 | 19/28 (H4, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.663×** | -6.4 | 7e-09 | 16/27 (A-427, CHP-212, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.685×** | -5.7 | 6e-07 | 13/28 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -4.9 | 5e-05 | 13/27 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.817×** | -4.4 | 4e-04 | 14/28 (HT-29, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.696×** | -4.0 | 0.002 | 10/28 (PANC-1, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.621×** | -3.9 | 0.003 | 16/28 (H4, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.652×** | -3.5 | 0.015 | 10/28 (Panc 03.27, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 266 | 0 | 29 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0523× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0891× (z -15.3) |
| [[A-427 (line)]] | wt | 49.8 | 2 (1 ⚠) | 9 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.16× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.186× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -13.1) |
| [[PANC-1 (line)]] | alt | 47.9 | 1 | 10 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.82× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -17.2) |
| [[A-172 (line)]] | wt | 97.1 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +23.6) | — |
| [[J82 (line)]] | alt | 211 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.262× (z -13.1) |
| [[HT-29 (line)]] | alt | 58.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -15.0) |
| [[SNU-423 (line)]] | alt | 216 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +18.0) | [[Bortezomib (drug)]] 0.05 µM 0.409× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 104 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.2) |
| [[LoVo (line)]] | wt | 15.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.199× (z -10.4) |
| [[A498 (line)]] | wt | 93.0 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.303× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 42.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -9.2) |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -8.8) |
| [[CHP-212 (line)]] | wt | 157 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 24.1 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.23× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 123 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.308× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -9.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 43.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0595× (z -11.8) |
| [[HS-578T (line)]] | alt | 159 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +19.7) | — |
| [[SK-MEL-2 (line)]] | alt | 55.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.75× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 9.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.33 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM1]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 857 |
| [[MYH9]] | +0.64 | +0.48 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS; STRING 770 |
| [[ANXA8]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CDH2]] | +0.59 | +0.43 / +0.73 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[EML1]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[COL4A2]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CDC42]] | +0.57 | +0.38 / +0.51 | both halves | 6e-05 | pathway: RHO GTPase Effectors; STRING 658 |
| [[PIEZO2]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[COL4A1]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[WDR1]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[RFTN1]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MOXD1]] | +0.56 | +0.35 / +0.58 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TMEM101]] | -0.54 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[RP9P]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PEX11A]] | -0.48 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[SDHAF1]] | -0.47 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MRPS12]] | -0.47 | -0.20 / -0.49 | both halves | 7e-04 |  |
| [[C16orf91]] | -0.47 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[ZNF500]] | -0.47 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[C8orf76]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[SCNM1]] | -0.47 | -0.24 / -0.55 | both halves | 5e-04 |  |
| [[EGFL8]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ALKBH4]] | -0.46 | -0.24 / -0.53 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 6, C 11. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MYLK's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[OLFML2A]] | B | OLFML2A activity raises MYLK's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 2.81× lower at baseline in the lines without OLFML2A | 0.058 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[SYNPO]] | B | SYNPO activity raises MYLK's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 4.04× lower at baseline in the lines without SYNPO | 0.074 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[CCDC3]] | B | CCDC3 activity raises MYLK's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 5.56× lower at baseline in the lines without CCDC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[MXRA5]] | B | MXRA5 activity raises MYLK's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 3.93× lower at baseline in the lines without MXRA5 | 0.093 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476 |
| [[SUSD5]] | B | SUSD5 activity raises MYLK's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 3.35× lower at baseline in the lines without SUSD5 | 0.094 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9 |
| [[SLIT3]] | C | SLIT3 activity raises MYLK's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 4.72× lower at baseline in the lines without SLIT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[COL4A1]] | C | COL4A1 activity raises MYLK's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 6.07× lower at baseline in the lines without COL4A1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises MYLK's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 5.99× lower at baseline in the lines without COL5A1 | 0.015 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[NALCN]] | C | NALCN activity raises MYLK's level | lines that do not express NALCN (22) vs lines expressing it (28) | 4.10× lower at baseline in the lines without NALCN | 0.027 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[PIEZO2]] | C | PIEZO2 activity raises MYLK's level | lines that do not express PIEZO2 (30) vs lines expressing it (20) | 4.61× lower at baseline in the lines without PIEZO2 | 0.033 | ⚠ within organs, on part of the lines; also absent: AMPH, COLEC12, ANKRD30B; co-absent with the target |
| [[GPR176]] | C | GPR176 activity raises MYLK's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 4.85× lower at baseline in the lines without GPR176 | 0.035 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPM1]] | B | MYLK activity raises TPM1's level | lines that do not express MYLK (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without MYLK | 0.085 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1 |
| [[SDHAF1]] | B | MYLK activity raises SDHAF1's level | lines that do not express MYLK (20) vs lines expressing it (30) | 1.09× lower at baseline in the lines without MYLK | 0.093 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1 |
| [[COL4A1]] | C | MYLK activity raises COL4A1's level | lines that do not express MYLK (20) vs lines expressing it (30) | 7.13× lower at baseline in the lines without MYLK | 0.011 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |
| [[COL4A2]] | C | MYLK activity raises COL4A2's level | lines that do not express MYLK (20) vs lines expressing it (30) | 7.32× lower at baseline in the lines without MYLK | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |
| [[SLIT3]] | C | MYLK activity raises SLIT3's level | lines that do not express MYLK (20) vs lines expressing it (30) | 2.71× lower at baseline in the lines without MYLK | 0.041 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |
| [[MOXD1]] | C | MYLK activity raises MOXD1's level | lines that do not express MYLK (20) vs lines expressing it (30) | 2.91× lower at baseline in the lines without MYLK | 0.047 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |
| [[KIRREL3]] | C | MYLK activity raises KIRREL3's level | lines that do not express MYLK (20) vs lines expressing it (30) | 3.07× lower at baseline in the lines without MYLK | 0.087 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (58.0, 21.1); signed map (42.9, 20.8). **Vector** length 96.8, 25.2% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.2 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.7 | +15.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +7.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.3 |
| fall | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -9.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -11.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -6.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:123,610,049-123,884,332 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MLCK, smMLCK, MYLK1, MLCK1, KRP, Telokin, MLCK108, MLCK210 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Myosin light chain kinase family |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION, ADIPOGENESIS |
| Reactome | 6 pathways, smallest: RHO GTPases activate PAKs; Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15746](https://www.uniprot.org/uniprotkb/Q15746) (Myosin light chain kinase, smooth muscle):

> Calcium/calmodulin-dependent myosin light chain kinase implicated in smooth muscle contraction via phosphorylation of myosin light chains (MLC). Also regulates actin-myosin interaction through a non-kinase activity. Phosphorylates PTK2B/PYK2 and myosin light-chains. Involved in the inflammatory response (e.g. apoptosis, vascular permeability, leukocyte diapedesis), cell motility and morphology, airway hyperreactivity and other activities relevant to asthma. Required for tonic airway smooth …

**Summary**, from NCBI Gene [4638](https://www.ncbi.nlm.nih.gov/gene/4638):

> This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an intron in the 3' region, it encodes telokin, a small protein identical in sequence to the …

**Accessions** — [HGNC:7590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7590) · Entrez [4638](https://www.ncbi.nlm.nih.gov/gene/4638) · UniProt [Q15746](https://www.uniprot.org/uniprotkb/Q15746) · Ensembl [ENSG00000065534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065534)

## Data

Gene col 792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 792); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 792]; `tensor/DDL_lfc|DDL_z.npy` [792]; `embed/gene_vectors.npy` [792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 792 or target_col == 792). Every well: [[MYLK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYLK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
