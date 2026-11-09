---
symbol: "PRKD2"
type: "gene"
col: 2576
ensembl_id: "ENSG00000105287"
name: "protein kinase D2"
location: "19q13.32"
module: 48
arm: "+"
pooled_cpm: 45.19
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# PRKD2

*protein kinase D2* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.61× (z +10.1, q 3e-21, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.383× (z -19.5, q 0e+00, down in 37 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.623× (z -10.0, q 3e-21, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MVB12A]] (+0.61, fdr 1e-05), [[NECTIN2]] (+0.61, fdr 1e-05), [[MARK4]] (+0.61, fdr 1e-05); moves opposite to [[MCCC2]] (-0.61, fdr 1e-05), [[OXCT1]] (-0.61, fdr 1e-05), [[IMPACT]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TMEM92]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +10.1 | 3e-21 | 38/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +9.8 | 2e-20 | 34/48 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +9.3 | 4e-18 | 39/47 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +7.3 | 4e-11 | 30/48 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +6.6 | 4e-09 | 28/48 (J82, KATO III, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.8 | 6e-07 | 23/47 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.2 | 1e-05 | 23/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 1e-04 | 21/46 (SW480, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.7 | 1e-04 | 24/49 (A498, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.7 | 2e-04 | 21/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +4.1 | 0.002 | 16/47 (A498, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.010 | 11/48 (SW480, hTERT-HPNE, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.013 | 9/48 (A-172, NCI-H460, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.014 | 13/48 (SW1417, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.022 | 9/46 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.042 | 7/47 (HS-578T, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.053 | 5/48 (AN3 CA, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2576.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.383×** | -19.5 | 0e+00 | 37/39 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.492×** | -15.0 | 0e+00 | 35/47 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.552×** | -11.6 | 1e-28 | 33/43 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -10.0 | 3e-21 | 31/48 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.801×** | -6.6 | 5e-09 | 27/48 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -5.3 | 9e-06 | 20/48 (SNU-423, A549, …) | rises with dose | low cells (technical?) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.836× | -5.3 | 9e-06 | 23/48 (LoVo, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.801×** | -4.7 | 2e-04 | 25/48 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.810×** | -4.3 | 0.001 | 21/46 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.811×** | -4.2 | 0.001 | 21/48 (NCI-H23, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -4.2 | 0.002 | 17/48 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.833×** | -3.8 | 0.006 | 17/48 (A549, SNU-423, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.842× | -3.6 | 0.014 | 15/48 (NCI-H23, HT-29, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.843× | -3.6 | 0.014 | 12/48 (AsPC-1, BT-474, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.844× | -3.5 | 0.015 | 15/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.854× | -3.3 | 0.033 | 12/48 (NCI-H661, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 101 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 61.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 78.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.3) |
| [[HS-578T (line)]] | alt | 50.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -18.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 53.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 37.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 40.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 75.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.3) |
| [[A-427 (line)]] | wt | 46.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -14.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 50.2 | 0 | 2 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0786× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 50.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -13.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -11.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 60.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 70.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -14.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 26.5 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.11× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 55.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.585× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 37.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 42.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.23× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -15.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -9.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 60.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -11.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -18.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -19.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MVB12A]] | +0.61 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[NECTIN2]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[MARK4]] | +0.61 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[C4orf48]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[HELZ2]] | +0.59 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[STAT2]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[OGFR]] | +0.58 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CHMP5]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.57 | +0.39 / +0.59 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC66A2]] | +0.57 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[FAM89B]] | +0.57 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PLIN3]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CARHSP1]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCCC2]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[OXCT1]] | -0.61 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[IMPACT]] | -0.60 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[SNX5]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[UCHL5]] | -0.59 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ADSS2]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[GUF1]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[IPO5]] | -0.56 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[FH]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.54 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MBTPS2]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ZMPSTE24]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92]] | B | TMEM92 activity raises PRKD2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.26× lower at baseline in the lines without TMEM92 | 0.043 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[OXCT1]] | B | OXCT1 activity lowers PRKD2's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 1.32× higher at baseline in the lines without OXCT1 | 0.050 | ⚠ within organs, on part of the lines |
| [[SP110]] | B | SP110 activity raises PRKD2's level | lines that do not express SP110 (5) vs lines expressing it (45) | 1.34× lower at baseline in the lines without SP110 | 0.050 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[HSH2D]] | B | HSH2D activity raises PRKD2's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.29× lower at baseline in the lines without HSH2D | 0.054 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[TYMP]] | B | TYMP activity raises PRKD2's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.06× lower at baseline in the lines without TYMP | 0.094 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (7.2, 0.2); signed map (-25.5, 29.3). **Vector** length 132, 37.3% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.6 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +9.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.7 | +3.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -19.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.2 | -5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -4.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.0 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,674,275-46,717,127 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKD2, HSPC187, DKFZP586E0820 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes; Protein kinase D family |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZL6](https://www.uniprot.org/uniprotkb/Q9BZL6) (Serine/threonine-protein kinase D2):

> Serine/threonine-protein kinase that converts transient diacylglycerol (DAG) signals into prolonged physiological effects downstream of PKC, and is involved in the regulation of cell proliferation via MAPK1/3 (ERK1/2) signaling, oxidative stress-induced NF-kappa-B activation, inhibition of HDAC7 transcriptional repression, signaling downstream of T-cell antigen receptor (TCR) and cytokine production, and plays a role in Golgi membrane trafficking, angiogenesis, secretory granule release and …

**Summary**, from NCBI Gene [25865](https://www.ncbi.nlm.nih.gov/gene/25865):

> The protein encoded by this gene belongs to the protein kinase D (PKD) family of serine/threonine protein kinases. This kinase can be activated by phorbol esters as well as by gastrin via the cholecystokinin B receptor (CCKBR) in gastric cancer cells. It can bind to diacylglycerol (DAG) in the trans-Golgi network (TGN) and may regulate basolateral membrane protein exit from TGN. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul …

**Accessions** — [HGNC:17293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17293) · Entrez [25865](https://www.ncbi.nlm.nih.gov/gene/25865) · UniProt [Q9BZL6](https://www.uniprot.org/uniprotkb/Q9BZL6) · Ensembl [ENSG00000105287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105287)

## Data

Gene col 2576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2576); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2576]; `tensor/DDL_lfc|DDL_z.npy` [2576]; `embed/gene_vectors.npy` [2576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2576 or target_col == 2576). Every well: [[PRKD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
