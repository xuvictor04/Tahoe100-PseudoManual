---
symbol: "SLC35E1"
type: "gene"
col: 4817
ensembl_id: "ENSG00000127526"
name: "solute carrier family 35 member E1"
location: "19p13.11"
module: 40
arm: "+"
pooled_cpm: 81.45
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SLC35E1

*solute carrier family 35 member E1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.59× (z +8.4, q 3e-14, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.485× (z -18.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKRIP1]] (+0.84, fdr 7e-06), [[HM13]] (+0.78, fdr 7e-06), [[QPCTL]] (+0.77, fdr 7e-06); moves opposite to [[HNRNPH3]] (-0.62, fdr 1e-05), [[ZNF280D]] (-0.61, fdr 1e-05), [[U2SURP]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +8.4 | 3e-14 | 37/48 (NCI-H2030, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +6.0 | 4e-07 | 38/49 (HS-578T, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.7 | 6e-04 | 26/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.59×** | +4.4 | 0.002 | 36/48 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.009 | 22/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.047 | 7/48 (SW 900, LS 180, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.069 | 18/48 (LoVo, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.069 | 7/49 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.485×** | -18.3 | 0e+00 | 47/48 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.394×** | -16.1 | 0e+00 | 39/44 (HCT15, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.395×** | -16.0 | 0e+00 | 48/48 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.470×** | -13.6 | 9e-40 | 44/48 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.475×** | -13.4 | 1e-38 | 40/49 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -8.5 | 1e-15 | 35/47 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.644×** | -7.3 | 2e-11 | 31/45 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.753×** | -7.2 | 5e-11 | 36/48 (C32, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.703×** | -6.1 | 7e-08 | 33/48 (C32, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.755×** | -5.0 | 3e-05 | 28/48 (A-427, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -4.6 | 2e-04 | 19/48 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.5 | 4e-04 | 21/48 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -3.9 | 0.004 | 26/48 (C32, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.810×** | -3.8 | 0.007 | 27/48 (hTERT-HPNE, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.808×** | -3.7 | 0.009 | 21/47 (HCT15, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.825×** | -3.4 | 0.020 | 24/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.845× | -3.0 | 0.090 | 19/48 (Hs 766T, A549, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.847× | -3.0 | 0.091 | 14/48 (AsPC-1, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -3.0 | 0.091 | 16/48 (A498, SW 900, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 149 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -13.8) |
| [[HS-578T (line)]] | alt | 119 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -18.6) |
| [[C32 (line)]] | wt | 119 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -22.0) |
| [[A-172 (line)]] | wt | 104 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -13.6) |
| [[A-427 (line)]] | wt | 66.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -17.5) |
| [[SNU-1 (line)]] | wt | 88.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -14.6) |
| [[SW 900 (line)]] | alt | 101 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.225× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -17.7) |
| [[C-33 A (line)]] | alt | 86.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.6) |
| [[H4 (line)]] | wt | 168 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -14.5) |
| [[HOP62 (line)]] | alt | 89.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -11.6) |
| [[J82 (line)]] | alt | 77.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 73.1 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.00× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.421× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 59.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -14.1) |
| [[RKO (line)]] | wt | 62.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.226× (z -11.8) |
| [[A549 (line)]] | wt | 58.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.251× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 95.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 71.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.425× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 58.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.265× (z -12.3) |
| [[SHP-77 (line)]] | alt | 91.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -12.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.7) |
| [[SW48 (line)]] | wt | 72.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.236× (z -10.8) |
| [[SW480 (line)]] | alt | 60.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.586× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 94.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -8.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 90.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -13.1) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -8.6) |
| [[HCT15 (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0467× (z -23.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 68.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.363× (z -9.5) |
| [[LS 180 (line)]] | wt | 48.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0815× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.302× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 65.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 106 | 1 | 1 | [[Auranofin (drug)]] 5 µM 1.98× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -11.2) |
| [[PANC-1 (line)]] | alt | 60.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.286× (z -13.3) |
| [[SW1417 (line)]] | alt | 55.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -15.2) |
| [[AN3 CA (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -13.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.1) |
| [[COLO 205 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -13.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 60.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.285× (z -10.6) |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.146× (z -10.1) |
| [[SNU-423 (line)]] | alt | 85.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKRIP1]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 |  |
| [[HM13]] | +0.78 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[POM121]] | +0.77 | +0.85 / +0.72 | both halves | 7e-06 |  |
| [[P4HB]] | +0.76 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[TBC1D20]] | +0.74 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[TMED9]] | +0.73 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[BET1L]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[POM121C]] | +0.71 | +0.83 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH3]] | -0.62 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.61 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[TIA1]] | -0.61 | -0.65 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRN1]] | B | NRN1 activity raises SLC35E1's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.12× lower at baseline in the lines without NRN1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (6.9, -20.3); signed map (-44.2, 12.2). **Vector** length 145, 47.9% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.9 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.5 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.2 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.2 | +2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.9 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.3 | -18.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.9 | -16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -13.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.8 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.5 | -8.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.5 | -6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member E1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,549,831-16,572,415 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14251 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96K37](https://www.uniprot.org/uniprotkb/Q96K37) (Solute carrier family 35 member E1):

> Putative transporter.

**Summary**, from NCBI Gene [79939](https://www.ncbi.nlm.nih.gov/gene/79939):

> Predicted to enable antiporter activity. Predicted to be involved in transmembrane transport. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20803) · Entrez [79939](https://www.ncbi.nlm.nih.gov/gene/79939) · UniProt [Q96K37](https://www.uniprot.org/uniprotkb/Q96K37) · Ensembl [ENSG00000127526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127526)

## Data

Gene col 4817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4817); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4817]; `tensor/DDL_lfc|DDL_z.npy` [4817]; `embed/gene_vectors.npy` [4817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4817 or target_col == 4817). Every well: [[SLC35E1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35E1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
