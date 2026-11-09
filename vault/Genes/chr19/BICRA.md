---
symbol: "BICRA"
type: "gene"
col: 720
ensembl_id: "ENSG00000063169"
name: "BRD4 interacting chromatin remodeling complex associated protein"
location: "19q13.33"
module: 36
arm: "+"
pooled_cpm: 44.01
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# BICRA

*BRD4 interacting chromatin remodeling complex associated protein* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 5.08× (z +11.3, q 5e-27, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.455× (z -11.3, q 5e-27, down in 39 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.623× (z -6.8, q 1e-09, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3R4]] (+0.58, fdr 1e-05), [[NCOA6]] (+0.58, fdr 1e-05), [[KPNA6]] (+0.58, fdr 3e-05); moves opposite to [[NOTCH2NLB]] (-0.51, fdr 3e-05), [[DYRK3]] (-0.49, fdr 3e-05), [[LINC02154]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C12orf50]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.08×** | +11.3 | 5e-27 | 42/49 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.07×** | +9.8 | 4e-20 | 45/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +4.8 | 4e-04 | 26/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.26× | +3.3 | 0.13 | 19/47 (KATO III, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.25 | 13/48 (SW 900, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.29× | +3.0 | 0.25 | 14/49 (SW 900, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.455×** | -11.3 | 5e-27 | 39/47 (LS 180, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.452×** | -10.6 | 1e-23 | 31/44 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.493×** | -9.5 | 5e-19 | 30/42 (LS 180, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.636×** | -9.2 | 5e-18 | 32/48 (C32, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -6.8 | 1e-09 | 32/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.642×** | -6.4 | 2e-08 | 29/48 (NCI-H1792, SW1417, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.667×** | -5.8 | 4e-07 | 32/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.722×** | -4.4 | 8e-04 | 24/47 (SW48, COLO 205, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.554×** | -4.1 | 0.002 | 26/48 (NCI-H2347, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.765×** | -3.9 | 0.006 | 21/48 (AsPC-1, NCI-H1792, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -3.4 | 0.035 | 19/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.794×** | -3.1 | 0.094 | 19/48 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.797×** | -3.1 | 0.098 | 20/49 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -3.0 | 0.100 | 16/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | 0.800× | -3.0 | 0.10 | 19/47 (SW 1271, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 57.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -19.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.333× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 47.0 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.93× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 58.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 44.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[KATO III (line)]] | alt | 41.4 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.03× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 40.3 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 7.86× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H2347 (line)]] | alt | 41.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 22.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -8.9) |
| [[A498 (line)]] | wt | 42.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -15.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -9.0) |
| [[A549 (line)]] | wt | 60.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -13.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 40.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 62.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 37.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LOX-IMVI (line)]] | wt | 50.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.10× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 39.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 16.5× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 52.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.312× (z -10.0) |
| [[COLO 205 (line)]] | alt | 39.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.5× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HCT15 (line)]] | alt | 51.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 42.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0755× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 48.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 42.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW 900 (line)]] | alt | 53.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 43.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.05× (z +10.6) | — |
| [[H4 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -14.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[J82 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -9.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 1 | — | [[Cytarabine (drug)]] 0.05 µM 0.0452× (z -8.7) |
| [[PANC-1 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 51.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW1417 (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3R4]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[NCOA6]] | +0.58 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[KPNA6]] | +0.58 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[EMC8]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[MLLT1]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZDHHC7]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[FAM222B]] | +0.54 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[PRCC]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[AMFR]] | +0.54 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[DCAF12]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZDHHC5]] | +0.53 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[CLASP1]] | +0.52 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLB]] | -0.51 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[DYRK3]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[LINC02154]] | -0.47 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[OR4F15]] | -0.47 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[CA8]] | -0.47 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[LINC00973]] | -0.47 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[ACVR1C]] | -0.47 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[AFF3]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[TRAF1]] | -0.46 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ENTHD1]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TENT5C]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[AHI1]] | -0.45 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | C12orf50 activity lowers BICRA's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 1.21× higher at baseline in the lines without C12orf50 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-12.8, -16.1); signed map (-41.5, -24.6). **Vector** length 96.2, 24.8% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +11.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.0 | +9.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.6 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +4.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.6 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | BRD4 interacting chromatin remodeling complex associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:47,608,196-47,703,277 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMARCK1; previously GLTSCR1 |
| Gene groups (HGNC) | GBAF complex subunits |
| Reactome | 4 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; SWI/SNF chromatin remodelers; ATP-dependent chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZM4](https://www.uniprot.org/uniprotkb/Q9NZM4) (BRD4-interacting chromatin-remodeling complex-associated protein):

> Component of SWI/SNF chromatin remodeling subcomplex GBAF that carries out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. May play a role in BRD4-mediated gene transcription.

**Summary**, from NCBI Gene [29998](https://www.ncbi.nlm.nih.gov/gene/29998):

> Enables transcription regulator activator activity. Involved in positive regulation of DNA-templated transcription. Located in nucleus. Part of SWI/SNF complex. Implicated in Coffin-Siris syndrome 12. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4332) · Entrez [29998](https://www.ncbi.nlm.nih.gov/gene/29998) · UniProt [Q9NZM4](https://www.uniprot.org/uniprotkb/Q9NZM4) · Ensembl [ENSG00000063169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063169)

## Data

Gene col 720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 720); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 720]; `tensor/DDL_lfc|DDL_z.npy` [720]; `embed/gene_vectors.npy` [720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 720 or target_col == 720). Every well: [[BICRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BICRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
