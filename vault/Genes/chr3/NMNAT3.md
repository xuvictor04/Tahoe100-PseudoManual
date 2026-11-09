---
symbol: "NMNAT3"
type: "gene"
col: 8793
ensembl_id: "ENSG00000163864"
name: "nicotinamide nucleotide adenylyltransferase 3"
location: "3q23"
module: 27
arm: "+"
pooled_cpm: 15.73
n_lines_expressing: 33
n_dd_up: 15
n_dd_down: 29
n_dd_up_clean: 12
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 12
direction_downstream: 11
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# NMNAT3

*nicotinamide nucleotide adenylyltransferase 3* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +7.5, q 5e-11, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.451× (z -11.5, q 1e-27, down in 24 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.271× (z -9.8, q 2e-20, down in 28 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1]] (+0.70, fdr 7e-06), [[VWA2]] (+0.68, fdr 1e-05), [[FGF20]] (+0.63, fdr 1e-05); moves opposite to [[MIR22HG]] (-0.43, fdr 1e-04), [[VPS9D1]] (-0.42, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[ENTREP2]] → it (grade B ⚠); 11 go from it, the strongest it → [[ENPP5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.5 | 5e-11 | 17/31 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +6.6 | 2e-08 | 19/29 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.29×** | +5.2 | 3e-05 | 15/30 (LoVo, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +4.8 | 3e-04 | 8/30 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.5 | 8e-04 | 12/30 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.011 | 11/30 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.011 | 7/30 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.014 | 7/30 (LS 180, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.028 | 6/29 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.4 | 0.045 | 2/30 (SW480, LS 180) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.25×** | +3.2 | 0.059 | 7/30 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.059 | 6/30 (BT-474, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.059 | 7/29 (LS 180, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.059 | 8/30 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.065 | 3/29 (HEC-1-A, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.065 | 1/31 (NCI-H1573) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8793.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.451×** | -11.5 | 1e-27 | 24/29 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.271×** | -9.8 | 2e-20 | 28/29 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.513×** | -9.6 | 1e-19 | 20/30 (SW480, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.514×** | -9.6 | 1e-19 | 23/30 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.572×** | -8.0 | 1e-13 | 18/30 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.591×** | -7.3 | 3e-11 | 19/28 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.383×** | -7.2 | 4e-11 | 18/28 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.640×** | -6.2 | 4e-08 | 17/30 (SK-MEL-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.652×** | -6.2 | 4e-08 | 17/30 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -6.2 | 4e-08 | 19/30 (SW480, HCT15, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.701×** | -5.1 | 2e-05 | 15/25 (SW48, SHP-77, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.731×** | -4.5 | 3e-04 | 12/30 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.732×** | -4.5 | 3e-04 | 12/30 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.735×** | -4.4 | 4e-04 | 14/30 (A549, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.738×** | -4.4 | 4e-04 | 15/29 (HEC-1-A, SNU-423, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.743×** | -4.3 | 7e-04 | 11/30 (SW480, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.748×** | -4.2 | 9e-04 | 12/29 (LS 180, NCI-H23, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.758×** | -3.9 | 0.004 | 13/30 (COLO 205, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.005 | 10/30 (SNU-423, J82, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.772×** | -3.6 | 0.008 | 8/31 (SW480, SW48, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.622×** | -3.6 | 0.008 | 8/29 (NCI-H1792, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.010 | 14/30 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.011 | 9/28 (Panc 03.27, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -3.4 | 0.015 | 10/30 (SW480, LoVo, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.4 | 0.015 | 11/29 (A549, SW48, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.751×** | -2.9 | 0.063 | 3/31 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 75.0 | 0 | 9 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.182× (z -15.6) |
| [[SW48 (line)]] | wt | 46.8 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0780× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.161× (z -10.7) |
| [[PANC-1 (line)]] | alt | 9.68 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.58× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.221× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0777× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 5.45 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 19.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.261× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0849× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.119× (z -8.9) ⚠ toxic |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.137× (z -10.5) |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 7.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.161× (z -9.4) |
| [[RKO (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0643× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SW1417 (line)]] | alt | 84.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[VWA2]] | +0.68 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[FGF20]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SHISA9]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[JAKMIP2-AS1]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[GPR143]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[COLGALT2]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LARGE2]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ST18]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[SLC30A10]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[SMOC2]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NKD1]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR22HG]] | -0.43 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[VPS9D1]] | -0.42 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 6, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTREP2]] | B | ENTREP2 activity raises NMNAT3's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without ENTREP2 | 0.036 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[SORL1]] | B | SORL1 activity raises NMNAT3's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.39× lower at baseline in the lines without SORL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[EMID1]] | B | EMID1 activity raises NMNAT3's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without EMID1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[LARGE2]] | B | LARGE2 activity raises NMNAT3's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.68× lower at baseline in the lines without LARGE2 | 0.057 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[LINC02981]] | B | LINC02981 activity raises NMNAT3's level | lines that do not express LINC02981 (14) vs lines expressing it (36) | 1.82× lower at baseline in the lines without LINC02981 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[APCDD1]] | B | APCDD1 activity raises NMNAT3's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.98× lower at baseline in the lines without APCDD1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[SMPDL3B]] | C | SMPDL3B activity raises NMNAT3's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 3.35× lower at baseline in the lines without SMPDL3B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |
| [[MEST]] | C | MEST activity raises NMNAT3's level | lines that do not express MEST (17) vs lines expressing it (33) | 2.97× lower at baseline in the lines without MEST | 0.005 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB; co-absent with the target |
| [[NOTUM]] | C | NOTUM activity raises NMNAT3's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without NOTUM | 0.006 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[COPG2IT1]] | C | COPG2IT1 activity raises NMNAT3's level | lines that do not express COPG2IT1 (12) vs lines expressing it (38) | 3.53× lower at baseline in the lines without COPG2IT1 | 0.026 | ⚠ within organs, on part of the lines; also absent: MEST, GLS2, NMNAT3; maybe low, not absent; co-absent with the target |
| [[SLC27A2]] | C | SLC27A2 activity raises NMNAT3's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 2.91× lower at baseline in the lines without SLC27A2 | 0.070 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656; co-absent with the target |
| [[CHDH]] | C | CHDH activity raises NMNAT3's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without CHDH | 0.089 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP5]] | B | NMNAT3 activity raises ENPP5's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.92× lower at baseline in the lines without NMNAT3 | 0.037 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[DCDC2]] | B | NMNAT3 activity raises DCDC2's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without NMNAT3 | 0.047 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[DTNB]] | B | NMNAT3 activity raises DTNB's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without NMNAT3 | 0.068 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[GSTO2]] | B | NMNAT3 activity raises GSTO2's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.76× lower at baseline in the lines without NMNAT3 | 0.072 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[GPR143]] | B | NMNAT3 activity raises GPR143's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without NMNAT3 | 0.076 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[LINC00923]] | B | NMNAT3 activity raises LINC00923's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 2.52× lower at baseline in the lines without NMNAT3 | 0.092 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[LARGE2]] | B | NMNAT3 activity raises LARGE2's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.80× lower at baseline in the lines without NMNAT3 | 0.097 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[ANGEL1]] | B | NMNAT3 activity raises ANGEL1's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without NMNAT3 | 0.098 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[SLC27A2]] | C | NMNAT3 activity raises SLC27A2's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 2.79× lower at baseline in the lines without NMNAT3 | 0.021 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C; co-absent with the target |
| [[CHDH]] | C | NMNAT3 activity raises CHDH's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 2.19× lower at baseline in the lines without NMNAT3 | 0.084 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C; co-absent with the target |
| [[SMPDL3B]] | C | NMNAT3 activity raises SMPDL3B's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 2.06× lower at baseline in the lines without NMNAT3 | 0.095 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.3, 44.0); signed map (62.3, 15.7). **Vector** length 59.8, 12.5% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +2.9 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +1.8 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[IQ 1 (drug)]] 5 µM |  | +1.2 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.7 | -9.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -9.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.5 | -4.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | nicotinamide nucleotide adenylyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:139,560,180-139,678,017 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PNAT3 |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T66](https://www.uniprot.org/uniprotkb/Q96T66) (Nicotinamide/nicotinic acid mononucleotide adenylyltransferase 3):

> Catalyzes the formation of NAD(+) from nicotinamide mononucleotide (NMN) and ATP. Can also use the deamidated form; nicotinic acid mononucleotide (NaMN) as substrate with the same efficiency. Can use triazofurin monophosphate (TrMP) as substrate. Can also use GTP and ITP as nucleotide donors. Also catalyzes the reverse reaction, i.e. the pyrophosphorolytic cleavage of NAD(+). For the pyrophosphorolytic activity, can use NAD(+), NADH, NaAD, nicotinic acid adenine dinucleotide phosphate (NHD), …

**Summary**, from NCBI Gene [349565](https://www.ncbi.nlm.nih.gov/gene/349565):

> This gene encodes a member of the nicotinamide/nicotinic acid mononucleotide adenylyltransferase family. These enzymes use ATP to catalyze the synthesis of nicotinamide adenine dinucleotide or nicotinic acid adenine dinucleotide from nicotinamide mononucleotide or nicotinic acid mononucleotide, respectively. The encoded protein is localized to mitochondria and may also play a neuroprotective role as a molecular chaperone. Alternatively spliced transcript variants encoding multiple isoforms have …

**Accessions** — [HGNC:20989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20989) · Entrez [349565](https://www.ncbi.nlm.nih.gov/gene/349565) · UniProt [Q96T66](https://www.uniprot.org/uniprotkb/Q96T66) · Ensembl [ENSG00000163864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163864)

## Data

Gene col 8793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8793); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8793]; `tensor/DDL_lfc|DDL_z.npy` [8793]; `embed/gene_vectors.npy` [8793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8793 or target_col == 8793). Every well: [[NMNAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMNAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
