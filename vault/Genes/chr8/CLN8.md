---
symbol: "CLN8"
type: "gene"
col: 11280
ensembl_id: "ENSG00000182372"
name: "CLN8 transmembrane ER and ERGIC protein"
location: "8p23.3"
module: 2
arm: "+"
pooled_cpm: 25.94
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CLN8

*CLN8 transmembrane ER and ERGIC protein* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.83× (z +18.4, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.566× (z -5.3, q 6e-05, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEA15]] (+0.57, fdr 4e-05), [[CRYM]] (+0.55, fdr 1e-05), [[RPLP0P2]] (+0.55, fdr 1e-05); moves opposite to [[WBP11]] (-0.56, fdr 2e-05), [[ARMC8]] (-0.55, fdr 3e-05), [[YAP1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRKCZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +18.4 | 0e+00 | 42/46 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.14×** | +12.7 | 2e-34 | 41/47 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +9.9 | 8e-21 | 36/47 (SHP-77, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +9.8 | 1e-20 | 37/46 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +9.8 | 1e-20 | 31/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +9.4 | 5e-19 | 29/46 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.7 | 1e-12 | 27/45 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +7.4 | 1e-11 | 29/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +6.2 | 3e-08 | 23/45 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +6.2 | 4e-08 | 29/47 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.0 | 1e-07 | 15/33 (HOP62, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +5.9 | 1e-07 | 26/46 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +5.5 | 2e-06 | 18/37 (SW 900, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 8e-06 | 22/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 7e-05 | 21/46 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.6 | 2e-04 | 18/47 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 19/47 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.010 | 16/46 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.012 | 15/45 (NCI-H1573, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.566×** | -5.3 | 6e-05 | 20/45 (KATO III, HS-578T, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.576×** | -5.1 | 8e-05 | 19/44 (LOX-IMVI, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.849× | -4.2 | 0.005 | 16/47 (LoVo, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.790×** | -4.1 | 0.006 | 20/47 (BT-474, COLO 205, …) | top dose only |  |
| [[AZD-7648 (drug)]] 5 µM |  | **0.672×** | -3.7 | 0.023 | 13/44 (C32, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.065 | 14/46 (A498, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.068 | 15/46 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.12 | 10/47 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.842× | -3.1 | 0.12 | 6/47 (RKO, SW1417, …) | top dose only | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.14 | 14/46 (A549, NCI-H460, …) | all doses, flat |  |
| [[Flutamide (drug)]] 5 µM |  | 0.847× | -3.0 | 0.14 | 10/46 (C32, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 62.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 22.7 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.48× (z +9.8) | — |
| [[A-427 (line)]] | wt | 24.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 62.5 | 2 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.08× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 22.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.51× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 5.02× (z +10.3) | — |
| [[SW480 (line)]] | alt | 18.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.42× (z +13.3) | — |
| [[A498 (line)]] | wt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.2) | — |
| [[A549 (line)]] | wt | 50.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.9) |
| [[BT-474 (line)]] | alt | 33.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 12.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.45× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 29.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.37× (z +13.5) | — |
| [[HepG2_C3A (line)]] | wt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 12.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.99× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 38.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.92× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 42.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.148× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0918× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 19.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.02× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.15× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 34.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.99× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 20.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.72× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEA15]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[CRYM]] | +0.55 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.55 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CPNE2]] | +0.53 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DDA1]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[TM4SF19-DYNLT2B]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[MAFK]] | +0.51 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[LINC02154]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[PRKCZ]] | +0.51 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[RABGEF1P3]] | +0.51 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ZNF83]] | +0.51 | +0.37 / +0.55 | both halves | 7e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP11]] | -0.56 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[ARMC8]] | -0.55 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[YAP1]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CAND1]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[DUT]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FBXO5]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[USP1]] | -0.49 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[ACTL6A]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[KCTD3]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[RAD21]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[HIRIP3]] | -0.48 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[MAP3K1]] | -0.47 | -0.31 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCZ]] | B | PRKCZ activity lowers CLN8's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 1.73× higher at baseline in the lines without PRKCZ | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C; its own permutation p |
| [[RPLP0P2]] | B | RPLP0P2 activity raises CLN8's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without RPLP0P2 | 0.064 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[ACVR1C]] | C | ACVR1C activity strengthens CLN8's drug response | lines that do not express ACVR1C (4) vs lines expressing it (43) | the lines without ACVR1C respond 0.28× as strongly (z diff +2.87); strongest at Homoharringtonine 5 µM: 0.81x vs 1.48x (z diff +6.4) | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CORIN, HDAC2-AS2, ENSG00000249951; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.324). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (19.0, -5.5); signed map (-5.8, 25.5). **Vector** length 96.6, 21.4% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.7 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +12.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +9.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +3.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -5.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.1 |
|  | [[NG25 (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | CLN8 transmembrane ER and ERGIC protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.3 — chr8:1,755,778-1,801,711 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39417, TLCD6; previously EPMR, C8orf61 |
| Gene groups (HGNC) | TLC domain containing |
| Hallmark sets | PEROXISOME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBY8](https://www.uniprot.org/uniprotkb/Q9UBY8) (Protein CLN8):

> Could play a role in cell proliferation during neuronal differentiation and in protection against cell death.

**Summary**, from NCBI Gene [2055](https://www.ncbi.nlm.nih.gov/gene/2055):

> This gene encodes a transmembrane protein belonging to a family of proteins containing TLC domains, which are postulated to function in lipid synthesis, transport, or sensing. The protein localizes to the endoplasmic reticulum (ER), and may recycle between the ER and ER-Golgi intermediate compartment. Mutations in this gene are associated with a disorder characterized by progressive epilepsy with cognitive disabilities (EPMR), which is a subtype of neuronal ceroid lipofuscinoses (NCL). Patients …

**Accessions** — [HGNC:2079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2079) · Entrez [2055](https://www.ncbi.nlm.nih.gov/gene/2055) · UniProt [Q9UBY8](https://www.uniprot.org/uniprotkb/Q9UBY8) · Ensembl [ENSG00000182372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182372)

## Data

Gene col 11280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11280); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11280]; `tensor/DDL_lfc|DDL_z.npy` [11280]; `embed/gene_vectors.npy` [11280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11280 or target_col == 11280). Every well: [[CLN8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLN8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
