---
symbol: "SYTL4"
type: "gene"
col: 2242
ensembl_id: "ENSG00000102362"
name: "synaptotagmin like 4"
location: "Xq22.1"
module: 6
arm: "+"
pooled_cpm: 14.75
n_lines_expressing: 40
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SYTL4

*synaptotagmin like 4* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +15.7, q 0e+00, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.435× (z -21.5, q 0e+00, down in 31 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTMR8]] (+0.61, fdr 1e-05), [[ZDHHC13]] (+0.60, fdr 1e-05), [[TBC1D1]] (+0.60, fdr 7e-06); moves opposite to [[BOLA1]] (-0.52, fdr 6e-05), [[ZNF597]] (-0.50, fdr 9e-05), [[CLBA1]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LYPD6]] → it (grade B ⚠); 11 go from it, the strongest it → [[GALNT12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +15.7 | 0e+00 | 32/37 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +12.1 | 5e-31 | 28/36 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +9.7 | 6e-20 | 8/38 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.9 | 8e-17 | 10/18 (LS 180, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +8.8 | 1e-16 | 24/37 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +8.6 | 9e-16 | 10/23 (NCI-H2030, SW1417, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.9 | 2e-13 | 13/25 (NCI-H2030, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 2e-04 | 10/36 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 4/37 (KATO III, Panc 03.27, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 10/37 (AsPC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.003 | 5/36 (HEC-1-A, RKO, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.24×** | +3.9 | 0.005 | 8/37 (SW480, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.005 | 10/37 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.55×** | +3.8 | 0.005 | 8/28 (SW480, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.005 | 11/36 (NCI-H2347, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.029 | 1/36 (SW1417) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.031 | 6/36 (AsPC-1, HT-29, …) | two highest doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.032 | 7/37 (RKO, KATO III, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.065 | 9/36 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Tadalafil (drug)]] 5 µM |  | 1.18× | +3.0 | 0.072 | 4/37 (A-172, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2242.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.435×** | -21.5 | 0e+00 | 31/36 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.463×** | -14.1 | 2e-42 | 25/34 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.597×** | -9.4 | 9e-19 | 24/37 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -7.7 | 2e-12 | 20/36 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.657×** | -7.7 | 2e-12 | 20/37 (C-33 A, HT-29, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -6.6 | 5e-09 | 18/35 (AsPC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.703×** | -6.4 | 9e-09 | 20/37 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -5.4 | 4e-06 | 14/34 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.735×** | -5.4 | 4e-06 | 15/36 (SK-MEL-2, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.747×** | -5.3 | 6e-06 | 15/37 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.769×** | -4.8 | 7e-05 | 14/37 (NCI-H1792, LS 180, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.581×** | -4.8 | 8e-05 | 12/33 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.776×** | -4.6 | 1e-04 | 17/36 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -4.6 | 2e-04 | 13/37 (SW1417, SK-MEL-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -4.5 | 3e-04 | 20/34 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.015 | 8/35 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.690×** | -3.3 | 0.033 | 7/35 (J82, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **0.786×** | -3.1 | 0.050 | 2/38 (SW480, HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Pemetrexed (drug)]] 5 µM |  | 0.839× | -3.1 | 0.052 | 4/35 (A498, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.844× | -3.1 | 0.052 | 6/37 (SNU-423, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 60.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -22.8) |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0701× (z -29.2) |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0429× (z -11.9) |
| [[LoVo (line)]] | wt | 14.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0913× (z -16.5) |
| [[LS 180 (line)]] | wt | 27.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -12.0) |
| [[SW480 (line)]] | alt | 13.8 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.56× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 6.26 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -15.3) |
| [[Hs 766T (line)]] | wt | 33.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.2) |
| [[A549 (line)]] | wt | 7.15 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0771× (z -11.4) |
| [[BT-474 (line)]] | alt | 7.57 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0723× (z -9.4) |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.1) |
| [[HOP62 (line)]] | alt | 10.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.4) |
| [[KATO III (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0683× (z -21.6) |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 5.92 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.79× (z +9.3) | — |
| [[RKO (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0720× (z -13.9) |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.1) |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -9.8) |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0874× (z -8.7) |
| [[A-172 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR8]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ZDHHC13]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TBC1D1]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[LYPD6]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[HAUS1]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[HPSE]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[PRSS12]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SOAT1]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[EMP2]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PARP1]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TMEM106C]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SNX7]] | +0.54 | +0.56 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BOLA1]] | -0.52 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ZNF597]] | -0.50 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[CLBA1]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[PDCD7]] | -0.50 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[EP300]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ZNF432]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[RECQL5]] | -0.47 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[LINS1]] | -0.47 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[USE1]] | -0.47 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[UBAP1L]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[CDKL3]] | -0.46 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[ZNF561]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD6]] | B | LYPD6 activity raises SYTL4's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without LYPD6 | 0.053 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[GALNT12]] | B | GALNT12 activity raises SYTL4's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.86× lower at baseline in the lines without GALNT12 | 0.072 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[ATP8A1]] | B | ATP8A1 activity raises SYTL4's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 2.49× lower at baseline in the lines without ATP8A1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT12]] | B | SYTL4 activity raises GALNT12's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without SYTL4 | 0.029 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[CCDC150]] | B | SYTL4 activity lowers CCDC150's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.34× higher at baseline in the lines without SYTL4 | 0.033 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[BLMH]] | B | SYTL4 activity lowers BLMH's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.69× higher at baseline in the lines without SYTL4 | 0.041 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[ADGRB2]] | B | SYTL4 activity lowers ADGRB2's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.43× higher at baseline in the lines without SYTL4 | 0.044 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[EPB41L4A]] | B | SYTL4 activity raises EPB41L4A's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 3.19× lower at baseline in the lines without SYTL4 | 0.051 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[DSCC1]] | B | SYTL4 activity lowers DSCC1's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.26× higher at baseline in the lines without SYTL4 | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[ASRGL1]] | B | SYTL4 activity lowers ASRGL1's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.46× higher at baseline in the lines without SYTL4 | 0.055 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[TSPAN14]] | B | SYTL4 activity raises TSPAN14's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without SYTL4 | 0.060 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[NSMCE4A]] | B | SYTL4 activity lowers NSMCE4A's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.19× higher at baseline in the lines without SYTL4 | 0.061 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[PLPP2]] | B | SYTL4 activity raises PLPP2's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without SYTL4 | 0.083 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[PRSS12]] | B | SYTL4 activity raises PRSS12's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 2.79× lower at baseline in the lines without SYTL4 | 0.099 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-2.4, 37.0); signed map (-2.4, 16.1). **Vector** length 78.2, 16.5% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | -0.1 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.5 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -14.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -21.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.7 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:100,671,783-100,732,123 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Slp4 |
| Gene groups (HGNC) | Synaptotagmin like tandem C2 proteins |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C24](https://www.uniprot.org/uniprotkb/Q96C24) (Synaptotagmin-like protein 4):

> Modulates exocytosis of dense-core granules and secretion of hormones in the pancreas and the pituitary. Interacts with vesicles containing negatively charged phospholipids in a Ca(2+)-independent manner (By similarity).

**Summary**, from NCBI Gene [94121](https://www.ncbi.nlm.nih.gov/gene/94121):

> This gene encodes a member of the synaptotagmin like protein family. Members of this family are characterized by an N-terminal Rab27 binding domain and C-terminal tandem C2 domains. The encoded protein binds specific small Rab GTPases and is involved in intracellular membrane trafficking. This protein binds Rab27 and may be involved in inhibiting dense core vesicle exocytosis. Alternate splicing results in multiple transcript variants that encode the same protein. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:15588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15588) · Entrez [94121](https://www.ncbi.nlm.nih.gov/gene/94121) · UniProt [Q96C24](https://www.uniprot.org/uniprotkb/Q96C24) · Ensembl [ENSG00000102362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102362)

## Data

Gene col 2242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2242); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2242]; `tensor/DDL_lfc|DDL_z.npy` [2242]; `embed/gene_vectors.npy` [2242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2242 or target_col == 2242). Every well: [[SYTL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYTL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
