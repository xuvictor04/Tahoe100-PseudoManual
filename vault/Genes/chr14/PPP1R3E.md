---
symbol: "PPP1R3E"
type: "gene"
col: 14005
ensembl_id: "ENSG00000235194"
name: "protein phosphatase 1 regulatory subunit 3E"
location: "14q11.2"
module: 46
arm: "+"
pooled_cpm: 13.13
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 30
n_dd_up_clean: 15
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PPP1R3E

*protein phosphatase 1 regulatory subunit 3E* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.85× (z +8.1, q 3e-13, up in 22 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.64× (z +7.1, q 3e-10, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.436× (z -11.7, q 5e-29, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.543× (z -8.6, q 1e-15, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMXL1-DT]] (+0.64, fdr 1e-05), [[MCCC1]] (+0.64, fdr 1e-05), [[HCG27]] (+0.62, fdr 1e-05); moves opposite to [[MICAL2]] (-0.62, fdr 1e-05), [[POLR3B]] (-0.56, fdr 3e-05), [[ELOVL1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +8.1 | 3e-13 | 22/32 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +7.1 | 3e-10 | 25/47 (A-427, RKO, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +5.1 | 5e-05 | 18/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.1 | 5e-05 | 16/38 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +4.9 | 1e-04 | 16/46 (KATO III, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.33×** | +4.4 | 0.001 | 13/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.003 | 15/46 (hTERT-HPNE, SW 900, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.003 | 13/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.008 | 7/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.020 | 12/47 (LoVo, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.4 | 0.031 | 10/48 (A549, HT-29, …) | top dose only | low cells (technical?) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.18× | +3.4 | 0.031 | 8/48 (KATO III, SW480, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.043 | 9/47 (C-33 A, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.043 | 11/44 (A549, SW 900, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.043 | 7/47 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.063 | 2/48 (SW480, MIA PaCa-2) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.084 | 4/46 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.084 | 7/47 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.089 | 5/47 (SNU-423, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.436×** | -11.7 | 5e-29 | 34/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.490×** | -10.1 | 2e-21 | 36/47 (C-33 A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.498×** | -9.8 | 1e-20 | 31/47 (NCI-H460, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -8.6 | 1e-15 | 29/45 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.319×** | -8.5 | 3e-15 | 35/44 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.679×** | -7.7 | 1e-12 | 26/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -6.4 | 1e-08 | 23/46 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.647×** | -6.1 | 7e-08 | 25/46 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.670×** | -5.6 | 1e-06 | 20/47 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -5.5 | 2e-06 | 21/44 (HEC-1-A, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.684×** | -5.3 | 5e-06 | 21/47 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -5.1 | 1e-05 | 21/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.694×** | -4.9 | 4e-05 | 20/46 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.698×** | -4.8 | 5e-05 | 18/40 (SNU-1, SK-MEL-2, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.731×** | -4.4 | 4e-04 | 16/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.764×** | -3.8 | 0.005 | 14/44 (SW48, Panc 03.27, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.836× | -3.5 | 0.012 | 15/48 (SK-MEL-2, CFPAC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.016 | 10/47 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.030 | 13/44 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.728×** | -3.2 | 0.035 | 3/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.045 | 12/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.805×** | -3.0 | 0.054 | 11/47 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat |  |
| [[Fluvoxamine (maleate) (drug)]] 0.05 µM |  | **0.810×** | -2.9 | 0.069 | 10/46 (SNU-1, NCI-H2347, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.674×** | -2.9 | 0.074 | 9/43 (NCI-H460, SNU-423, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.813×** | -2.9 | 0.074 | 18/46 (SK-MEL-2, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 22.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -11.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -8.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0353× (z -17.5) ⚠ cell-cycle shift, explains ~96% of this change |
| [[Panc 03.27 (line)]] | alt | 9.68 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.125× (z -9.6) |
| [[A-172 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMXL1-DT]] | +0.64 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MCCC1]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[HCG27]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CFAP43]] | +0.62 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LINC00938]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[ZBTB25]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PNISR]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[BCL2L2-PABPN1]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 | ⚠ same locus (4.0 kb: neighbours can correlate without regulation) |
| [[GARS1-DT]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[HEXA]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DYNLT2]] | +0.58 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[PNISR-AS1]] | +0.57 | +0.59 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICAL2]] | -0.62 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[POLR3B]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ELOVL1]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[NAPG]] | -0.52 | -0.50 / -0.23 | both halves | 5e-04 |  |
| [[HYAL2]] | -0.51 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[PWP2]] | -0.50 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[RGS19]] | -0.50 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[EHD4]] | -0.50 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[GBA2]] | -0.50 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[GNB1L]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[SPTLC2]] | -0.50 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[LYAR]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PPP1R3E's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.1, 24.1); signed map (-1.0, -4.5). **Vector** length 83.2, 16.6% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.7 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +2.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.1 | -10.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.9 | -11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.2 | -9.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -8.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 3E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,295,652-23,302,859 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00089 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7J1](https://www.uniprot.org/uniprotkb/Q9H7J1) (Protein phosphatase 1 regulatory subunit 3E):

> Acts as a glycogen-targeting subunit for PP1. PP1 is involved in glycogen metabolism and contributes to the activation of glycogen synthase leading to an increase in glycogen synthesis.

**Summary**, from NCBI Gene [90673](https://www.ncbi.nlm.nih.gov/gene/90673):

> Predicted to enable [phosphorylase] phosphatase activity; glycogen binding activity; and protein phosphatase 1 binding activity. Predicted to be involved in positive regulation of glycogen biosynthetic process. Predicted to be located in glycogen granule. Predicted to be part of protein phosphatase type 1 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14943) · Entrez [90673](https://www.ncbi.nlm.nih.gov/gene/90673) · UniProt [Q9H7J1](https://www.uniprot.org/uniprotkb/Q9H7J1) · Ensembl [ENSG00000235194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235194)

## Data

Gene col 14005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14005); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14005]; `tensor/DDL_lfc|DDL_z.npy` [14005]; `embed/gene_vectors.npy` [14005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14005 or target_col == 14005). Every well: [[PPP1R3E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R3E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
