---
symbol: "TMEM181"
type: "gene"
col: 7096
ensembl_id: "ENSG00000146433"
name: "transmembrane protein 181"
location: "6q25.3"
module: 59
arm: "-"
pooled_cpm: 115.08
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TMEM181

*transmembrane protein 181* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.55× (z +13.6, q 3e-39, up in 43 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.23× (z +6.3, q 2e-08, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.694× (z -10.9, q 7e-25, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK39]] (+0.62, fdr 7e-06), [[SCLY]] (+0.61, fdr 1e-05), [[CMTM4]] (+0.60, fdr 1e-05); moves opposite to [[GALT]] (-0.61, fdr 8e-06), [[KMT2E]] (-0.60, fdr 2e-05), [[MARCKS]] (-0.60, fdr 2e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR2F2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +13.6 | 3e-39 | 43/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +10.1 | 2e-21 | 27/49 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.32×** | +8.6 | 1e-15 | 28/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +7.7 | 3e-12 | 25/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.27×** | +7.2 | 7e-11 | 26/44 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.24×** | +6.6 | 4e-09 | 24/49 (HOP62, NCI-H1792, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +6.6 | 4e-09 | 29/48 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +6.3 | 2e-08 | 25/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.20×** | +5.8 | 4e-07 | 21/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +5.5 | 3e-06 | 28/48 (NCI-H1792, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.43×** | +5.4 | 3e-06 | 26/48 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +4.9 | 4e-05 | 23/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +4.6 | 1e-04 | 16/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.14× | +4.2 | 0.001 | 16/48 (H4, SNU-423, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.13× | +3.9 | 0.004 | 11/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.13× | +3.8 | 0.004 | 10/48 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.015 | 12/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.12× | +3.5 | 0.017 | 14/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.11× | +3.2 | 0.044 | 4/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.10× | +3.0 | 0.065 | 9/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.068 | 11/49 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.068 | 10/48 (MIA PaCa-2, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.07× | +2.9 | 0.085 | 1/48 (SW 1088) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.07× | +2.9 | 0.087 | 1/48 (SNU-1) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.07× | +2.9 | 0.089 | 5/49 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.694×** | -10.9 | 7e-25 | 36/48 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.592×** | -8.0 | 4e-13 | 27/49 (LS 180, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.853× | -5.8 | 2e-06 | 14/48 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.838× | -5.5 | 7e-06 | 16/49 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.862× | -4.6 | 5e-04 | 17/49 (NCI-H1792, SW48, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.819×** | -4.1 | 0.004 | 17/48 (RPMI-7951, SW48, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.872× | -4.1 | 0.004 | 17/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.878× | -4.0 | 0.004 | 13/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.891× | -3.8 | 0.009 | 11/48 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.892× | -3.8 | 0.009 | 11/49 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.887× | -3.7 | 0.010 | 17/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.919× | -3.7 | 0.011 | 5/48 (KATO III, SW1417, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.809×** | -3.2 | 0.056 | 16/47 (H4, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.928× | -3.1 | 0.068 | 3/49 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.925× | -3.1 | 0.068 | 10/50 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | 0.908× | -3.0 | 0.095 | 5/48 (A-427, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.8 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 93.0 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.352× (z -16.4) |
| [[A498 (line)]] | wt | 89.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.473× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 355 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.323× (z -13.5) |
| [[LS 180 (line)]] | wt | 182 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.376× (z -13.6) |
| [[SNU-1 (line)]] | wt | 127 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.327× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[AsPC-1 (line)]] | alt | 167 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.303× (z -15.3) |
| [[HOP62 (line)]] | alt | 93.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1792 (line)]] | alt | 78.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 98.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0715× (z -29.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 151 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.522× (z -8.6) |
| [[SW 900 (line)]] | alt | 107 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.341× (z -13.4) |
| [[SW1417 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.545× (z -9.9) |
| [[A-427 (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.209× (z -8.6) ⚠ toxic |
| [[C32 (line)]] | wt | 99.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0649× (z -16.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 49.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 96.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 87.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.481× (z -9.1) |
| [[J82 (line)]] | alt | 132 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.567× (z -8.7) |
| [[KATO III (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.543× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[NCI-H2030 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +10.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Panc 03.27 (line)]] | alt | 123 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.498× (z -9.2) |
| [[PANC-1 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.78× (z +11.6) ⚠ unreliable plate only | — |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.64× (z +8.6) ⚠ unreliable plate only | — |
| [[A-172 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 143 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 151 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK39]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[SCLY]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CMTM4]] | +0.60 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.60 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[LRP8]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ATAD3A]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[WDR4]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[GART]] | +0.59 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[MACROD1]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[LETM1]] | +0.57 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[UBE2G2]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALT]] | -0.61 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[KMT2E]] | -0.60 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[MARCKS]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[C2orf74-DT]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ING3]] | -0.57 | -0.40 / -0.62 | both halves | 4e-05 |  |
| [[ZSCAN26]] | -0.57 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[KMT2A]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[RAB30]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ZNF292]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TAB2]] | -0.55 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[LINC01273]] | -0.55 | -0.36 / -0.63 | both halves | 1e-04 |  |
| [[IGSF1]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F2-AS1]] | B | NR2F2-AS1 activity lowers TMEM181's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.83× higher at baseline in the lines without NR2F2-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[RFLNB]] | B | RFLNB activity raises TMEM181's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.03× lower at baseline in the lines without RFLNB | 0.055 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[CFAP300]] | B | CFAP300 activity lowers TMEM181's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 1.46× higher at baseline in the lines without CFAP300 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |
| [[ABCA1]] | B | ABCA1 activity lowers TMEM181's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 1.35× higher at baseline in the lines without ABCA1 | 0.068 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.6, -36.9); signed map (-1.3, -53.5). **Vector** length 121, 32.4% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.9 | +13.6 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.7 | +6.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.6 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.4 | +3.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -10.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.2 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -5.1 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -8.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.3 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 181 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:158,536,436-158,635,433 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1423, GPR178 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2C4](https://www.uniprot.org/uniprotkb/Q9P2C4) (Transmembrane protein 181):

> Mediates action of cytolethal distending toxins (CDT), which are secreted by many pathogenic bacteria. Expression level of TMEM181 is rate-limiting for intoxication.

**Summary**, from NCBI Gene [57583](https://www.ncbi.nlm.nih.gov/gene/57583):

> The TMEM181 gene encodes a putative G protein-coupled receptor expressed on the cell surface (Carette et al., 2009 [PubMed 19965467]; Wollscheid et al., 2009 [PubMed 19349973]).[supplied by OMIM, Jan 2010]

**Accessions** — [HGNC:20958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20958) · Entrez [57583](https://www.ncbi.nlm.nih.gov/gene/57583) · UniProt [Q9P2C4](https://www.uniprot.org/uniprotkb/Q9P2C4) · Ensembl [ENSG00000146433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146433)

## Data

Gene col 7096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7096); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7096]; `tensor/DDL_lfc|DDL_z.npy` [7096]; `embed/gene_vectors.npy` [7096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7096 or target_col == 7096). Every well: [[TMEM181 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM181.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
