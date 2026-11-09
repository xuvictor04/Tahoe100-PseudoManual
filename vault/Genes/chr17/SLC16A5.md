---
symbol: "SLC16A5"
type: "gene"
col: 9913
ensembl_id: "ENSG00000170190"
name: "solute carrier family 16 member 5"
location: "17q25.1"
module: 31
arm: "+"
pooled_cpm: 9.83
n_lines_expressing: 35
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 8
direction_downstream: 17
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# SLC16A5

*solute carrier family 16 member 5* — 17q25.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.377× (z -17.3, q 0e+00, down in 26 of 32 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.348× (z -13.2, q 1e-37, down in 27 of 33 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC3]] (+0.60, fdr 1e-05), [[BAIAP2L2]] (+0.56, fdr 2e-05), [[TNS4]] (+0.55, fdr 1e-05); moves opposite to [[EYA1]] (-0.48, fdr 4e-05), [[IGFBP5]] (-0.45, fdr 8e-05), [[LINC01098]] (-0.44, fdr 5e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ALS2CL]] → it (grade B ⚠); 17 go from it, the strongest it → [[PSD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.43× | +3.2 | 0.25 | 2/30 (NCI-H460, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.29× | +3.2 | 0.25 | 8/32 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.25 | 7/31 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.28× | +3.1 | 0.25 | 8/32 (A549, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.377×** | -17.3 | 0e+00 | 26/32 (NCI-H1573, HT-29, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.348×** | -13.2 | 1e-37 | 27/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.357×** | -12.9 | 6e-36 | 27/33 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.375×** | -11.8 | 5e-30 | 25/33 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.449×** | -10.0 | 1e-21 | 26/33 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -9.1 | 1e-17 | 24/31 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.509×** | -8.4 | 2e-15 | 23/33 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.279×** | -8.4 | 4e-15 | 24/28 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.315×** | -7.6 | 2e-12 | 24/33 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.573×** | -7.0 | 2e-10 | 19/31 (HT-29, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.602×** | -6.4 | 1e-08 | 18/33 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.608×** | -6.0 | 1e-07 | 17/29 (NCI-H23, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.628×** | -5.8 | 3e-07 | 15/33 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -4.7 | 1e-04 | 12/32 (SW480, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.725×** | -4.0 | 0.002 | 15/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.725×** | -3.8 | 0.005 | 8/32 (RPMI-7951, KATO III, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.758×** | -3.5 | 0.016 | 12/31 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -3.2 | 0.044 | 6/33 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.704×** | -3.1 | 0.048 | 6/33 (NCI-H1792, SW1417, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.772×** | -3.1 | 0.049 | 5/32 (NCI-H1573, MIA PaCa-2, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.639×** | -2.9 | 0.076 | 9/29 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.6 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.125× (z -15.9) |
| [[HT-29 (line)]] | alt | 45.0 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -16.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0842× (z -12.7) |
| [[PANC-1 (line)]] | alt | 12.2 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.105× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.179× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 24.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0474× (z -19.6) |
| [[KATO III (line)]] | alt | 17.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0860× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -14.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.144× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -9.1) |
| [[A549 (line)]] | wt | 15.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -9.2) |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0734× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.134× (z -10.0) |
| [[LoVo (line)]] | wt | 11.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -12.9) |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 17.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -8.6) |
| [[COLO 205 (line)]] | alt | 9.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 6.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 6.24 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0663× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 5.04 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0583× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 3.83 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0802× (z -11.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 4.26 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0384× (z -10.5) |
| [[RKO (line)]] | wt | 6.00 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0716× (z -8.5) |
| [[A-172 (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.966 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.875 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.957 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC3]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[BAIAP2L2]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TNS4]] | +0.55 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[PSD4]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[CAPN8]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MST1R]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TNNT2]] | +0.52 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[PDE9A]] | +0.52 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.51 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[DIO3OS]] | +0.51 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[IQANK1]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[LRP5]] | +0.50 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EYA1]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[IGFBP5]] | -0.45 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[LINC01098]] | -0.44 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[IGFBP3]] | -0.44 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[ZNF521]] | -0.43 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[EDNRA]] | -0.41 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[PLOD2]] | -0.40 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[UFSP2]] | -0.40 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[DPYSL3]] | -0.40 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[CFAP20DC]] | -0.40 | -0.35 / -0.32 | both halves | 1e-04 |  |
| [[TUBA1A]] | -0.39 | -0.44 / -0.24 | both halves | 5e-04 |  |
| [[RARB]] | -0.39 | -0.32 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALS2CL]] | B | ALS2CL activity raises SLC16A5's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.96× lower at baseline in the lines without ALS2CL | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[PDE9A]] | B | PDE9A activity raises SLC16A5's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without PDE9A | 0.028 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[BCL2L1]] | B | BCL2L1 activity raises SLC16A5's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 3.10× lower at baseline in the lines without BCL2L1 | 0.028 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[EPHA2-AS1]] | B | EPHA2-AS1 activity raises SLC16A5's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 3.20× lower at baseline in the lines without EPHA2-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[IQANK1]] | B | IQANK1 activity raises SLC16A5's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.63× lower at baseline in the lines without IQANK1 | 0.080 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[TNS4]] | B | TNS4 activity raises SLC16A5's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.83× lower at baseline in the lines without TNS4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[S100P]] | B | S100P activity raises SLC16A5's level | lines that do not express S100P (34) vs lines expressing it (16) | 2.91× lower at baseline in the lines without S100P | 0.093 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6 |
| [[ARHGEF16]] | C | ARHGEF16 activity raises SLC16A5's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 3.44× lower at baseline in the lines without ARHGEF16 | 0.082 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSD4]] | B | SLC16A5 activity raises PSD4's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 2.72× lower at baseline in the lines without SLC16A5 | 0.017 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[BCL2L1]] | B | SLC16A5 activity raises BCL2L1's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without SLC16A5 | 0.028 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[ABCC3]] | B | SLC16A5 activity raises ABCC3's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without SLC16A5 | 0.029 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[ITGB4]] | B | SLC16A5 activity raises ITGB4's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 4.87× lower at baseline in the lines without SLC16A5 | 0.030 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[TNFRSF1A]] | B | SLC16A5 activity raises TNFRSF1A's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without SLC16A5 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[B3GNT3]] | B | SLC16A5 activity raises B3GNT3's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 3.40× lower at baseline in the lines without SLC16A5 | 0.040 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[PDE9A]] | B | SLC16A5 activity raises PDE9A's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without SLC16A5 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[ALS2CL]] | B | SLC16A5 activity raises ALS2CL's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 2.82× lower at baseline in the lines without SLC16A5 | 0.067 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[TNS4]] | B | SLC16A5 activity raises TNS4's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 3.90× lower at baseline in the lines without SLC16A5 | 0.072 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[RARB]] | B | SLC16A5 activity lowers RARB's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 2.88× higher at baseline in the lines without SLC16A5 | 0.078 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[LPAR2]] | B | SLC16A5 activity raises LPAR2's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 1.17× lower at baseline in the lines without SLC16A5 | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[HTR1D]] | B | SLC16A5 activity raises HTR1D's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 1.93× lower at baseline in the lines without SLC16A5 | 0.082 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, 49.7); signed map (5.5, 36.6). **Vector** length 69.4, 15.3% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.6 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.9 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | -0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -13.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -9.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 16 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,087,727-75,106,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCT5, MCT6 |
| Gene groups (HGNC) | Solute carrier family 16 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15375](https://www.uniprot.org/uniprotkb/O15375) (Monocarboxylate transporter 6):

> Proton-linked monocarboxylate transporter. Catalyzes the rapid transport across the plasma membrane of many monocarboxylates such as lactate, pyruvate, branched-chain oxo acids derived from leucine, valine and isoleucine, and the ketone bodies acetoacetate, beta-hydroxybutyrate and acetate (By similarity).

**Summary**, from NCBI Gene [9121](https://www.ncbi.nlm.nih.gov/gene/9121):

> This gene encodes a member of the monocarboxylate transporter family and the major facilitator superfamily. The encoded protein is localized to the cell membrane and acts as a proton-linked transporter of bumetanide. Transport by the encoded protein is inhibited by four loop diuretics, nateglinide, thiazides, probenecid, and glibenclamide. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:10926](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10926) · Entrez [9121](https://www.ncbi.nlm.nih.gov/gene/9121) · UniProt [O15375](https://www.uniprot.org/uniprotkb/O15375) · Ensembl [ENSG00000170190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170190)

## Data

Gene col 9913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9913); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9913]; `tensor/DDL_lfc|DDL_z.npy` [9913]; `embed/gene_vectors.npy` [9913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9913 or target_col == 9913). Every well: [[SLC16A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
