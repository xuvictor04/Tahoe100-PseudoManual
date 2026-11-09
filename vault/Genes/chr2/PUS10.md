---
symbol: "PUS10"
type: "gene"
col: 8600
ensembl_id: "ENSG00000162927"
name: "pseudouridine synthase 10"
location: "2p16.1-p15"
module: 23
arm: "+"
pooled_cpm: 20.18
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 36
n_dd_up_clean: 19
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PUS10

*pseudouridine synthase 10* — 2p16.1-p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +12.3, q 3e-32, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.345× (z -17.0, q 0e+00, down in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.438× (z -13.2, q 2e-37, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD5]] (+0.65, fdr 1e-05), [[C2orf76]] (+0.65, fdr 1e-05), [[ZC3H6]] (+0.63, fdr 1e-05); moves opposite to [[ADAMTSL5]] (-0.65, fdr 7e-06), [[GPRIN1]] (-0.63, fdr 2e-05), [[EDA]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +12.3 | 3e-32 | 33/47 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.4 | 4e-08 | 21/46 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 3e-06 | 23/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.5 | 5e-06 | 24/48 (LoVo, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +5.0 | 5e-05 | 19/48 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +5.0 | 5e-05 | 21/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 1e-04 | 14/48 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.33×** | +4.2 | 0.002 | 14/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.002 | 10/48 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.003 | 11/48 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.008 | 14/48 (LoVo, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.012 | 12/47 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.021 | 9/48 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.021 | 7/47 (Hs 766T, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.023 | 10/47 (SW480, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.024 | 10/47 (A-172, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8600.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.345×** | -17.0 | 0e+00 | 39/46 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.438×** | -13.2 | 2e-37 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.459×** | -12.5 | 2e-33 | 41/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.502×** | -11.1 | 3e-26 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.555×** | -9.4 | 4e-19 | 31/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -8.9 | 6e-17 | 39/48 (NCI-H1792, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.581×** | -8.7 | 3e-16 | 25/42 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.370×** | -8.3 | 5e-15 | 31/44 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.603×** | -8.1 | 3e-14 | 32/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.649×** | -6.9 | 3e-10 | 29/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.687×** | -5.8 | 4e-07 | 25/44 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.710×** | -5.5 | 2e-06 | 23/44 (LS 180, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.723×** | -5.2 | 9e-06 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.732×** | -5.0 | 2e-05 | 22/46 (AN3 CA, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.725×** | -4.9 | 4e-05 | 19/48 (NCI-H1573, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.813×** | -4.7 | 9e-05 | 23/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.710×** | -3.9 | 0.002 | 15/46 (MIA PaCa-2, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.784×** | -3.9 | 0.002 | 16/46 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.780×** | -3.8 | 0.003 | 15/47 (H4, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.790×** | -3.8 | 0.003 | 15/47 (RPMI-7951, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.9 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -18.6) |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -11.6) |
| [[SW480 (line)]] | alt | 17.8 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.253× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 28.0 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.235× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 70.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.136× (z -9.3) |
| [[A-427 (line)]] | wt | 37.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -9.7) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.183× (z -8.6) |
| [[KATO III (line)]] | alt | 18.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.133× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 23.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -11.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0779× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0572× (z -13.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 8.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 49.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -8.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -9.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0804× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0806× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW1417 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.0) | — |
| [[A549 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD5]] | +0.65 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[C2orf76]] | +0.65 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ZC3H6]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[NMNAT1]] | +0.61 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[CFAP418]] | +0.60 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[TSTD3]] | +0.59 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[DDX59]] | +0.58 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[MFSD8]] | +0.58 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[FAM76B]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[RBM43]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PDHX]] | +0.55 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[DICER1-AS1]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL5]] | -0.65 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[GPRIN1]] | -0.63 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[EDA]] | -0.63 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[GPR153]] | -0.62 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[KIF21B]] | -0.60 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[CORO1C]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[KCTD17]] | -0.57 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[GDF11]] | -0.57 | -0.20 / -0.49 | ⚠ not reproduced | 7e-04 |  |
| [[MICAL2]] | -0.57 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[UNC5A]] | -0.57 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[MIR222HG]] | -0.57 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[GDPD5]] | -0.56 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[ATP1A3]] | -0.55 | -0.23 / -0.42 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PUS10's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers PUS10's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-0.1, 15.6); signed map (23.3, -11.0). **Vector** length 71.2, 13.7% of its response variance represented; |z| ≥ 3 in 1,246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -12.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.9 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -5.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.2 | -3.9 |
|  | [[vincristine (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | pseudouridine synthase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1-p15 — chr2:60,940,222-61,018,259 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32312; previously CCDC139 |
| Gene groups (HGNC) | Pseudouridine synthases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3MIT2](https://www.uniprot.org/uniprotkb/Q3MIT2) (tRNA pseudouridine synthase Pus10):

> Protein with different functions depending on its subcellular location: involved in miRNA processing in the nucleus and acts as a tRNA pseudouridylate synthase in the cytoplasm. In the cytoplasm, acts as a pseudouridylate synthase by catalyzing synthesis of pseudouridine(54) and pseudouridine(55) from uracil-54 and uracil-55, respectively, in the psi GC loop of a subset of tRNAs. tRNA pseudouridylate synthase activity is enhanced by the presence of 1-methyladenosine at position 53-61 of tRNAs. …

**Summary**, from NCBI Gene [150962](https://www.ncbi.nlm.nih.gov/gene/150962):

> Pseudouridination, the isomerization of uridine to pseudouridine, is the most common posttranscriptional nucleotide modification found in RNA and is essential for biologic functions such as spliceosome biogenesis. Pseudouridylate synthases, such as PUS10, catalyze pseudouridination of structural RNAs, including transfer, ribosomal, and splicing RNAs. These enzymes also act as RNA chaperones, facilitating the correct folding and assembly of tRNAs (McCleverty et al., 2007 [PubMed …

**Accessions** — [HGNC:26505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26505) · Entrez [150962](https://www.ncbi.nlm.nih.gov/gene/150962) · UniProt [Q3MIT2](https://www.uniprot.org/uniprotkb/Q3MIT2) · Ensembl [ENSG00000162927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162927)

## Data

Gene col 8600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8600); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8600]; `tensor/DDL_lfc|DDL_z.npy` [8600]; `embed/gene_vectors.npy` [8600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8600 or target_col == 8600). Every well: [[PUS10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUS10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
