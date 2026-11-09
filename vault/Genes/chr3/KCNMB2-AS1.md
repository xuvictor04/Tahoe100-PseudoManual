---
symbol: "KCNMB2-AS1"
type: "gene"
col: 14161
ensembl_id: "ENSG00000237978"
name: "KCNMB2 antisense RNA 1"
location: "3q26.32"
module: 10
arm: "+"
pooled_cpm: 36.67
n_lines_expressing: 36
n_dd_up: 30
n_dd_down: 19
n_dd_up_clean: 27
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KCNMB2-AS1

*KCNMB2 antisense RNA 1* — 3q26.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.83× (z +14.8, q 0e+00, up in 25 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.468× (z -7.6, q 1e-11, down in 21 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.519× (z -6.6, q 6e-09, down in 23 of 33 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPAS3]] (+0.71, fdr 1e-05), [[FBXO38-DT]] (+0.69, fdr 2e-05), [[TAFA2]] (+0.69, fdr 2e-05); moves opposite to [[SH3PXD2B]] (-0.60, fdr 8e-05), [[TPST2]] (-0.58, fdr 1e-04), [[GPR180]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC00491]] → it (grade B ⚠); 3 go from it, the strongest it → [[FBXO38-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +14.8 | 0e+00 | 25/34 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.63×** | +13.7 | 2e-40 | 25/34 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +8.1 | 7e-14 | 24/33 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.1 | 1e-13 | 21/34 (A-172, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.98×** | +6.6 | 4e-09 | 23/33 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +6.1 | 7e-08 | 12/30 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +5.0 | 4e-05 | 24/33 (KATO III, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +4.8 | 1e-04 | 19/33 (RKO, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 2e-04 | 21/34 (SW480, C32, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 3e-04 | 21/33 (C32, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.5 | 4e-04 | 16/32 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.36×** | +4.4 | 6e-04 | 19/34 (SNU-1, J82, …) | top dose only | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.001 | 18/34 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.006 | 16/34 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +3.8 | 0.006 | 18/34 (LoVo, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.007 | 17/34 (LoVo, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.007 | 16/33 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.010 | 18/33 (C32, SW48, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.468×** | -7.6 | 1e-11 | 21/32 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.497×** | -7.0 | 4e-10 | 24/33 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.498×** | -7.0 | 4e-10 | 24/33 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.519×** | -6.6 | 6e-09 | 23/33 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.549×** | -6.0 | 2e-07 | 23/33 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.572×** | -5.6 | 2e-06 | 20/33 (HT-29, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.602×** | -4.9 | 7e-05 | 20/32 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.601×** | -4.8 | 9e-05 | 22/33 (HT-29, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.627×** | -4.5 | 4e-04 | 20/34 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.429×** | -4.5 | 5e-04 | 18/29 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.652×** | -4.3 | 9e-04 | 20/33 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.662×** | -4.0 | 0.003 | 22/31 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.599×** | -3.7 | 0.010 | 18/34 (HEC-1-A, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.697×** | -3.6 | 0.011 | 16/33 (SW1417, AN3 CA, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.710×** | -3.4 | 0.022 | 16/33 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.539×** | -3.2 | 0.041 | 12/33 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.543×** | -3.2 | 0.045 | 15/33 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.660×** | -3.0 | 0.086 | 13/34 (HEC-1-A, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 82.1 | 0 | 14 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0707× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.246× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 257 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -14.8) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.353× (z -9.7) |
| [[HT-29 (line)]] | alt | 44.5 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -11.6) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.190× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 58.7 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.233× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.2) |
| [[RKO (line)]] | wt | 16.3 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +13.7) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.110× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 73.9 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 10.4 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +14.8) | [[Pimozide (drug)]] 0.05 µM 0.0711× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 8.90× (z +9.6) | [[Pimozide (drug)]] 0.05 µM 0.0652× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 54.5 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 35.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +19.4) | [[Digitoxin (drug)]] 5 µM 0.126× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 40.4 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.194× (z -10.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 9.97 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +16.0) | — |
| [[H4 (line)]] | wt | 18.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +13.3) | — |
| [[LoVo (line)]] | wt | 17.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.54× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 78.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 28.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +10.0) | — |
| [[C32 (line)]] | wt | 45.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 64.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 11.7× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0865× (z -9.3) ⚠ toxic |
| [[KATO III (line)]] | alt | 28.7 | 1 | 1 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 4.39× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.209× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 46.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 33.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0737× (z -8.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 34.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.226× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 49.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.341× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 70.3 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.29× (z +8.8) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[SW 900 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +10.9) | — |
| [[A549 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPAS3]] | +0.71 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[FBXO38-DT]] | +0.69 | +0.76 / +0.46 | both halves | 2e-05 |  |
| [[TAFA2]] | +0.69 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[AK9]] | +0.68 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[TMEM232]] | +0.68 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.68 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[STPG2]] | +0.66 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[LINC02398]] | +0.66 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[FAM227B]] | +0.66 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.64 | +0.69 / +0.36 | both halves | 9e-05 |  |
| [[TSGA10]] | +0.64 | +0.72 / +0.32 | both halves | 1e-04 |  |
| [[IQCH-AS1]] | +0.64 | +0.70 / +0.34 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.60 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[TPST2]] | -0.58 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[GPR180]] | -0.56 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.56 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[FAM118A]] | -0.56 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[YIF1B]] | -0.56 | -0.58 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[GNA12]] | -0.55 | -0.61 / -0.29 | both halves | 2e-04 |  |
| [[PHKA2]] | -0.55 | -0.60 / -0.21 | both halves | 6e-04 |  |
| [[GTF2E2]] | -0.55 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[CCDC134]] | -0.54 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[CDR2L]] | -0.54 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[LPCAT1]] | -0.54 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[GTPBP3]] | -0.54 | -0.46 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00491]] | B | LINC00491 activity raises KCNMB2-AS1's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 2.20× lower at baseline in the lines without LINC00491 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7 |
| [[TOP2A]] | B | TOP2A activity lowers KCNMB2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCC]] | B | MCC activity raises KCNMB2-AS1's level | lines that do not express MCC (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without MCC | 0.045 | ⚠ within organs, on part of the lines; also absent: CAMK4, EGFEM1P, DYNC1I1 |
| [[LINC02147]] | B | LINC02147 activity raises KCNMB2-AS1's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without LINC02147 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |
| [[MIR2052HG]] | B | MIR2052HG activity raises KCNMB2-AS1's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without MIR2052HG | 0.072 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[NIHCOLE]] | B | NIHCOLE activity strengthens KCNMB2-AS1's drug response | lines that do not express NIHCOLE (13) vs lines expressing it (21) | the lines without NIHCOLE respond 1.05× as strongly (z diff -0.28); strongest at Digitoxin 5 µM: 0.88x vs 0.32x (z diff +5.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1; target measured in part of the lines; both ways; artifact flags |
| [[PINCR]] | B | PINCR activity raises KCNMB2-AS1's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.99× lower at baseline in the lines without PINCR | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[ENPEP]] | B | ENPEP activity raises KCNMB2-AS1's level | lines that do not express ENPEP (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without ENPEP | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02253, KCNE3, ENSG00000265554; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO38-DT]] | B | KCNMB2-AS1 activity raises FBXO38-DT's level | lines that do not express KCNMB2-AS1 (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without KCNMB2-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: FIRRE, STXBP6, LINC01980; maybe low, not absent |
| [[MCC]] | B | KCNMB2-AS1 activity raises MCC's level | lines that do not express KCNMB2-AS1 (14) vs lines expressing it (36) | 2.29× lower at baseline in the lines without KCNMB2-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: FIRRE, STXBP6, LINC01980; maybe low, not absent |
| [[PTCHD4]] | B | KCNMB2-AS1 activity raises PTCHD4's level | lines that do not express KCNMB2-AS1 (14) vs lines expressing it (36) | 3.48× lower at baseline in the lines without KCNMB2-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: FIRRE, STXBP6, LINC01980; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.5, 15.6); signed map (28.6, -10.4). **Vector** length 112, 32.2% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.9 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.3 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.7 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -3.8 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | KCNMB2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q26.32 — chr3:178,526,505-178,937,352 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-385J1.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51409](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51409) · Entrez [104797538](https://www.ncbi.nlm.nih.gov/gene/104797538) · Ensembl [ENSG00000237978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237978)

## Data

Gene col 14161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14161); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14161]; `tensor/DDL_lfc|DDL_z.npy` [14161]; `embed/gene_vectors.npy` [14161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14161 or target_col == 14161). Every well: [[KCNMB2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNMB2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
