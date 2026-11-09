---
symbol: "FOXK2"
type: "gene"
col: 6548
ensembl_id: "ENSG00000141568"
name: "forkhead box K2"
location: "17q25.3"
module: 3
arm: "+"
pooled_cpm: 111.29
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# FOXK2

*forkhead box K2* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.68× (z +10.4, q 1e-22, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.631× (z -13.2, q 9e-37, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIRA]] (+0.74, fdr 7e-06), [[CSNK1G2]] (+0.73, fdr 7e-06), [[UBE2G1]] (+0.73, fdr 7e-06); moves opposite to [[DZIP3]] (-0.67, fdr 1e-05), [[FUNDC1]] (-0.63, fdr 1e-05), [[SF3B1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +10.4 | 1e-22 | 41/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +10.3 | 1e-22 | 44/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +9.7 | 6e-20 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +9.6 | 1e-19 | 42/48 (C32, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +9.5 | 2e-19 | 39/48 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +9.4 | 7e-19 | 44/49 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +8.9 | 4e-17 | 37/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.4 | 3e-15 | 32/49 (CFPAC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +8.2 | 1e-14 | 36/47 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +8.1 | 3e-14 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +7.7 | 6e-13 | 36/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +6.5 | 4e-09 | 38/48 (MIA PaCa-2, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +5.8 | 4e-07 | 34/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.2 | 1e-05 | 36/48 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.9 | 5e-05 | 21/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +4.7 | 9e-05 | 19/48 (A549, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +4.5 | 2e-04 | 27/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.631×** | -13.2 | 9e-37 | 42/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.677×** | -7.9 | 9e-13 | 35/49 (SW48, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.689×** | -7.5 | 1e-11 | 36/48 (A-427, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.772×** | -5.2 | 3e-05 | 30/49 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -5.1 | 3e-05 | 25/44 (SK-MEL-2, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.768×** | -4.9 | 8e-05 | 25/45 (SW48, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.845× | -4.8 | 1e-04 | 21/48 (A-172, C32, …) | all doses, stronger at high dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.770×** | -3.6 | 0.023 | 22/48 (LoVo, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.6 | 0.023 | 20/48 (A498, C32, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.842× | -3.5 | 0.028 | 21/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.4 | 0.030 | 22/48 (A498, RKO, …) | all doses, flat | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.846× | -3.4 | 0.035 | 15/48 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.2 | 0.061 | 15/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.073 | 17/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.860× | -3.1 | 0.086 | 14/47 (LoVo, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 118 | 12 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.60× (z +14.5) | [[Selinexor (drug)]] 5 µM 0.644× (z -9.3) |
| [[COLO 205 (line)]] | alt | 65.0 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.94× (z +13.6) | — |
| [[HOP62 (line)]] | alt | 101 | 6 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.55× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.7) | [[Selinexor (drug)]] 5 µM 0.569× (z -8.5) |
| [[LS 180 (line)]] | wt | 105 | 6 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.33× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +14.0) | [[Selinexor (drug)]] 5 µM 0.508× (z -11.8) |
| [[PANC-1 (line)]] | alt | 163 | 4 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.15× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.500× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.656× (z -8.8) |
| [[A-427 (line)]] | wt | 154 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -19.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.420× (z -18.0) |
| [[C32 (line)]] | wt | 136 | 2 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.13× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -20.3) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.510× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 109 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.20× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.535× (z -11.2) |
| [[RKO (line)]] | wt | 120 | 1 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 4.17× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.354× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.567× (z -10.2) |
| [[BT-474 (line)]] | alt | 141 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -11.7) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Selinexor (drug)]] 0.5 µM 0.472× (z -10.1) |
| [[Hs 766T (line)]] | wt | 57.9 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.88× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.459× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 94.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.5) ⚠ cell-cycle shift, explains ~7% of this change |
| [[SNU-423 (line)]] | alt | 59.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +10.9) | — |
| [[A-172 (line)]] | wt | 85.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.3) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A498 (line)]] | wt | 96.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.351× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.584× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 50.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 98.7 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.535× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 109 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.63× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.59× (z +9.5) | — |
| [[SW48 (line)]] | wt | 146 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.64× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -12.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 132 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.92× (z +10.3) | [[Selinexor (drug)]] 5 µM 0.567× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 64.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.429× (z -11.6) |
| [[C-33 A (line)]] | alt | 173 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -12.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 66.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -9.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -10.6) ⚠ cell-cycle shift, explains ~7% of this change |
| [[LoVo (line)]] | wt | 97.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.612× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 132 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.30× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 92.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.56× (z +9.7) | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 161 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 117 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.613× (z -8.7) |
| [[A549 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 141 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 220 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIRA]] | +0.74 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[CSNK1G2]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[SLC27A4]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TSEN54]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD13D]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[PGP]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TAF4]] | +0.65 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[DCUN1D2]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[DEXI]] | +0.65 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[SRPK2]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZIP3]] | -0.67 | -0.76 / -0.50 | both halves | 1e-05 |  |
| [[FUNDC1]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SF3B1]] | -0.62 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[TAF9]] | -0.61 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[TOR1AIP1]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.61 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.60 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[POLR2M]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[RBM7]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[SMARCA1]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GDAP1]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises FOXK2's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without NT5M | 0.032 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[ANKRD13B]] | C | ANKRD13B activity raises FOXK2's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without ANKRD13B | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.7, -4.2); signed map (-42.2, 0.7). **Vector** length 133, 47.1% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.0 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.3 | +8.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +8.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +2.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +9.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +3.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -13.9 | -13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -12.4 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -11.2 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -10.6 | -2.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -8.7 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box K2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,519,713-82,644,662 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ILF, ILF1 |
| Gene groups (HGNC) | Forkhead boxes |
| Reactome | 2 pathways, smallest: UCH proteinases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01167](https://www.uniprot.org/uniprotkb/Q01167) (Forkhead box protein K2):

> Transcriptional regulator involved in different processes such as glucose metabolism, aerobic glycolysis and autophagy. Recognizes and binds the forkhead DNA sequence motif (5'-GTAAACA-3') and can both act as a transcription activator or repressor, depending on the context. Together with FOXK1, acts as a key regulator of metabolic reprogramming towards aerobic glycolysis, a process in which glucose is converted to lactate in the presence of oxygen (By similarity). Acts by promoting expression …

**Summary**, from NCBI Gene [3607](https://www.ncbi.nlm.nih.gov/gene/3607):

> The protein encoded by this gene contains a fork head DNA binding domain. This protein can bind to the purine-rich motifs of the HIV long terminal repeat (LTR), and to the similar purine-rich motif in the interleukin 2 (IL2) promoter. It may be involved in the regulation of viral and cellular promoter elements. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6036) · Entrez [3607](https://www.ncbi.nlm.nih.gov/gene/3607) · UniProt [Q01167](https://www.uniprot.org/uniprotkb/Q01167) · Ensembl [ENSG00000141568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141568)

## Data

Gene col 6548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6548); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6548]; `tensor/DDL_lfc|DDL_z.npy` [6548]; `embed/gene_vectors.npy` [6548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6548 or target_col == 6548). Every well: [[FOXK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
