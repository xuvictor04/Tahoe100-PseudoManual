---
symbol: "SIDT1"
type: "gene"
col: 1036
ensembl_id: "ENSG00000072858"
name: "SID1 transmembrane family member 1"
location: "3q13.2"
module: 8
arm: "+"
pooled_cpm: 15.31
n_lines_expressing: 18
n_dd_up: 17
n_dd_down: 28
n_dd_up_clean: 14
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 64
direction_downstream: 100
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SIDT1

*SID1 transmembrane family member 1* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.38× (z +13.4, q 4e-38, up in 1 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.70× (z +5.9, q 6e-07, up in 13 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.371× (z -11.3, q 1e-26, down in 15 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TC2N]] (+0.75, fdr 7e-06), [[PRR15L]] (+0.73, fdr 7e-06), [[CATSPERB]] (+0.71, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 64 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 100 go from it, the strongest it → [[PROM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +13.4 | 4e-38 | 1/13 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +9.2 | 1e-17 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.1 | 1e-13 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +5.9 | 6e-07 | 13/16 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.56×** | +5.4 | 1e-05 | 12/16 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.0 | 6e-05 | 1/16 (J82) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +4.6 | 3e-04 | 10/16 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 4e-04 | 13/16 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 5e-04 | 11/16 (NCI-H1573, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.002 | 12/16 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.002 | 3/16 (J82, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.003 | 12/16 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.005 | 4/16 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.005 | 11/16 (CFPAC-1, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.099 | 6/16 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.099 | 0/16 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.099 | 1/16 (NCI-H1573) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.371×** | -11.3 | 1e-26 | 15/16 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.410×** | -10.1 | 1e-21 | 16/16 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.526×** | -7.3 | 7e-11 | 14/16 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.664×** | -6.5 | 9e-09 | 16/16 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -6.0 | 3e-07 | 16/16 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.625×** | -5.3 | 1e-05 | 14/16 (LS 180, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.721×** | -5.2 | 2e-05 | 15/16 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.639×** | -5.1 | 3e-05 | 12/16 (HT-29, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.629×** | -5.0 | 3e-05 | 9/16 (BT-474, LS 180, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.636×** | -4.9 | 5e-05 | 10/16 (SNU-423, A498, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.651×** | -4.8 | 7e-05 | 12/16 (HT-29, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.662×** | -4.7 | 2e-04 | 7/16 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.658×** | -4.5 | 2e-04 | 13/16 (COLO 205, A549, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -4.5 | 2e-04 | 13/16 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.673×** | -4.3 | 7e-04 | 9/16 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.686×** | -4.2 | 8e-04 | 10/16 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.680×** | -4.2 | 1e-03 | 4/16 (A498, COLO 205, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.002 | 8/16 (NCI-H1573, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.007 | 10/16 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.730×** | -3.5 | 0.011 | 15/16 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.745×** | -3.3 | 0.026 | 8/16 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 163 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -30.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -18.8) |
| [[LS 180 (line)]] | wt | 96.4 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0871× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -11.5) |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -14.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0870× (z -11.2) |
| [[KATO III (line)]] | alt | 25.8 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0622× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0840× (z -14.7) |
| [[BT-474 (line)]] | alt | 129 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 47.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0403× (z -25.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0652× (z -15.1) |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0827× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -10.4) |
| [[A549 (line)]] | wt | 12.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 7.24 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -10.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 5.92 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0934× (z -9.5) ⚠ cell-cycle shift, explains ~24% of this change |
| [[CFPAC-1 (line)]] | alt | 9.87 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0759× (z -9.1) |
| [[SNU-423 (line)]] | alt | 7.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0938× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0336× (z -14.0) |
| [[A-172 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TC2N]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[CATSPERB]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[PRR15]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[MUC5B]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | same gene group |
| [[UGT1A1]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SLC6A14]] | +0.67 | +0.60 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[MUC13]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[UGT1A6]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[POF1B]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 8, C 56. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity lowers SIDT1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 6.68× higher at baseline in the lines without BOLA3-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[PLEKHS1]] | B | PLEKHS1 activity raises SIDT1's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 2.37× lower at baseline in the lines without PLEKHS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers SIDT1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[SRMS]] | B | SRMS activity raises SIDT1's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without SRMS | 0.059 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[LGALS9]] | B | LGALS9 activity raises SIDT1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without LGALS9 | 0.061 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises SIDT1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without MTUS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[TLR3]] | B | TLR3 activity raises SIDT1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without TLR3 | 0.078 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[PBX1]] | B | PBX1 activity raises SIDT1's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without PBX1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[FAM3D]] | C | FAM3D activity raises SIDT1's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 7.97× lower at baseline in the lines without FAM3D | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises SIDT1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.70× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[GRHL2]] | C | GRHL2 activity raises SIDT1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 4.63× lower at baseline in the lines without GRHL2 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[CATSPERB]] | C | CATSPERB activity raises SIDT1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 4.09× lower at baseline in the lines without CATSPERB | 0.003 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14; co-absent with the target |

### Downstream of this gene

*100 arrows, 100 of them with an alert ⚠; grade A 0, B 29, C 71. Shown: the 12 strongest; 88 more arrows (88 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROM2]] | B | SIDT1 activity raises PROM2's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.74× lower at baseline in the lines without SIDT1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[BOLA3-DT]] | B | SIDT1 activity lowers BOLA3-DT's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.11× higher at baseline in the lines without SIDT1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[TMEM62]] | B | SIDT1 activity raises TMEM62's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.91× lower at baseline in the lines without SIDT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[LGALS9]] | B | SIDT1 activity raises LGALS9's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without SIDT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[MTUS1]] | B | SIDT1 activity raises MTUS1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 4.07× lower at baseline in the lines without SIDT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[C4orf19]] | B | SIDT1 activity raises C4orf19's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.93× lower at baseline in the lines without SIDT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[CARD14]] | B | SIDT1 activity raises CARD14's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without SIDT1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[PLCH1]] | B | SIDT1 activity raises PLCH1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.89× lower at baseline in the lines without SIDT1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[STS]] | B | SIDT1 activity raises STS's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.17× lower at baseline in the lines without SIDT1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[BAG1]] | B | SIDT1 activity raises BAG1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without SIDT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[NT5C2]] | B | SIDT1 activity strengthens NT5C2's drug response | lines that do not express SIDT1 (32) vs lines expressing it (17) | the lines without SIDT1 respond 0.57× as strongly (z diff +2.48); strongest at Panobinostat 5 µM: 0.81x vs 0.59x (z diff +3.8) | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2; target measured in part of the lines; artifact flags |
| [[SLC44A3-AS1]] | B | SIDT1 activity raises SLC44A3-AS1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.23× lower at baseline in the lines without SIDT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.4, 53.9); signed map (62.4, 4.2). **Vector** length 81.5, 31.7% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +5.4 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +1.7 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +4.6 |
| fall | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.4 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | SID1 transmembrane family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:113,532,555-113,629,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20174, SID-1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; SID1 transmembrane family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXL6](https://www.uniprot.org/uniprotkb/Q9NXL6) (SID1 transmembrane family member 1):

> In vitro binds long double-stranded RNA (dsRNA) (500 and 700 base pairs), but not dsRNA shorter than 300 bp. Not involved in RNA autophagy, a process in which RNA is directly imported into lysosomes in an ATP-dependent manner, and degraded.

**Summary**, from NCBI Gene [54847](https://www.ncbi.nlm.nih.gov/gene/54847):

> The protein encoded by this gene belongs to SID1 family of transmembrane dsRNA-gated channels. Family members transport dsRNA into cells and are required for systemic RNA interference. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:25967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25967) · Entrez [54847](https://www.ncbi.nlm.nih.gov/gene/54847) · UniProt [Q9NXL6](https://www.uniprot.org/uniprotkb/Q9NXL6) · Ensembl [ENSG00000072858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072858)

## Data

Gene col 1036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1036); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1036]; `tensor/DDL_lfc|DDL_z.npy` [1036]; `embed/gene_vectors.npy` [1036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1036 or target_col == 1036). Every well: [[SIDT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIDT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
