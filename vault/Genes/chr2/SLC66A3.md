---
symbol: "SLC66A3"
type: "gene"
col: 8609
ensembl_id: "ENSG00000162976"
name: "solute carrier family 66 member 3"
location: "2p25.1"
module: 30
arm: "+"
pooled_cpm: 11.07
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 32
n_dd_up_clean: 9
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SLC66A3

*solute carrier family 66 member 3* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.14× (z +11.7, q 7e-29, up in 12 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.33× (z +4.5, q 0.001, up in 15 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.286× (z -28.3, q 0e+00, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL2]] (+0.69, fdr 7e-06), [[SEMA4F]] (+0.61, fdr 2e-05), [[ABRAXAS1]] (+0.60, fdr 1e-05); moves opposite to [[LINC01252]] (-0.51, fdr 6e-05), [[HGD]] (-0.51, fdr 1e-04), [[TNFSF14]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +11.7 | 7e-29 | 12/20 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.45×** | +8.4 | 1e-14 | 23/46 (A-427, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.3 | 1e-14 | 20/32 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 0.001 | 15/46 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.003 | 11/45 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +4.2 | 0.003 | 6/27 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.003 | 11/37 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.003 | 11/45 (A549, C-33 A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 13/46 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.6 | 0.015 | 5/46 (PANC-1, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.019 | 6/46 (KATO III, C-33 A, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.24×** | +3.5 | 0.021 | 7/45 (NCI-H2347, A498, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.053 | 6/45 (A498, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.065 | 13/46 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.065 | 7/46 (NCI-H2030, A-427, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.065 | 7/45 (LOX-IMVI, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.067 | 1/45 (LS 180) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +2.9 | 0.096 | 9/46 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.20× | +2.9 | 0.096 | 8/46 (A-427, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.20× | +2.9 | 0.096 | 1/45 (SNU-1) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.286×** | -28.3 | 0e+00 | 40/43 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.365×** | -16.1 | 0e+00 | 36/44 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.358×** | -15.7 | 0e+00 | 38/45 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -12.6 | 4e-34 | 39/46 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -10.2 | 2e-22 | 29/43 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.516×** | -10.1 | 4e-22 | 30/37 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -9.5 | 1e-19 | 29/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.556×** | -9.3 | 7e-19 | 30/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -8.7 | 2e-16 | 31/45 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.583×** | -8.6 | 4e-16 | 26/46 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.590×** | -8.4 | 2e-15 | 27/46 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.371×** | -8.3 | 7e-15 | 27/42 (SW1417, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -7.5 | 3e-12 | 27/46 (HOP62, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -7.2 | 3e-11 | 25/45 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -6.5 | 3e-09 | 20/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.667×** | -6.1 | 4e-08 | 21/46 (AsPC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -5.1 | 1e-05 | 14/46 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.678×** | -4.4 | 3e-04 | 8/46 (MIA PaCa-2, SHP-77, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -22.1) |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -17.6) |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.9) |
| [[PANC-1 (line)]] | alt | 16.9 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -16.7) |
| [[A-427 (line)]] | wt | 22.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.2) |
| [[A549 (line)]] | wt | 23.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -24.1) |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0856× (z -19.6) |
| [[AsPC-1 (line)]] | alt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.7) |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0977× (z -12.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.5) |
| [[J82 (line)]] | alt | 6.49 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -13.3) |
| [[KATO III (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.233× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0776× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 7.91 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.47× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.9) |
| [[A498 (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.8) |
| [[HCT15 (line)]] | alt | 8.57 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0530× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 7.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -8.7) |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.5) |
| [[LoVo (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -11.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 8.41 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -9.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 5.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -12.6) |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -12.3) |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL2]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SEMA4F]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ABRAXAS1]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[IL17RD]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[STX2]] | +0.60 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[IAH1]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PLD2]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CAPG]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TMOD2]] | +0.56 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[STX7]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[DUSP18]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[STARD9]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01252]] | -0.51 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[HGD]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[TNFSF14]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[LINC01340]] | -0.50 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PLXDC2]] | -0.48 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[DKK2]] | -0.47 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[KIF26B]] | -0.47 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[FBXW10B]] | -0.47 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[NRG1]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PCDH7]] | -0.45 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-2.8, -3.4); signed map (-32.5, -5.1). **Vector** length 71.3, 13.0% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.6 | +8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -28.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -16.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.1 | +2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 66 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:11,155,198-11,178,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33602; previously C2orf22, PQLC3 |
| Gene groups (HGNC) | Solute carrier family 66 |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

UniProt [Q8N755](https://www.uniprot.org/uniprotkb/Q8N755) carries no function annotation.

**Summary**, from NCBI Gene [130814](https://www.ncbi.nlm.nih.gov/gene/130814):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28503) · Entrez [130814](https://www.ncbi.nlm.nih.gov/gene/130814) · UniProt [Q8N755](https://www.uniprot.org/uniprotkb/Q8N755) · Ensembl [ENSG00000162976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162976)

## Data

Gene col 8609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8609); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8609]; `tensor/DDL_lfc|DDL_z.npy` [8609]; `embed/gene_vectors.npy` [8609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8609 or target_col == 8609). Every well: [[SLC66A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC66A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
