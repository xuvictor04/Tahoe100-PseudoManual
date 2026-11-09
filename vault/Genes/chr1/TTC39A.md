---
symbol: "TTC39A"
type: "gene"
col: 1441
ensembl_id: "ENSG00000085831"
name: "tetratricopeptide repeat domain 39A"
location: "1p32.3"
module: 8
arm: "+"
pooled_cpm: 6.33
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TTC39A

*tetratricopeptide repeat domain 39A* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.69× (z +7.0, q 2e-09, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +6.5, q 2e-08, up in 16 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.539× (z -8.5, q 1e-14, down in 25 of 44 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.687× (z -5.2, q 1e-05, down in 18 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (HT-29 0.162×, CFPAC-1 0.187×, HEC-1-A 0.317×, COLO 205 0.183×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.129×, MIA PaCa-2 0.135×; ⚠ cell-cycle shift, explains ~31% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.192×, COLO 205 0.105×; ⚠ cell-cycle shift, explains ~36% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.274×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (PANC-1 0.0483×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0550×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCP]] (+0.69, fdr 7e-06), [[FAM149A]] (+0.63, fdr 4e-05), [[AXDND1]] (+0.60, fdr 1e-05); moves opposite to [[UBR7]] (-0.53, fdr 4e-05), [[IFT122]] (-0.50, fdr 1e-04), [[CNOT10]] (-0.49, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01564]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.0 | 2e-09 | 3/10 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.5 | 2e-08 | 16/37 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +6.1 | 2e-07 | 16/43 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +5.8 | 1e-06 | 3/15 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.4 | 6e-06 | 6/20 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +4.8 | 1e-04 | 12/45 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +4.7 | 2e-04 | 11/46 (HS-578T, A-427, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.001 | 11/43 (A549, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.002 | 12/43 (SW480, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.008 | 11/44 (PANC-1, Panc 03.27, …) | all doses, flat |  |
| [[Ivabradine (hydrochloride) (drug)]] 0.5 µM | ⚠ transcription drop; unreliable plate only | **1.30×** | +3.6 | 0.013 | 4/41 (C32, SW 900, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.013 | 8/44 (A549, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.29×** | +3.3 | 0.036 | 9/42 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.3 | 0.037 | 5/45 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.043 | 7/44 (MIA PaCa-2, BT-474, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.075 | 9/44 (SW480, HCT15, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 14 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1441.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (HT-29 0.162×, CFPAC-1 0.187×, HEC-1-A 0.317×, COLO 205 0.183×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.129×, MIA PaCa-2 0.135×; ⚠ cell-cycle shift, explains ~31% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.192×, COLO 205 0.105×; ⚠ cell-cycle shift, explains ~36% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.274×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (PANC-1 0.0483×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0550×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.539×** | -8.5 | 1e-14 | 25/44 (BT-474, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.584×** | -7.4 | 4e-11 | 22/46 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.591×** | -7.2 | 9e-11 | 23/45 (NCI-H2030, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.598×** | -7.1 | 2e-10 | 20/45 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.600×** | -7.0 | 3e-10 | 19/46 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.606×** | -6.9 | 6e-10 | 23/46 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.619×** | -6.6 | 3e-09 | 20/44 (J82, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.631×** | -6.3 | 2e-08 | 18/33 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.724×** | -6.3 | 2e-08 | 19/39 (HT-29, CFPAC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.687×** | -5.2 | 1e-05 | 18/40 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.492×** | -5.1 | 2e-05 | 12/42 (MIA PaCa-2, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.697×** | -4.8 | 9e-05 | 16/44 (MIA PaCa-2, HT-29, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.556×** | -4.2 | 0.001 | 12/37 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.756×** | -3.8 | 0.005 | 9/46 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.760×** | -3.8 | 0.006 | 12/45 (MIA PaCa-2, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 26.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -17.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0896× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.159× (z -9.2) |
| [[LoVo (line)]] | wt | 13.3 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -14.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 4.45 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0741× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 5.00 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0550× (z -10.1) |
| [[LS 180 (line)]] | wt | 7.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -8.8) ⚠ cell-cycle shift, explains ~85% of this change |
| [[NCI-H2030 (line)]] | alt | 4.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0730× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 6.25 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0654× (z -10.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 3.10 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0483× (z -12.0) |
| [[SW1417 (line)]] | alt | 5.06 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCP]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[FAM149A]] | +0.63 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[AXDND1]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MROH3P]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[KLHL2P1]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[BTBD16]] | +0.58 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CDHR2]] | +0.57 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[ADAP2]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[OIT3]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CYP4F3]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[MMP24]] | +0.56 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[LINC02580]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBR7]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[IFT122]] | -0.50 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[CNOT10]] | -0.49 | -0.39 / -0.47 | both halves | 5e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01564]] | B | LINC01564 activity raises TTC39A's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 1.64× lower at baseline in the lines without LINC01564 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[FAM83B]] | B | FAM83B activity raises TTC39A's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without FAM83B | 0.041 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[HKDC1]] | B | HKDC1 activity strengthens TTC39A's drug response | lines that do not express HKDC1 (28) vs lines expressing it (18) | the lines without HKDC1 respond 0.59× as strongly (z diff +1.10); strongest at Panobinostat 5 µM: 0.87x vs 0.41x (z diff +3.8) | 0.047 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; target measured in part of the lines; artifact flags |
| [[BTBD16]] | B | BTBD16 activity lowers TTC39A's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.08× higher at baseline in the lines without BTBD16 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HKDC1]] | B | HKDC1 activity raises TTC39A's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 1.51× lower at baseline in the lines without HKDC1 | 0.088 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.7, 41.3); signed map (54.1, 4.6). **Vector** length 66.5, 9.85% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.0 | -7.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.7 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.2 | -7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.1 | -7.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 39A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:51,287,258-51,345,116 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0452, DEME-6; previously C1orf34 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

UniProt [Q5SRH9](https://www.uniprot.org/uniprotkb/Q5SRH9) carries no function annotation.

**Summary**, from NCBI Gene [22996](https://www.ncbi.nlm.nih.gov/gene/22996):

> Located in centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18657) · Entrez [22996](https://www.ncbi.nlm.nih.gov/gene/22996) · UniProt [Q5SRH9](https://www.uniprot.org/uniprotkb/Q5SRH9) · Ensembl [ENSG00000085831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085831)

## Data

Gene col 1441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1441); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1441]; `tensor/DDL_lfc|DDL_z.npy` [1441]; `embed/gene_vectors.npy` [1441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1441 or target_col == 1441). Every well: [[TTC39A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC39A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
