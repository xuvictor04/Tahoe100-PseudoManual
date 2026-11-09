---
symbol: "PUS7"
type: "gene"
col: 1651
ensembl_id: "ENSG00000091127"
name: "pseudouridine synthase 7"
location: "7q22.3"
module: 18
arm: "+"
pooled_cpm: 86.16
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PUS7

*pseudouridine synthase 7* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.78× (z +14.2, q 9e-43, up in 46 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.55× (z +10.8, q 9e-25, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.716× (z -11.7, q 8e-29, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3G]] (+0.72, fdr 7e-06), [[XPO5]] (+0.71, fdr 7e-06), [[MDN1]] (+0.69, fdr 7e-06); moves opposite to [[MAGED2]] (-0.61, fdr 8e-06), [[KDM5A]] (-0.55, fdr 1e-05), [[FBXO8]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RILPL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.78×** | +14.2 | 9e-43 | 46/47 (NCI-H460, SW1417, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +10.8 | 9e-25 | 36/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +9.9 | 8e-21 | 35/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +9.7 | 6e-20 | 34/47 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +9.6 | 1e-19 | 35/47 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +8.1 | 6e-14 | 33/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +7.7 | 8e-13 | 27/47 (Hs 766T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +6.4 | 1e-08 | 27/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +6.0 | 1e-07 | 21/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.8 | 5e-07 | 27/47 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +5.7 | 5e-07 | 29/47 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.54×** | +5.5 | 2e-06 | 26/47 (NCI-H23, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +5.5 | 2e-06 | 27/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.52×** | +5.4 | 3e-06 | 25/47 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 5e-05 | 23/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +4.4 | 3e-04 | 21/47 (HCT15, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +4.4 | 3e-04 | 20/47 (BT-474, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.716×** | -11.7 | 8e-29 | 30/47 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.672×** | -9.8 | 2e-20 | 28/47 (C32, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.784×** | -8.5 | 3e-15 | 31/47 (J82, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -8.3 | 2e-14 | 33/48 (SNU-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.832×** | -4.6 | 5e-04 | 16/47 (KATO III, A498, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.836× | -4.4 | 9e-04 | 16/48 (LOX-IMVI, HCT15, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.719×** | -4.3 | 0.002 | 17/46 (C32, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.724×** | -4.2 | 0.002 | 18/47 (HCT15, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.791×** | -4.1 | 0.002 | 17/47 (HEC-1-A, NCI-H661, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.865× | -4.0 | 0.003 | 13/47 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.852× | -3.8 | 0.007 | 21/47 (RKO, SNU-1, …) | top dose only | composition shift |
| [[AZD-7648 (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.024 | 14/47 (C32, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.873× | -3.4 | 0.032 | 17/46 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.882× | -3.3 | 0.039 | 10/49 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.879× | -3.2 | 0.050 | 13/47 (C32, AN3 CA, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.878× | -3.1 | 0.065 | 15/47 (MIA PaCa-2, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 281 | 1 (1 ⚠) | 10 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.93× (z +8.7) ⚠ unreliable plate only | [[Auranofin (drug)]] 5 µM 0.259× (z -17.9) |
| [[SNU-1 (line)]] | wt | 135 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 111 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 260 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -15.0) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.521× (z -12.9) |
| [[RKO (line)]] | wt | 147 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.329× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -13.0) |
| [[SW480 (line)]] | alt | 107 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.31× (z +11.0) | — |
| [[A-427 (line)]] | wt | 85.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -24.5) |
| [[A549 (line)]] | wt | 80.8 | 2 | 1 | [[Bortezomib (drug)]] 0.05 µM 2.34× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -8.9) |
| [[Hs 766T (line)]] | wt | 55.7 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.69× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +8.6) | [[Selinexor (drug)]] 5 µM 0.490× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 98.5 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.211× (z -17.6) |
| [[A-172 (line)]] | wt | 87.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.9) |
| [[C-33 A (line)]] | alt | 194 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 83.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.485× (z -9.6) |
| [[HS-578T (line)]] | alt | 71.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.425× (z -9.1) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.558× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 47.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.66× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 112 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 1.94× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.647× (z -9.0) |
| [[SW48 (line)]] | wt | 139 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.307× (z -10.8) |
| [[A498 (line)]] | wt | 65.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.01× (z +9.0) ⚠ unreliable plate only | — |
| [[AsPC-1 (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +8.5) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[CFPAC-1 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +8.9) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[CHP-212 (line)]] | wt | 75.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 88.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.54× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 94.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -10.3) |
| [[HT-29 (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +8.5) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[J82 (line)]] | alt | 103 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.427× (z -14.3) |
| [[KATO III (line)]] | alt | 66.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 70.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.9) |
| [[LS 180 (line)]] | wt | 48.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 52.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.58× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -17.0) |
| [[NCI-H2347 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.72× (z +9.1) ⚠ unreliable plate only | — |
| [[SNU-423 (line)]] | alt | 82.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -16.7) |
| [[SW1417 (line)]] | alt | 75.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.29× (z +9.5) ⚠ unreliable plate only | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3G]] | +0.72 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[XPO5]] | +0.71 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MDN1]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[UBE3C]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[DKC1]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 | same gene group; STRING 832 |
| [[NLN]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ANAPC1]] | +0.67 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[GARNL3]] | +0.66 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[RILPL1]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.65 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 | pathway: tRNA processing |
| [[SFXN4]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGED2]] | -0.61 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[KDM5A]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[FBXO8]] | -0.55 | -0.63 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises PUS7's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.31× lower at baseline in the lines without NT5M | 0.006 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[ADCY3]] | B | ADCY3 activity raises PUS7's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without ADCY3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[NCS1]] | B | NCS1 activity raises PUS7's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without NCS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises PUS7's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.60× lower at baseline in the lines without FAM78B | 0.039 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[NT5M]] | B | NT5M activity strengthens PUS7's drug response | lines that do not express NT5M (6) vs lines expressing it (42) | the lines without NT5M respond 0.87× as strongly (z diff +0.88); strongest at Homoharringtonine 5 µM: 1.38x vs 0.66x (z diff +9.5) | 0.066 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG; target measured in part of the lines; both ways; artifact flags |
| [[MTHFD1L]], [[USP31]] | C | MTHFD1L, USP31 activity raises PUS7's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.89× lower at baseline in the lines without MTHFD1L, USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RILPL1]] | C | PUS7's natural level strengthens RILPL1's drug response | PUS7's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.07; direction clear | 0.002 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.794). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.8, -35.8); signed map (-4.7, -53.1). **Vector** length 146, 47.3% of its response variance represented; |z| ≥ 3 in 1,372 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.3 | +14.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +10.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.7 | +5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.1 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.0 | +8.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +6.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.9 | +5.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.4 | -11.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.8 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -9.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.0 | -8.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.9 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -4.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | pseudouridine synthase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:105,439,661-105,522,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20485 |
| Gene groups (HGNC) | Pseudouridine synthases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PZ0](https://www.uniprot.org/uniprotkb/Q96PZ0) (Pseudouridylate synthase 7 homolog):

> Pseudouridylate synthase that catalyzes pseudouridylation of RNAs. Acts as a regulator of protein synthesis in embryonic stem cells by mediating pseudouridylation of RNA fragments derived from tRNAs (tRFs): pseudouridylated tRFs inhibit translation by targeting the translation initiation complex. Also catalyzes pseudouridylation of mRNAs: mediates pseudouridylation of mRNAs with the consensus sequence 5'-UGUAG-3'. Acts as a regulator of pre-mRNA splicing by mediating pseudouridylation of …

**Summary**, from NCBI Gene [54517](https://www.ncbi.nlm.nih.gov/gene/54517):

> Enables enzyme binding activity and tRNA pseudouridine(13) synthase activity. Involved in several processes, including pseudouridine synthesis; regulation of hematopoietic stem cell differentiation; and regulation of mesoderm development. Is active in nucleus. Implicated in intellectual developmental disorder with abnormal behavior, microcephaly, and short stature. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26033) · Entrez [54517](https://www.ncbi.nlm.nih.gov/gene/54517) · UniProt [Q96PZ0](https://www.uniprot.org/uniprotkb/Q96PZ0) · Ensembl [ENSG00000091127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091127)

## Data

Gene col 1651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1651); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1651]; `tensor/DDL_lfc|DDL_z.npy` [1651]; `embed/gene_vectors.npy` [1651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1651 or target_col == 1651). Every well: [[PUS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
