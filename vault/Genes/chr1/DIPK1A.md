---
symbol: "DIPK1A"
type: "gene"
col: 7811
ensembl_id: "ENSG00000154511"
name: "divergent protein kinase domain 1A"
location: "1p22.1"
module: 65
arm: "+"
pooled_cpm: 42.49
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# DIPK1A

*divergent protein kinase domain 1A* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.46× (z +8.7, q 2e-15, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.553× (z -19.4, q 0e+00, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.525× (z -14.9, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGAP1]] (+0.55, fdr 1e-05), [[PPP3CC]] (+0.54, fdr 3e-05), [[TBK1]] (+0.53, fdr 1e-05); moves opposite to [[ITPRIPL2]] (-0.50, fdr 2e-05), [[LRGUK]] (-0.48, fdr 7e-05), [[NRP1]] (-0.47, fdr 8e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +8.7 | 2e-15 | 33/46 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +8.1 | 1e-13 | 25/46 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +6.0 | 4e-07 | 19/46 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +6.0 | 4e-07 | 25/46 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +5.8 | 9e-07 | 24/46 (LS 180, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +5.5 | 5e-06 | 20/45 (SW480, C32, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 21/46 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 1e-04 | 13/46 (LS 180, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +4.8 | 1e-04 | 13/45 (A498, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 2e-04 | 17/45 (C32, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +4.4 | 6e-04 | 20/46 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +4.2 | 0.001 | 16/46 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +4.1 | 0.002 | 12/46 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.004 | 12/46 (Panc 03.27, NCI-H2030, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.018 | 13/45 (H4, SW 900, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.019 | 16/46 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.019 | 9/46 (KATO III, C-33 A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.553×** | -19.4 | 0e+00 | 36/46 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.525×** | -14.9 | 0e+00 | 39/46 (C32, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -14.9 | 0e+00 | 40/46 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -12.6 | 2e-34 | 39/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.580×** | -12.6 | 3e-34 | 35/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.578×** | -12.2 | 4e-32 | 31/46 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -8.9 | 4e-17 | 33/46 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.706×** | -8.0 | 6e-14 | 30/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.716×** | -7.7 | 7e-13 | 27/46 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.719×** | -7.3 | 1e-11 | 26/45 (SNU-1, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.724×** | -7.2 | 4e-11 | 20/37 (A-427, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.739×** | -7.0 | 1e-10 | 25/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.768×** | -6.1 | 4e-08 | 22/45 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.788×** | -5.5 | 1e-06 | 21/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.807×** | -4.8 | 7e-05 | 18/46 (SW480, NCI-H460, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.905× | -3.3 | 0.034 | 7/46 (HS-578T, SHP-77, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.871× | -3.2 | 0.039 | 6/46 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.081 | 13/44 (HCT15, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 66.6 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -21.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -13.6) |
| [[C32 (line)]] | wt | 87.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -26.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.136× (z -18.3) |
| [[LS 180 (line)]] | wt | 48.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -18.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 100 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -9.0) |
| [[SW480 (line)]] | alt | 57.0 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.354× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.385× (z -11.9) |
| [[Hs 766T (line)]] | wt | 59.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -10.4) |
| [[SNU-1 (line)]] | wt | 57.9 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.3) |
| [[A498 (line)]] | wt | 54.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -9.9) |
| [[C-33 A (line)]] | alt | 68.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 42.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -11.2) |
| [[SNU-423 (line)]] | alt | 72.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -9.8) |
| [[LoVo (line)]] | wt | 40.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 32.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 39.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.440× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 57.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 61.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.349× (z -10.0) |
| [[A-427 (line)]] | wt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 44.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 12.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.169× (z -8.8) ⚠ toxic |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.107× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 85.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -14.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -18.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 19.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.30× (z +8.9) | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -8.5) |
| [[SHP-77 (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAP1]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PPP3CC]] | +0.54 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[TBK1]] | +0.53 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PLPP1]] | +0.52 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[NENF]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[AGTPBP1]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HACE1]] | +0.51 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[RHOBTB1]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[CRYZL1]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[PKIG]] | +0.49 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[CDON]] | +0.49 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[BLVRA]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPRIPL2]] | -0.50 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[LRGUK]] | -0.48 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[NRP1]] | -0.47 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[ARMCX4]] | -0.45 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PDCL3P4]] | -0.45 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[SLC37A2]] | -0.45 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[PLCH2]] | -0.45 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[SLC38A4-AS1]] | -0.44 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[THOC6]] | -0.43 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[NEK11]] | -0.43 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TTN-AS1]] | -0.43 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[PPP1R10]] | -0.43 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises DIPK1A's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without STARD9 | 0.087 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[PLCH2]] | B | PLCH2 activity lowers DIPK1A's level | lines that do not express PLCH2 (26) vs lines expressing it (24) | 1.45× higher at baseline in the lines without PLCH2 | 0.096 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent |
| [[GPR155]] | B | GPR155 activity raises DIPK1A's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without GPR155 | 0.097 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.372). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (19.3, -8.7); signed map (-16.7, 3.1). **Vector** length 94.2, 22.2% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -14.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.4 | -19.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | divergent protein kinase domain 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:92,832,737-92,961,522 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23493; previously FAM69A |
| Gene groups (HGNC) | Divergent protein kinase domain family |
| Matched by | ensembl_id |

UniProt [Q5T7M9](https://www.uniprot.org/uniprotkb/Q5T7M9) carries no function annotation.

**Summary**, from NCBI Gene [388650](https://www.ncbi.nlm.nih.gov/gene/388650):

> This gene encodes a member of the FAM69 family of cysteine-rich type II transmembrane proteins. These proteins localize to the endoplasmic reticulum but their specific functions are unknown. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:32213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32213) · Entrez [388650](https://www.ncbi.nlm.nih.gov/gene/388650) · UniProt [Q5T7M9](https://www.uniprot.org/uniprotkb/Q5T7M9) · Ensembl [ENSG00000154511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154511)

## Data

Gene col 7811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7811); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7811]; `tensor/DDL_lfc|DDL_z.npy` [7811]; `embed/gene_vectors.npy` [7811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7811 or target_col == 7811). Every well: [[DIPK1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIPK1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
