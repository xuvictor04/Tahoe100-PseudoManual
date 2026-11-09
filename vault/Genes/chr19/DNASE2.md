---
symbol: "DNASE2"
type: "gene"
col: 2626
ensembl_id: "ENSG00000105612"
name: "deoxyribonuclease 2, lysosomal"
location: "19p13.13"
module: 45
arm: "+"
pooled_cpm: 19.66
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# DNASE2

*deoxyribonuclease 2, lysosomal* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.01× (z +8.3, q 4e-14, up in 30 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.53× (z +7.2, q 1e-10, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.264× (z -22.4, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASAH1]] (+0.69, fdr 7e-06), [[GLMP]] (+0.66, fdr 7e-06), [[ERP29]] (+0.66, fdr 7e-06); moves opposite to [[MPHOSPH6]] (-0.62, fdr 1e-05), [[AGO2]] (-0.59, fdr 9e-06), [[TNFRSF12A]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CPVL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +8.3 | 4e-14 | 30/39 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.5 | 2e-11 | 21/31 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +7.2 | 1e-10 | 36/48 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +6.3 | 4e-08 | 27/45 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.5 | 7e-04 | 25/48 (A-172, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.015 | 18/47 (LS 180, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.017 | 15/47 (A-427, C-33 A, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.031 | 12/47 (A498, SNU-423, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.049 | 17/48 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.3 | 0.053 | 18/43 (LS 180, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +3.2 | 0.069 | 16/47 (SW1417, A-427, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.077 | 15/46 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.091 | 19/47 (SW480, NCI-H23, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.31× | +3.0 | 0.10 | 19/37 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.264×** | -22.4 | 0e+00 | 45/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.218×** | -18.1 | 0e+00 | 45/47 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.348×** | -12.1 | 3e-31 | 40/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.456×** | -9.3 | 2e-18 | 39/48 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -7.8 | 6e-13 | 41/48 (COLO 205, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.525×** | -7.7 | 2e-12 | 37/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.572×** | -6.6 | 3e-09 | 31/48 (HT-29, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -6.3 | 2e-08 | 34/47 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -5.9 | 3e-07 | 28/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.613×** | -5.6 | 1e-06 | 32/47 (NCI-H2030, J82, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.645×** | -5.2 | 1e-05 | 27/47 (C32, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.655×** | -4.6 | 2e-04 | 27/46 (SW48, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -4.4 | 4e-04 | 23/47 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.524×** | -4.0 | 0.002 | 20/45 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.754×** | -3.3 | 0.032 | 17/48 (HCT15, KATO III, …) | all doses, flat | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.768×** | -3.1 | 0.059 | 15/47 (RKO, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.059 | 19/47 (NCI-H23, SW480, …) | top dose only |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.770×** | -3.1 | 0.059 | 14/47 (BT-474, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -22.6) |
| [[H4 (line)]] | wt | 37.0 | 0 | 5 | — | [[Harringtonine (drug)]] 0.5 µM 0.0603× (z -15.7) |
| [[RKO (line)]] | wt | 22.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.6) |
| [[SW48 (line)]] | wt | 26.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0318× (z -16.5) |
| [[A-172 (line)]] | wt | 33.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -13.4) |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.8) |
| [[HS-578T (line)]] | alt | 37.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0965× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -24.0) |
| [[A498 (line)]] | wt | 30.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -14.1) |
| [[A549 (line)]] | wt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -14.8) |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -17.6) |
| [[HCT15 (line)]] | alt | 24.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 18.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 8.83 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -11.3) |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.9) |
| [[J82 (line)]] | alt | 18.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.7) |
| [[KATO III (line)]] | alt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 7.77 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.132× (z -9.0) |
| [[LS 180 (line)]] | wt | 21.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -12.2) |
| [[SNU-423 (line)]] | alt | 37.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.9) |
| [[SW480 (line)]] | alt | 17.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -15.1) |
| [[A-427 (line)]] | wt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.0) |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 1 | — | [[Zileuton (drug)]] 0.5 µM 0.0544× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -11.1) |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.3) |
| [[LoVo (line)]] | wt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.9) |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0700× (z -10.1) |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASAH1]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GLMP]] | +0.66 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ERP29]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[GRN]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CTSD]] | +0.65 | +0.74 / +0.58 | both halves | 7e-06 | STRING 414 |
| [[SCPEP1]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MYL6B]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MARCHF8]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.63 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[NFE2L1]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[C20orf96]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | -0.62 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[AGO2]] | -0.59 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[TNFRSF12A]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SVIL]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[EEFSEC]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[PTPRN2]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.56 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[MAMLD1]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZBTB38]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PPIL1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.53 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[CCDC57]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPVL]] | B | CPVL activity lowers DNASE2's level | lines that do not express CPVL (21) vs lines expressing it (29) | 1.32× higher at baseline in the lines without CPVL | 0.036 | ⚠ within organs, on part of the lines; also absent: CHN2, PTPRR, BBOX1-AS1 |
| [[CTSD]] | C | CTSD activity raises DNASE2's level | lines that do not express CTSD (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without CTSD | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-17.1, -19.0); signed map (-24.5, -3.3). **Vector** length 90.1, 22.2% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.9 | +7.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +5.3 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.8 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -18.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -12.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | deoxyribonuclease 2, lysosomal |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,875,209-12,881,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DNL, DNL2 |
| Reactome | 4 pathways, smallest: Lysosome Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O00115](https://www.uniprot.org/uniprotkb/O00115) (Deoxyribonuclease-2-alpha):

> Hydrolyzes DNA under acidic conditions with a preference for double-stranded DNA. Plays a major role in the clearance of nucleic acids generated through apoptosis, hence preventing autoinflammation. Necessary for proper fetal development and for definitive erythropoiesis in fetal liver and bone marrow, where it degrades nuclear DNA expelled from erythroid precursor cells.

**Summary**, from NCBI Gene [1777](https://www.ncbi.nlm.nih.gov/gene/1777):

> This gene encodes a member of the DNase family. The protein, located in the lysosome, hydrolyzes DNA under acidic conditions and mediates the breakdown of DNA during erythropoiesis and apoptosis. Two codominant alleles have been characterized, DNASE2*L (low activity) and DNASE2*H (high activity), that differ at one nucleotide in the promoter region. The DNASE2*H allele is represented in this record. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2960) · Entrez [1777](https://www.ncbi.nlm.nih.gov/gene/1777) · UniProt [O00115](https://www.uniprot.org/uniprotkb/O00115) · Ensembl [ENSG00000105612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105612)

## Data

Gene col 2626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2626); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2626]; `tensor/DDL_lfc|DDL_z.npy` [2626]; `embed/gene_vectors.npy` [2626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2626 or target_col == 2626). Every well: [[DNASE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNASE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
