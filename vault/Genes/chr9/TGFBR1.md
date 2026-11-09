---
symbol: "TGFBR1"
type: "gene"
col: 2807
ensembl_id: "ENSG00000106799"
name: "transforming growth factor beta receptor 1"
location: "9q22.33"
module: 233
arm: "+"
pooled_cpm: 129.06
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/233"]
generated_by: "tahoemap"
---

# TGFBR1

*transforming growth factor beta receptor 1* — 9q22.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 2.54×, HepG2/C3A 2.49×, KATO III 1.80×); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (A549 1.94×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.580× (z -13.5, q 1e-38, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCSAP]] (+0.58, fdr 3e-05), [[TRIM36]] (+0.57, fdr 4e-05), [[KCTD9]] (+0.55, fdr 1e-05); moves opposite to [[TRIM16]] (-0.52, fdr 1e-05), [[PHF14]] (-0.50, fdr 1e-05), [[DDX10]] (-0.48, fdr 3e-05).
> It is in [[Module 233]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FIRRE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2807.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 2.54×, HepG2/C3A 2.49×, KATO III 1.80×); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (A549 1.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.9 | 0.051 | 15/49 (BT-474, A498, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.15× | +3.4 | 0.19 | 10/49 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.22 | 8/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.22 | 2/48 (C32, Hs 766T) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | 1.14× | +3.1 | 0.22 | 4/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.13× | +3.0 | 0.22 | 16/48 (BT-474, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2807.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.580×** | -13.5 | 1e-38 | 41/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.617×** | -11.9 | 2e-30 | 37/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.606×** | -11.9 | 2e-30 | 31/44 (J82, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.669×** | -9.9 | 5e-21 | 36/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -9.7 | 4e-20 | 37/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.776×** | -8.8 | 9e-17 | 26/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.689×** | -8.5 | 2e-15 | 27/45 (NCI-H23, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.715×** | -8.3 | 9e-15 | 31/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.532×** | -8.2 | 2e-14 | 36/49 (J82, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.719×** | -8.1 | 3e-14 | 28/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.713×** | -7.8 | 4e-13 | 31/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -7.6 | 1e-12 | 27/47 (NCI-H661, J82, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.757×** | -6.9 | 3e-10 | 31/49 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -6.6 | 2e-09 | 29/48 (HEC-1-A, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.774×** | -6.3 | 1e-08 | 28/48 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.792×** | -5.5 | 1e-06 | 25/48 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.665×** | -5.3 | 4e-06 | 23/48 (SNU-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.699×** | -4.6 | 1e-04 | 20/48 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.713×** | -4.4 | 4e-04 | 23/48 (A549, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.732×** | -4.0 | 0.001 | 20/47 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.852× | -3.9 | 0.002 | 18/48 (SNU-423, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 562 | 0 | 28 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -24.0) |
| [[A-172 (line)]] | wt | 235 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -30.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.268× (z -26.4) |
| [[HEC-1-A (line)]] | alt | 142 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -15.2) |
| [[A549 (line)]] | wt | 225 | 1 | 9 (4 ⚠) | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 1.94× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -17.9) |
| [[J82 (line)]] | alt | 230 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -18.6) |
| [[C32 (line)]] | wt | 206 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 73.8 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.344× (z -11.3) |
| [[Hs 766T (line)]] | wt | 145 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.376× (z -9.8) |
| [[LoVo (line)]] | wt | 85.2 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.593× (z -10.4) |
| [[SNU-1 (line)]] | wt | 99.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.145× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 264 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.415× (z -10.6) |
| [[HS-578T (line)]] | alt | 103 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.173× (z -9.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.457× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 88.9 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.519× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 177 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.474× (z -9.0) |
| [[SW480 (line)]] | alt | 78.6 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.474× (z -11.5) |
| [[BT-474 (line)]] | alt | 96.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -9.4) |
| [[HOP62 (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 60.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.478× (z -9.1) |
| [[SNU-423 (line)]] | alt | 210 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -13.8) |
| [[SW 900 (line)]] | alt | 124 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.6) |
| [[A-427 (line)]] | wt | 52.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.431× (z -9.2) |
| [[A498 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HepG2_C3A (line)]] | wt | 69.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 97.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.4) |
| [[KATO III (line)]] | alt | 56.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.7) |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0757× (z -9.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 82.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.407× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 104 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.4) | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 106 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCSAP]] | +0.58 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[TRIM36]] | +0.57 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[KCTD9]] | +0.55 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CDK2AP2]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[KATNA1]] | +0.53 | +0.40 / +0.49 | both halves | 4e-05 |  |
| [[YPEL1]] | +0.50 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[CNIH4]] | +0.50 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TMEM50B]] | +0.50 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TUBGCP5]] | +0.50 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[UNC119]] | +0.50 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[APAF1]] | +0.49 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ATP11B]] | +0.49 | +0.56 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM16]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PHF14]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[DDX10]] | -0.48 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[NOL10]] | -0.48 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[COMMD10]] | -0.47 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[BCCIP]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[LINC01278]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TASP1]] | -0.46 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[LSG1]] | -0.45 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TTN-AS1]] | -0.44 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CWC27]] | -0.44 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MRRF]] | -0.44 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FIRRE]] | B | FIRRE activity weakens TGFBR1's drug response | lines that do not express FIRRE (18) vs lines expressing it (31) | the lines without FIRRE respond 1.63× as strongly (z diff -1.72); strongest at Dinaciclib 0.05 µM: 0.57x vs 0.77x (z diff -3.3) | 0.088 | ⚠ within organs, on part of the lines; also absent: HMCN1, GAP43, ENSG00000286033; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 233]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.2, -24.6); signed map (-23.2, 16.6). **Vector** length 96.1, 23.5% of its response variance represented; |z| ≥ 3 in 1,351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.0 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.5 | -8.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.0 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -6.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:99,104,038-99,154,192 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALK-5, ACVRLK4, ALK5, TBRI, TBR-i; previously MSSE, ESS1 |
| Gene groups (HGNC) | Type 1 receptor serine/threonine kinases |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 19 pathways, smallest: Loss of Function of TGFBR2 in Cancer; TGFBR2 Kinase Domain Mutants in Cancer; TGFBR1 LBD Mutants in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P36897](https://www.uniprot.org/uniprotkb/P36897) (TGF-beta receptor type-1):

> Transmembrane serine/threonine kinase forming with the TGF-beta type II serine/threonine kinase receptor, TGFBR2, the non-promiscuous receptor for the TGF-beta cytokines TGFB1, TGFB2 and TGFB3. Transduces the TGFB1, TGFB2 and TGFB3 signal from the cell surface to the cytoplasm and is thus regulating a plethora of physiological and pathological processes including cell cycle arrest in epithelial and hematopoietic cells, control of mesenchymal cell proliferation and differentiation, wound …

**Summary**, from NCBI Gene [7046](https://www.ncbi.nlm.nih.gov/gene/7046):

> The protein encoded by this gene forms a heteromeric complex with type II TGF-beta receptors when bound to TGF-beta, transducing the TGF-beta signal from the cell surface to the cytoplasm. The encoded protein is a serine/threonine protein kinase. Mutations in this gene have been associated with Loeys-Dietz aortic aneurysm syndrome (LDAS). Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:11772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11772) · Entrez [7046](https://www.ncbi.nlm.nih.gov/gene/7046) · UniProt [P36897](https://www.uniprot.org/uniprotkb/P36897) · Ensembl [ENSG00000106799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106799)

## Data

Gene col 2807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2807); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2807]; `tensor/DDL_lfc|DDL_z.npy` [2807]; `embed/gene_vectors.npy` [2807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2807 or target_col == 2807). Every well: [[TGFBR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFBR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
