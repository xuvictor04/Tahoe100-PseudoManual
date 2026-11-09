---
symbol: "C7orf31"
type: "gene"
col: 7738
ensembl_id: "ENSG00000153790"
name: "sperm microtubule inner protein 4"
location: "7p15.3"
module: 35
arm: "+"
pooled_cpm: 5.86
n_lines_expressing: 43
n_dd_up: 25
n_dd_down: 14
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# C7orf31

*sperm microtubule inner protein 4* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +12.1, q 9e-31, up in 21 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.394× (z -11.1, q 2e-26, down in 28 of 40 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.420× (z -10.4, q 7e-23, down in 29 of 40 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAXIP1-AS2]] (+0.70, fdr 1e-05), [[PIGV]] (+0.70, fdr 1e-04), [[CCDC102A]] (+0.69, fdr 1e-05); moves opposite to [[GNB1L]] (-0.60, fdr 3e-05), [[SCART1]] (-0.59, fdr 3e-05), [[NHP2]] (-0.59, fdr 3e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[DPY19L2]] → it (grade B ⚠); 3 go from it, the strongest it → [[TRAM2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +12.1 | 9e-31 | 21/36 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.95×** | +11.4 | 2e-27 | 26/39 (Panc 03.27, A-172, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +9.3 | 4e-18 | 25/38 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +8.9 | 1e-16 | 21/39 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.34×** | +4.9 | 1e-04 | 12/40 (SW480, SNU-423, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.49×** | +4.8 | 1e-04 | 11/37 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.5 | 5e-04 | 3/10 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.003 | 9/39 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.005 | 8/40 (LoVo, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.005 | 13/33 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.37×** | +3.6 | 0.015 | 7/40 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.020 | 8/38 (SW480, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.021 | 10/38 (SW480, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.021 | 5/40 (LoVo, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.021 | 5/40 (SW480, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.021 | 9/38 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.021 | 4/37 (MIA PaCa-2, C32, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.032 | 6/38 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.040 | 10/36 (A498, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7738.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.394×** | -11.1 | 2e-26 | 28/40 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.394×** | -11.1 | 2e-26 | 26/33 (SNU-423, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.420×** | -10.4 | 7e-23 | 29/40 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.462×** | -9.2 | 4e-18 | 24/39 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.508×** | -7.8 | 7e-13 | 22/32 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.540×** | -7.4 | 1e-11 | 19/40 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.592×** | -6.3 | 3e-08 | 19/40 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.638×** | -5.4 | 6e-06 | 16/40 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.487×** | -4.5 | 4e-04 | 11/38 (A498, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.510×** | -4.2 | 0.001 | 16/34 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.746×** | -3.5 | 0.023 | 8/40 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.747×** | -3.5 | 0.023 | 13/39 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.757×** | -3.3 | 0.038 | 16/40 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.765×** | -3.2 | 0.056 | 8/39 (CFPAC-1, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.92 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +15.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.202× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 9.63 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.139× (z -9.6) |
| [[A-172 (line)]] | wt | 7.72 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +14.1) | [[Digitoxin (drug)]] 0.05 µM 0.125× (z -9.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 7.47 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.138× (z -11.5) |
| [[A-427 (line)]] | wt | 9.04 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0837× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.61 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0613× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0725× (z -8.7) |
| [[A498 (line)]] | wt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +8.9) | — |
| [[A549 (line)]] | wt | 6.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 5.84 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0696× (z -8.5) |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0829× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 4.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 3.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +10.4) | — |
| [[J82 (line)]] | alt | 4.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 5.11 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0731× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 9.06 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.132× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 3.30 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0986× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 4.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.167× (z -8.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.122× (z -10.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 7.63 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0846× (z -8.8) |
| [[SNU-423 (line)]] | alt | 9.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAXIP1-AS2]] | +0.70 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[PIGV]] | +0.70 | +0.73 / +0.36 | both halves | 1e-04 |  |
| [[CCDC102A]] | +0.69 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[BTN2A3P-1]] | +0.67 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[TCEAL1]] | +0.64 | +0.64 / +0.38 | both halves | 6e-05 |  |
| [[BTN2A3P]] | +0.64 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[MAGI2-AS3]] | +0.64 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[ATF5]] | +0.63 | +0.61 / +0.33 | both halves | 1e-04 |  |
| [[PHYH]] | +0.63 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[PLS3-AS1]] | +0.63 | +0.69 / +0.29 | both halves | 2e-04 |  |
| [[ZXDA]] | +0.63 | +0.59 / +0.28 | both halves | 3e-04 |  |
| [[C1QTNF1-AS1]] | +0.62 | +0.52 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB1L]] | -0.60 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SCART1]] | -0.59 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[NHP2]] | -0.59 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[NPHP4]] | -0.57 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[TREX2]] | -0.56 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[LSM4]] | -0.55 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2]] | B | DPY19L2 activity raises C7orf31's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without DPY19L2 | 0.007 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[ANKRD18B]] | B | ANKRD18B activity raises C7orf31's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.59× lower at baseline in the lines without ANKRD18B | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises C7orf31's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without SYT9-AS1 | 0.018 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CNN3-DT]] | B | CNN3-DT activity raises C7orf31's level | lines that do not express CNN3-DT (8) vs lines expressing it (42) | 2.30× lower at baseline in the lines without CNN3-DT | 0.047 | ⚠ within organs, on part of the lines; also absent: MPP2, CNN3, SLC35F1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers C7orf31's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[TBKBP1]] | C | TBKBP1 activity raises C7orf31's level | lines that do not express TBKBP1 (5) vs lines expressing it (45) | 3.42× lower at baseline in the lines without TBKBP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSRP2, PHC1, DNAJC18; co-absent with the target; its own permutation p |
| [[BTN2A2]] | C | BTN2A2 activity raises C7orf31's level | lines that do not express BTN2A2 (3) vs lines expressing it (47) | 3.89× lower at baseline in the lines without BTN2A2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC18, TBKBP1, TTC23L; its own permutation p |
| [[ZDHHC1]] | C | ZDHHC1 activity raises C7orf31's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 2.57× lower at baseline in the lines without ZDHHC1 | 0.087 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAM2-AS1]] | B | C7orf31 activity raises TRAM2-AS1's level | lines that do not express C7orf31 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without C7orf31 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC00888, TMEM145, TBKBP1; maybe low, not absent |
| [[ZC2HC1C]] | B | C7orf31 activity raises ZC2HC1C's level | lines that do not express C7orf31 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without C7orf31 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC00888, TMEM145, TBKBP1; maybe low, not absent |
| [[BTN2A2]] | B | C7orf31 activity raises BTN2A2's level | lines that do not express C7orf31 (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without C7orf31 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC00888, TMEM145, TBKBP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (14.8, 10.6); signed map (18.5, -13.2). **Vector** length 71.2, 12.7% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +9.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +8.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.2 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +4.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -10.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.5 | -7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -3.4 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.3 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.7 | -9.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sperm microtubule inner protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:25,134,692-25,180,356 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C7orf31 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N865](https://www.uniprot.org/uniprotkb/Q8N865) (Sperm-associated microtubule inner protein 4):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in flagellum axoneme. May serve to reinforce and thus stabilize the microtubule structure in the sperm flagella.

**Summary**, from NCBI Gene [136895](https://www.ncbi.nlm.nih.gov/gene/136895):

> Located in centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21722) · Entrez [136895](https://www.ncbi.nlm.nih.gov/gene/136895) · UniProt [Q8N865](https://www.uniprot.org/uniprotkb/Q8N865) · Ensembl [ENSG00000153790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153790)

## Data

Gene col 7738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7738); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7738]; `tensor/DDL_lfc|DDL_z.npy` [7738]; `embed/gene_vectors.npy` [7738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7738 or target_col == 7738). Every well: [[C7orf31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C7orf31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
