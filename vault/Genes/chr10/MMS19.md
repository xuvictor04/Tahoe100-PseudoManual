---
symbol: "MMS19"
type: "gene"
col: 7877
ensembl_id: "ENSG00000155229"
name: "MMS19 cytosolic iron-sulfur assembly component"
location: "10q24.1"
module: 30
arm: "+"
pooled_cpm: 51.22
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MMS19

*MMS19 cytosolic iron-sulfur assembly component* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 2.39× (z +7.9, q 2e-12, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.461× (z -18.8, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LCMT1]] (+0.78, fdr 7e-06), [[SNAPC3]] (+0.77, fdr 7e-06), [[MALSU1]] (+0.76, fdr 7e-06); moves opposite to [[SKIL]] (-0.74, fdr 7e-06), [[ZNF655]] (-0.72, fdr 7e-06), [[FKRP]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[P3H3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +7.9 | 2e-12 | 38/48 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +6.3 | 7e-08 | 34/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.003 | 26/48 (C-33 A, J82, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.5 | 0.067 | 14/48 (C32, PANC-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.067 | 11/48 (HepG2/C3A, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.461×** | -18.8 | 0e+00 | 45/48 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.426×** | -14.7 | 0e+00 | 45/47 (NCI-H23, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.412×** | -14.1 | 6e-43 | 38/44 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -11.2 | 7e-27 | 32/41 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -11.0 | 2e-26 | 40/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.605×** | -8.7 | 5e-16 | 32/48 (C32, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -8.5 | 1e-15 | 38/48 (C32, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -6.7 | 1e-09 | 32/48 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.761×** | -6.6 | 2e-09 | 33/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -6.6 | 3e-09 | 28/47 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -4.8 | 9e-05 | 24/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -4.7 | 1e-04 | 27/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -4.5 | 2e-04 | 25/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.783×** | -4.2 | 0.001 | 25/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.776×** | -4.2 | 0.001 | 23/47 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -4.1 | 0.002 | 24/48 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.789×** | -4.1 | 0.002 | 22/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.857× | -3.7 | 0.005 | 16/48 (HS-578T, Hs 766T, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.009 | 18/48 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.822×** | -3.4 | 0.020 | 14/48 (A549, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 69.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -17.5) |
| [[PANC-1 (line)]] | alt | 57.4 | 2 (1 ⚠) | 6 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.42× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.79× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 58.4 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.5) |
| [[HOP62 (line)]] | alt | 82.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -25.4) |
| [[C32 (line)]] | wt | 78.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -21.0) |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -12.7) |
| [[HS-578T (line)]] | alt | 51.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -24.3) |
| [[LOX-IMVI (line)]] | wt | 48.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.3) |
| [[NCI-H1573 (line)]] | alt | 47.6 | 1 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.84× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.9) |
| [[HCT15 (line)]] | alt | 66.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 57.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 49.8 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -12.3) |
| [[SW 900 (line)]] | alt | 61.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -9.2) |
| [[A498 (line)]] | wt | 45.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -11.7) |
| [[A549 (line)]] | wt | 64.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 38.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.2) |
| [[H4 (line)]] | wt | 65.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -11.8) |
| [[Hs 766T (line)]] | wt | 65.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 65.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 47.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 58.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -24.7) |
| [[A-427 (line)]] | wt | 47.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -17.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 32.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 71.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.345× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 44.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -13.1) |
| [[SHP-77 (line)]] | alt | 54.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 61.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -17.0) |
| [[SW48 (line)]] | wt | 53.9 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 47.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 52.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.4) |
| [[CHP-212 (line)]] | wt | 58.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.132× (z -9.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[J82 (line)]] | alt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -14.3) |
| [[LoVo (line)]] | wt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 37.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.3) |
| [[SNU-1 (line)]] | wt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0887× (z -17.1) |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -10.1) |
| [[AN3 CA (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | +0.78 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.77 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.76 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.76 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[HDHD5]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ELP2]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ALG9]] | +0.72 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.72 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.72 | +0.71 / +0.57 | both halves | 8e-06 |  |
| [[GMCL1]] | +0.71 | +0.73 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIL]] | -0.74 | -0.76 / -0.62 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.72 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[FKRP]] | -0.70 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | -0.70 | -0.74 / -0.51 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | -0.68 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[ARAP2]] | -0.68 | -0.71 / -0.50 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | -0.67 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.66 | -0.71 / -0.38 | both halves | 6e-05 |  |
| [[CHMP3]] | -0.66 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.66 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[C11orf58]] | -0.66 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[ST7L]] | -0.65 | -0.72 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H3]] | B | P3H3 activity raises MMS19's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without P3H3 | 0.013 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[GPR155]] | B | GPR155 activity raises MMS19's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without GPR155 | 0.064 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[DSC2]] | B | DSC2 activity lowers MMS19's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 1.26× higher at baseline in the lines without DSC2 | 0.067 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[RDH10]] | B | RDH10 activity lowers MMS19's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.30× higher at baseline in the lines without RDH10 | 0.074 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.0, -13.5); signed map (-37.6, 0.5). **Vector** length 127, 39.1% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.9 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | -0.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.8 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.9 | -18.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -8.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | MMS19 cytosolic iron-sulfur assembly component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:97,458,324-97,498,794 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MET18, hMMS19, CIAO4; previously MMS19L |
| Gene groups (HGNC) | Cytosolic iron-sulfur assembly components; Nucleotide excision repair; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: Cytosolic iron-sulfur cluster assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T76](https://www.uniprot.org/uniprotkb/Q96T76) (MMS19 nucleotide excision repair protein homolog):

> Key component of the cytosolic iron-sulfur protein assembly (CIA) complex, a multiprotein complex that mediates the incorporation of iron-sulfur cluster into apoproteins specifically involved in DNA metabolism and genomic integrity. In the CIA complex, MMS19 acts as an adapter between early-acting CIA components and a subset of cellular target iron-sulfur proteins such as ERCC2/XPD, FANCJ and RTEL1, thereby playing a key role in nucleotide excision repair (NER), homologous …

**Summary**, from NCBI Gene [64210](https://www.ncbi.nlm.nih.gov/gene/64210):

> Enables nuclear estrogen receptor binding activity and transcription coactivator activity. Involved in protein maturation. Located in cytoplasm; nucleoplasm; and spindle. Part of MMXD complex and cytosolic [4Fe-4S] assembly targeting complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13824) · Entrez [64210](https://www.ncbi.nlm.nih.gov/gene/64210) · UniProt [Q96T76](https://www.uniprot.org/uniprotkb/Q96T76) · Ensembl [ENSG00000155229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155229)

## Data

Gene col 7877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7877); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7877]; `tensor/DDL_lfc|DDL_z.npy` [7877]; `embed/gene_vectors.npy` [7877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7877 or target_col == 7877). Every well: [[MMS19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMS19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
