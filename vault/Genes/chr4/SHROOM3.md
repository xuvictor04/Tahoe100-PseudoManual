---
symbol: "SHROOM3"
type: "gene"
col: 6234
ensembl_id: "ENSG00000138771"
name: "shroom family member 3"
location: "4q21.1"
module: 8
arm: "+"
pooled_cpm: 116.88
n_lines_expressing: 31
n_dd_up: 14
n_dd_down: 32
n_dd_up_clean: 13
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 48
direction_downstream: 61
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SHROOM3

*shroom family member 3* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.29× (z +6.6, q 3e-08, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.581× (z -13.9, q 4e-41, down in 25 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLAC8]] (+0.70, fdr 7e-06), [[EDN1]] (+0.64, fdr 7e-06), [[SORL1]] (+0.64, fdr 8e-06); moves opposite to [[FAM219A]] (-0.54, fdr 1e-05), [[CFAP20DC]] (-0.51, fdr 3e-05), [[TM4SF19]] (-0.50, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 48 arrows point to it, the strongest [[SLC44A3]] → it (grade B ⚠); 61 go from it, the strongest it → [[FGD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +6.6 | 3e-08 | 13/29 (NCI-H2347, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +6.1 | 4e-07 | 20/30 (A498, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +4.4 | 0.002 | 16/30 (LS 180, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.004 | 16/28 (AsPC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.004 | 14/29 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +4.1 | 0.004 | 19/29 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.007 | 17/29 (LS 180, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.012 | 13/29 (NCI-H1573, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +3.5 | 0.026 | 15/31 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.035 | 11/29 (SHP-77, A549, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.045 | 11/31 (AsPC-1, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.045 | 8/29 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.053 | 12/28 (AsPC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.055 | 12/29 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.055 | 11/29 (AsPC-1, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.055 | 7/30 (Panc 03.27, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -13.9 | 4e-41 | 25/30 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.479×** | -13.3 | 4e-38 | 27/29 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.511×** | -12.1 | 1e-31 | 26/29 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -10.1 | 5e-22 | 23/29 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.611×** | -8.9 | 5e-17 | 24/29 (LoVo, Hs 766T, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.615×** | -8.8 | 1e-16 | 26/29 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.623×** | -8.6 | 8e-16 | 23/29 (LoVo, Hs 766T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.616×** | -7.9 | 2e-13 | 24/29 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -7.6 | 3e-12 | 24/29 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.656×** | -7.3 | 1e-11 | 18/25 (C-33 A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.475×** | -7.0 | 1e-10 | 22/29 (LoVo, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -6.2 | 3e-08 | 16/29 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.533×** | -5.9 | 1e-07 | 20/27 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.696×** | -5.9 | 2e-07 | 20/26 (C-33 A, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.725×** | -5.8 | 2e-07 | 22/30 (C-33 A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.544×** | -5.8 | 3e-07 | 19/29 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.764×** | -4.9 | 4e-05 | 17/29 (LoVo, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.630×** | -4.4 | 3e-04 | 19/29 (LoVo, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.637×** | -4.3 | 5e-04 | 16/29 (CFPAC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.740×** | -3.9 | 0.003 | 10/29 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.003 | 13/29 (Panc 03.27, CFPAC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.793×** | -3.8 | 0.004 | 15/29 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 647 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -21.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.139× (z -20.5) |
| [[KATO III (line)]] | alt | 406 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -16.3) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -18.8) |
| [[SW1417 (line)]] | alt | 180 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 247 | 0 | 8 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.321× (z -11.6) |
| [[SW480 (line)]] | alt | 122 | 0 | 8 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.215× (z -19.5) |
| [[C-33 A (line)]] | alt | 704 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0724× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -13.3) |
| [[LS 180 (line)]] | wt | 395 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.306× (z -12.6) |
| [[A498 (line)]] | wt | 42.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.1) | — |
| [[BT-474 (line)]] | alt | 436 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 242 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.0) |
| [[HCT15 (line)]] | alt | 266 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.265× (z -11.8) |
| [[HT-29 (line)]] | alt | 192 | 0 | 4 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.220× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 151 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +19.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.1) |
| [[AN3 CA (line)]] | alt | 306 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 78.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -13.6) |
| [[SW48 (line)]] | wt | 161 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.174× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 128 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 56.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW 900 (line)]] | alt | 59.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +15.4) | — |
| [[A-172 (line)]] | wt | 54.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.96× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 58.8 | 1 | 0 | [[Trametinib (drug)]] 0.05 µM 2.25× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 47.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.77× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 47.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.2) |
| [[SHP-77 (line)]] | alt | 72.8 | 1 | 0 | [[Dexamethasone (drug)]] 0.5 µM 2.80× (z +8.6) | — |
| [[A-427 (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 431 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAC8]] | +0.70 | +0.59 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[EDN1]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SORL1]] | +0.64 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[MTUS1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 | same gene group |
| [[PLEKHG6]] | +0.62 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[ANK3]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SCNN1A]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ARHGEF38]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TOX3]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RNF43]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[DLEU1]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM219A]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[CFAP20DC]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[TM4SF19]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[GPAT3]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 15, C 33. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | SLC44A3 activity raises SHROOM3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.98× lower at baseline in the lines without SLC44A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SLC6A14]] | B | SLC6A14 activity raises SHROOM3's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.21× lower at baseline in the lines without SLC6A14 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[RNF43]] | B | RNF43 activity raises SHROOM3's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.56× lower at baseline in the lines without RNF43 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[PDLIM1]] | B | PDLIM1 activity raises SHROOM3's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without PDLIM1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[TMEM139]] | B | TMEM139 activity raises SHROOM3's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 3.10× lower at baseline in the lines without TMEM139 | 0.026 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[KCNMA1]] | B | KCNMA1 activity lowers SHROOM3's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 3.75× higher at baseline in the lines without KCNMA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[SH3BGRL2]] | B | SH3BGRL2 activity raises SHROOM3's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 3.06× lower at baseline in the lines without SH3BGRL2 | 0.047 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[FGD4]] | B | FGD4 activity raises SHROOM3's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 2.30× lower at baseline in the lines without FGD4 | 0.048 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[PHACTR3]] | B | PHACTR3 activity raises SHROOM3's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without PHACTR3 | 0.050 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises SHROOM3's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.20× lower at baseline in the lines without ATP8B1 | 0.053 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[SLC40A1]] | B | SLC40A1 activity raises SHROOM3's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.12× lower at baseline in the lines without SLC40A1 | 0.064 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SHROOM3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 31, C 30. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD4]] | B | SHROOM3 activity raises FGD4's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.95× lower at baseline in the lines without SHROOM3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[SLC44A3]] | B | SHROOM3 activity raises SLC44A3's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without SHROOM3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[FRK]] | B | SHROOM3 activity raises FRK's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.84× lower at baseline in the lines without SHROOM3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[ATP8B1]] | B | SHROOM3 activity raises ATP8B1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.91× lower at baseline in the lines without SHROOM3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[FOXO1]] | B | SHROOM3 activity raises FOXO1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without SHROOM3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[EFNA1]] | B | SHROOM3 activity raises EFNA1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without SHROOM3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[RNF43]] | B | SHROOM3 activity raises RNF43's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 3.08× lower at baseline in the lines without SHROOM3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[MAP3K1]] | B | SHROOM3 activity raises MAP3K1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without SHROOM3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[PLEKHA7]] | B | SHROOM3 activity raises PLEKHA7's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without SHROOM3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[PDLIM1]] | B | SHROOM3 activity raises PDLIM1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without SHROOM3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[RHOU]] | B | SHROOM3 activity raises RHOU's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without SHROOM3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[EHF]] | B | SHROOM3 activity raises EHF's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 4.43× lower at baseline in the lines without SHROOM3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 49.8); signed map (53.3, 10.9). **Vector** length 121, 35.9% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -13.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -7.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -7.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | shroom family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:76,435,229-76,783,253 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ShrmL, SHRM, KIAA1481, APXL3 |
| Gene groups (HGNC) | PDZ domain containing; MicroRNA protein coding host genes; Shroom family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF72](https://www.uniprot.org/uniprotkb/Q8TF72) (Protein Shroom3):

> Controls cell shape changes in the neuroepithelium during neural tube closure. Induces apical constriction in epithelial cells by promoting the apical accumulation of F-actin and myosin II, and probably by bundling stress fibers (By similarity). Induces apicobasal cell elongation by redistributing gamma-tubulin and directing the assembly of robust apicobasal microtubule arrays (By similarity).

**Summary**, from NCBI Gene [57619](https://www.ncbi.nlm.nih.gov/gene/57619):

> This gene encodes a PDZ-domain-containing protein that belongs to a family of Shroom-related proteins. This protein may be involved in regulating cell shape in certain tissues. A similar protein in mice is required for proper neurulation. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:30422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30422) · Entrez [57619](https://www.ncbi.nlm.nih.gov/gene/57619) · UniProt [Q8TF72](https://www.uniprot.org/uniprotkb/Q8TF72) · Ensembl [ENSG00000138771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138771)

## Data

Gene col 6234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6234); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6234]; `tensor/DDL_lfc|DDL_z.npy` [6234]; `embed/gene_vectors.npy` [6234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6234 or target_col == 6234). Every well: [[SHROOM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHROOM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
