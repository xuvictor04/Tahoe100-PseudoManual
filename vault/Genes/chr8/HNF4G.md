---
symbol: "HNF4G"
type: "gene"
col: 9001
ensembl_id: "ENSG00000164749"
name: "hepatocyte nuclear factor 4 gamma"
location: "8q21.13"
module: 8
arm: "+"
pooled_cpm: 30.8
n_lines_expressing: 34
n_dd_up: 15
n_dd_down: 28
n_dd_up_clean: 14
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 37
direction_downstream: 42
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HNF4G

*hepatocyte nuclear factor 4 gamma* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.45× (z +4.9, q 6e-04, up in 22 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.213× (z -21.1, q 0e+00, down in 31 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLCH1]] (+0.72, fdr 7e-06), [[ACTR3C]] (+0.69, fdr 2e-05), [[MGAM2]] (+0.67, fdr 1e-05); moves opposite to [[GNAI2]] (-0.61, fdr 1e-04), [[EPOR]] (-0.60, fdr 3e-05), [[EFEMP2]] (-0.60, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[TMPRSS2]] → it (grade B ⚠); 42 go from it, the strongest it → [[TSPAN13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.9 | 6e-04 | 22/31 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 1e-03 | 20/31 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 0.003 | 11/32 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.019 | 13/31 (SW 900, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.023 | 12/31 (AsPC-1, A549, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.023 | 12/32 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.023 | 11/31 (AsPC-1, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.035 | 8/32 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.035 | 11/31 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.27×** | +3.4 | 0.035 | 13/32 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.4 | 0.041 | 11/32 (KATO III, SW 900, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.058 | 9/32 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.060 | 9/32 (LS 180, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.2 | 0.060 | 9/32 (COLO 205, A498, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.060 | 13/32 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.060 | 14/31 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.060 | 11/32 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9001.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.213×** | -21.1 | 0e+00 | 31/31 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.234×** | -19.8 | 0e+00 | 30/31 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.260×** | -18.3 | 0e+00 | 30/31 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.467×** | -14.6 | 0e+00 | 25/32 (A498, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.490×** | -9.7 | 3e-20 | 26/31 (SW480, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.491×** | -9.7 | 3e-20 | 25/31 (RKO, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.560×** | -7.9 | 2e-13 | 26/31 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.488×** | -7.7 | 1e-12 | 25/31 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.590×** | -7.2 | 5e-11 | 22/31 (SW480, KATO III, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.595×** | -7.1 | 9e-11 | 22/31 (SW480, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -6.8 | 6e-10 | 22/32 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.619×** | -6.5 | 4e-09 | 23/31 (SW48, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.460×** | -5.5 | 1e-06 | 19/32 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.678×** | -5.3 | 6e-06 | 20/31 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -4.9 | 4e-05 | 15/31 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.513×** | -4.7 | 7e-05 | 19/30 (RKO, A498, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.719×** | -4.5 | 3e-04 | 18/31 (RKO, A498, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.732×** | -4.1 | 0.002 | 12/32 (C32, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.598×** | -3.7 | 0.007 | 11/31 (LoVo, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.606×** | -3.6 | 0.010 | 12/30 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.843× | -3.3 | 0.025 | 11/32 (HT-29, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 82.6 | 0 | 15 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0933× (z -18.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.105× (z -18.4) |
| [[SW480 (line)]] | alt | 44.4 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0464× (z -27.5) |
| [[KATO III (line)]] | alt | 96.9 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0659× (z -25.0) |
| [[HEC-1-A (line)]] | alt | 46.8 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -20.8) |
| [[A498 (line)]] | wt | 66.3 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0986× (z -21.2) |
| [[COLO 205 (line)]] | alt | 83.6 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0426× (z -23.6) |
| [[LoVo (line)]] | wt | 112 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0777× (z -26.9) |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -17.7) |
| [[SW48 (line)]] | wt | 78.8 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0740× (z -16.9) |
| [[LS 180 (line)]] | wt | 95.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0733× (z -23.3) |
| [[CFPAC-1 (line)]] | alt | 40.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.129× (z -12.3) |
| [[HT-29 (line)]] | alt | 91.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0791× (z -19.9) |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.174× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 53.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -16.8) |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.103× (z -13.3) |
| [[A549 (line)]] | wt | 9.10 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0645× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0868× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 58.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -12.9) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.149× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 49.7 | 1 | 1 (1 ⚠) | [[Trametinib (drug)]] 0.5 µM 3.39× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 23.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.131× (z -8.8) |
| [[J82 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.179× (z -9.2) |
| [[BT-474 (line)]] | alt | 7.76 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0749× (z -9.1) |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0386× (z -9.7) ⚠ cell-cycle shift, explains ~94% of this change |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.172× (z -9.5) |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -8.9) |
| [[A-172 (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCH1]] | +0.72 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ACTR3C]] | +0.69 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[MGAM2]] | +0.67 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SYK]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TMCO4]] | +0.64 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[SAMD12-AS1]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TOX3]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PHACTR2]] | +0.62 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[SLC44A3-AS1]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[PROM1]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[A1CF]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 | STRING 622 |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | -0.61 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[EPOR]] | -0.60 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[EFEMP2]] | -0.60 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ARID3B]] | -0.58 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SFXN3]] | -0.58 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[TNNT1]] | -0.56 | -0.48 / -0.26 | both halves | 3e-04 |  |
| [[MPP2]] | -0.55 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[DNAAF9]] | -0.54 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[PC]] | -0.54 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[PCMT1]] | -0.54 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[EHD2]] | -0.54 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[TUBGCP2]] | -0.54 | -0.46 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 28, C 9. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS2]] | B | TMPRSS2 activity raises HNF4G's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.45× lower at baseline in the lines without TMPRSS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[CLIC5]] | B | CLIC5 activity raises HNF4G's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 4.21× lower at baseline in the lines without CLIC5 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[ZFP28]] | B | ZFP28 activity lowers HNF4G's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 3.95× higher at baseline in the lines without ZFP28 | 0.018 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[EPS8L3]] | B | EPS8L3 activity raises HNF4G's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 5.24× lower at baseline in the lines without EPS8L3 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[NPSR1-AS1]] | B | NPSR1-AS1 activity raises HNF4G's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without NPSR1-AS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[CCSER1]] | B | CCSER1 activity raises HNF4G's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.75× lower at baseline in the lines without CCSER1 | 0.021 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[RHEX]] | B | RHEX activity raises HNF4G's level | lines that do not express RHEX (43) vs lines expressing it (7) | 3.52× lower at baseline in the lines without RHEX | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[TRIM31]] | B | TRIM31 activity raises HNF4G's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.97× lower at baseline in the lines without TRIM31 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers HNF4G's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[GRHL2]] | B | GRHL2 activity raises HNF4G's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 3.51× lower at baseline in the lines without GRHL2 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[MMP7]] | B | MMP7 activity raises HNF4G's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.42× lower at baseline in the lines without MMP7 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[PRRG4]] | B | PRRG4 activity raises HNF4G's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 3.53× lower at baseline in the lines without PRRG4 | 0.049 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 32, C 10. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN13]] | B | HNF4G activity raises TSPAN13's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.60× lower at baseline in the lines without HNF4G | 0.004 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[FRK]] | B | HNF4G activity raises FRK's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without HNF4G | 0.005 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[SPATA6L]] | B | HNF4G activity raises SPATA6L's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without HNF4G | 0.012 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[ZNF471]] | B | HNF4G activity lowers ZNF471's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 4.22× higher at baseline in the lines without HNF4G | 0.021 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[HNF1B]] | B | HNF4G activity raises HNF1B's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.56× lower at baseline in the lines without HNF4G | 0.023 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[PTPRK]] | B | HNF4G activity raises PTPRK's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.67× lower at baseline in the lines without HNF4G | 0.027 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[ZFP28]] | B | HNF4G activity lowers ZFP28's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.83× higher at baseline in the lines without HNF4G | 0.030 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[EXPH5]] | B | HNF4G activity raises EXPH5's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.10× lower at baseline in the lines without HNF4G | 0.032 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[EPOR]] | B | HNF4G activity weakens EPOR's drug response | lines that do not express HNF4G (16) vs lines expressing it (32) | the lines without HNF4G respond 1.41× as strongly (z diff -1.01); strongest at Homoharringtonine 0.5 µM: 0.21x vs 0.44x (z diff -3.2) | 0.034 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5; target measured in part of the lines; artifact flags |
| [[MMAA]] | B | HNF4G activity raises MMAA's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without HNF4G | 0.034 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[SPINT1-AS1]] | B | HNF4G activity raises SPINT1-AS1's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without HNF4G | 0.037 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[PRSS23-AS1]] | B | HNF4G activity lowers PRSS23-AS1's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.12× higher at baseline in the lines without HNF4G | 0.041 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, 51.5); signed map (57.6, 0.3). **Vector** length 97.7, 28.3% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.3 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -18.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -21.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -19.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -5.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | hepatocyte nuclear factor 4 gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:75,407,914-75,566,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NR2A2 |
| Gene groups (HGNC) | Hepatocyte nuclear factor 4 family |
| Reactome | 3 pathways, smallest: Regulation of gene expression in beta cells; Regulation of beta-cell development; Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14541](https://www.uniprot.org/uniprotkb/Q14541) (Hepatocyte nuclear factor 4-gamma):

> Transcription factor. Has a lower transcription activation potential than HNF4-alpha.

**Summary**, from NCBI Gene [3174](https://www.ncbi.nlm.nih.gov/gene/3174):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in positive regulation of transcription by RNA polymerase II. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5026) · Entrez [3174](https://www.ncbi.nlm.nih.gov/gene/3174) · UniProt [Q14541](https://www.uniprot.org/uniprotkb/Q14541) · Ensembl [ENSG00000164749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164749)

## Data

Gene col 9001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9001); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9001]; `tensor/DDL_lfc|DDL_z.npy` [9001]; `embed/gene_vectors.npy` [9001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9001 or target_col == 9001). Every well: [[HNF4G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNF4G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
