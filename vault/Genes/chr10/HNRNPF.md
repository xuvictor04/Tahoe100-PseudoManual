---
symbol: "HNRNPF"
type: "gene"
col: 9856
ensembl_id: "ENSG00000169813"
name: "heterogeneous nuclear ribonucleoprotein F"
location: "10q11.21"
module: 1
arm: "+"
pooled_cpm: 88.97
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# HNRNPF

*heterogeneous nuclear ribonucleoprotein F* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.89× (z +21.1, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.826× (z -6.9, q 3e-09, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.815× (z -5.2, q 5e-05, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 0.336×, HEC-1-A 0.329×, SNU-1 0.382×, NCI-H23 0.469×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.249×, NCI-H2030 0.412×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (PANC-1 0.533×, HT-29 0.532×); [[Belinostat (drug)]] 5 µM in 1 line (PANC-1 0.612×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRWD1]] (+0.68, fdr 7e-06), [[SF3B3]] (+0.68, fdr 7e-06), [[URB2]] (+0.66, fdr 7e-06); moves opposite to [[KCTD9]] (-0.59, fdr 1e-05), [[GABARAPL2]] (-0.59, fdr 1e-05), [[RAB6A]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.89×** | +21.1 | 0e+00 | 48/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.33×** | +15.9 | 0e+00 | 42/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +10.8 | 1e-24 | 41/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +10.4 | 3e-23 | 40/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +9.7 | 2e-20 | 40/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +9.5 | 2e-19 | 34/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +9.1 | 5e-18 | 38/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +8.4 | 4e-15 | 31/48 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +8.3 | 6e-15 | 32/48 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.37×** | +8.0 | 8e-14 | 31/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.21×** | +6.8 | 5e-10 | 23/48 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +6.8 | 5e-10 | 28/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.4 | 4e-04 | 21/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.19× | +4.4 | 5e-04 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +4.2 | 8e-04 | 17/48 (C32, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 21/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.015 | 13/48 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.017 | 19/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.082 | 9/49 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9856.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 0.336×, HEC-1-A 0.329×, SNU-1 0.382×, NCI-H23 0.469×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.249×, NCI-H2030 0.412×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (PANC-1 0.533×, HT-29 0.532×); [[Belinostat (drug)]] 5 µM in 1 line (PANC-1 0.612×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.826×** | -6.9 | 3e-09 | 23/48 (LoVo, A-427, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **0.815×** | -5.2 | 5e-05 | 24/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.822×** | -5.0 | 1e-04 | 23/48 (HCT15, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.832×** | -4.7 | 4e-04 | 22/48 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.860× | -3.7 | 0.024 | 19/47 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.866× | -3.7 | 0.024 | 17/49 (CHP-212, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.916× | -3.2 | 0.12 | 7/48 (PANC-1, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.915× | -3.1 | 0.14 | 7/49 (SW480, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 155 | 12 (5 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.32× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.533× (z -11.4) |
| [[A-172 (line)]] | wt | 75.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +16.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.35× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 84.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.7) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +10.5) | — |
| [[A549 (line)]] | wt | 86.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.45× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 46.7 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.22× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 78.1 | 5 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.73× (z +12.8) | — |
| [[SNU-1 (line)]] | wt | 123 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.00× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 88.4 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.81× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 78.3 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.19× (z +10.2) | — |
| [[LoVo (line)]] | wt | 100 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.49× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 63.6 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.52× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 89.0 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.52× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 80.8 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.35× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 83.0 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 132 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.79× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.644× (z -9.0) ⚠ cell-cycle shift, explains ~59% of this change |
| [[COLO 205 (line)]] | alt | 94.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 80.7 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.62× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 133 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.92× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.532× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 37.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 86.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.94× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 89.4 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.21× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 116 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.91× (z +10.7) | — |
| [[A-427 (line)]] | wt | 112 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.53× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 112 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.63× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 44.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.08× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 54.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.24× (z +8.6) | — |
| [[RKO (line)]] | wt | 134 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.20× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 57.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.09× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 90.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.89× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 81.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.67× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 72.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.94× (z +8.8) | — |
| [[SW48 (line)]] | wt | 101 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.75× (z +9.0) | — |
| [[A498 (line)]] | wt | 97.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 115 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRWD1]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[SF3B3]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 431 |
| [[URB2]] | +0.66 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[BYSL]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[UTP15]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ADO]] | +0.62 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[NOP2]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PATZ1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MYC]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 | STRING 403 |
| [[DNAAF2]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PUF60]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 557 |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD9]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[GABARAPL2]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[SELENOW]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CCS]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[F11R]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[STX12]] | -0.56 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[PPP2R5B]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MXD1]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[RUFY2]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TALAM1]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[CBFA2T2]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HNRNPF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.6, -35.8); signed map (3.0, -40.4). **Vector** length 116, 33.5% of its response variance represented; |z| ≥ 3 in 1,166 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.3 | +21.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.5 | +15.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +10.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +9.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.8 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -1.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.6 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.2 | -6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.8 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:43,385,617-43,409,186 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNRPF |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 18 pathways, smallest: FGFR2 alternative splicing; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P52597](https://www.uniprot.org/uniprotkb/P52597) (Heterogeneous nuclear ribonucleoprotein F):

> Component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complexes which provide the substrate for the processing events that pre-mRNAs undergo before becoming functional, translatable mRNAs in the cytoplasm. Plays a role in the regulation of alternative splicing events. Binds G-rich sequences in pre-mRNAs and keeps target RNA in an unfolded state.

**Summary**, from NCBI Gene [3185](https://www.ncbi.nlm.nih.gov/gene/3185):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and regulate alternative splicing, polyadenylation, and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins …

**Accessions** — [HGNC:5039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5039) · Entrez [3185](https://www.ncbi.nlm.nih.gov/gene/3185) · UniProt [P52597](https://www.uniprot.org/uniprotkb/P52597) · Ensembl [ENSG00000169813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169813)

## Data

Gene col 9856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9856); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9856]; `tensor/DDL_lfc|DDL_z.npy` [9856]; `embed/gene_vectors.npy` [9856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9856 or target_col == 9856). Every well: [[HNRNPF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
