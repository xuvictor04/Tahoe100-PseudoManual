---
symbol: "IQANK1"
type: "gene"
col: 12770
ensembl_id: "ENSG00000203499"
name: "IQ motif and ankyrin repeat containing 1"
location: "8q24.3"
module: 31
arm: "+"
pooled_cpm: 13.02
n_lines_expressing: 32
n_dd_up: 9
n_dd_down: 29
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 60
direction_downstream: 47
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# IQANK1

*IQ motif and ankyrin repeat containing 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.67× (z +7.9, q 2e-12, up in 6 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +6.6, q 9e-09, up in 7 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.379× (z -14.8, q 0e+00, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPRSS4]] (+0.66, fdr 1e-05), [[ELMO3]] (+0.64, fdr 1e-05), [[GPR35]] (+0.64, fdr 1e-05); moves opposite to [[GLIS3]] (-0.49, fdr 5e-05), [[RARB]] (-0.49, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[SLC6A14]] → it (grade B ⚠); 47 go from it, the strongest it → [[CNRIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +7.9 | 2e-12 | 6/21 (A549, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.6 | 9e-09 | 7/27 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.8 | 4e-04 | 2/15 (KATO III, HT-29) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 1e-03 | 10/29 (NCI-H1573, A-427, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.011 | 6/29 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.032 | 6/30 (NCI-H1573, PANC-1, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.038 | 5/29 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.077 | 1/28 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.094 | 4/27 (LS 180, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.379×** | -14.8 | 0e+00 | 27/30 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.458×** | -11.9 | 3e-30 | 24/28 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.476×** | -10.9 | 2e-25 | 21/29 (LoVo, SW48, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.529×** | -9.0 | 3e-17 | 19/29 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.576×** | -8.4 | 4e-15 | 17/30 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.578×** | -8.4 | 6e-15 | 18/26 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.691×** | -8.0 | 1e-13 | 21/28 (LS 180, NCI-H1573, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -7.2 | 5e-11 | 17/29 (NCI-H1573, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.627×** | -6.6 | 3e-09 | 17/29 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.601×** | -6.5 | 5e-09 | 14/30 (LoVo, SW48, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.649×** | -6.1 | 5e-08 | 17/26 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -5.3 | 5e-06 | 16/30 (HCT15, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -5.2 | 9e-06 | 16/29 (NCI-H2030, BT-474, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.529×** | -5.1 | 1e-05 | 16/27 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.728×** | -4.8 | 5e-05 | 11/29 (SW48, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.739×** | -4.6 | 2e-04 | 14/28 (NCI-H1573, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -3.8 | 0.006 | 12/29 (RKO, HCT15, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.007 | 8/29 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.801×** | -3.4 | 0.019 | 4/29 (A549, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 78.2 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -17.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -16.9) |
| [[LoVo (line)]] | wt | 44.0 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -22.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -18.6) |
| [[NCI-H1573 (line)]] | alt | 71.8 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -23.1) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -17.3) |
| [[LS 180 (line)]] | wt | 41.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -27.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -17.8) |
| [[SW480 (line)]] | alt | 10.8 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -11.2) |
| [[HCT15 (line)]] | alt | 47.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -11.4) |
| [[SW1417 (line)]] | alt | 23.8 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.181× (z -10.5) |
| [[SW48 (line)]] | wt | 44.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -15.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -10.8) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.152× (z -10.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0951× (z -10.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 6.33 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0791× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -11.0) |
| [[HT-29 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -13.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H2030 (line)]] | alt | 5.45 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -8.5) |
| [[PANC-1 (line)]] | alt | 3.95 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.163× (z -8.5) |
| [[A-172 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS4]] | +0.66 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ELMO3]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[GPR35]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[EPHA1]] | +0.63 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MST1R]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[TMEM184A]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[CDH3]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[CAPN8]] | +0.61 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[TMEM45B]] | +0.61 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[TMC4]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TMC6]] | +0.60 | +0.58 / +0.59 | both halves | 8e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIS3]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[RARB]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 24, C 36. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC6A14]] | B | SLC6A14 activity raises IQANK1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.62× lower at baseline in the lines without SLC6A14 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[CEACAM6]] | B | CEACAM6 activity raises IQANK1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without CEACAM6 | 0.007 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[GSDMC]] | B | GSDMC activity raises IQANK1's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 3.15× lower at baseline in the lines without GSDMC | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[HS3ST1]] | B | HS3ST1 activity raises IQANK1's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without HS3ST1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[ONECUT3]] | B | ONECUT3 activity raises IQANK1's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 3.42× lower at baseline in the lines without ONECUT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[GALNT3]] | B | GALNT3 activity raises IQANK1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 3.92× lower at baseline in the lines without GALNT3 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[ZNF860]] | B | ZNF860 activity raises IQANK1's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.03× lower at baseline in the lines without ZNF860 | 0.022 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[ARHGEF5]], [[ARHGEF34P]] | B | ARHGEF5, ARHGEF34P activity raises IQANK1's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.19× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[PROM2]] | B | PROM2 activity raises IQANK1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without PROM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[B4GALNT3]] | B | B4GALNT3 activity raises IQANK1's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.73× lower at baseline in the lines without B4GALNT3 | 0.033 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[EPS8L1]] | B | EPS8L1 activity raises IQANK1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.14× lower at baseline in the lines without EPS8L1 | 0.052 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[CDH3]] | B | CDH3 activity strengthens IQANK1's drug response | lines that do not express CDH3 (10) vs lines expressing it (20) | the lines without CDH3 respond 0.73× as strongly (z diff +1.23); strongest at Homoharringtonine 5 µM: 0.55x vs 0.35x (z diff +3.7) | 0.054 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 19, C 28. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNRIP1]] | B | IQANK1 activity lowers CNRIP1's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 5.69× higher at baseline in the lines without IQANK1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[ZNF860]] | B | IQANK1 activity raises ZNF860's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without IQANK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[RARB]] | B | IQANK1 activity lowers RARB's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 4.51× higher at baseline in the lines without IQANK1 | 0.014 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[FAM83E]] | B | IQANK1 activity raises FAM83E's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.81× lower at baseline in the lines without IQANK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[TMC6]] | B | IQANK1 activity raises TMC6's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.95× lower at baseline in the lines without IQANK1 | 0.040 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[EPS8L1]] | B | IQANK1 activity raises EPS8L1's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.66× lower at baseline in the lines without IQANK1 | 0.041 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[KLHL2P1]] | B | IQANK1 activity raises KLHL2P1's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 1.53× lower at baseline in the lines without IQANK1 | 0.044 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[CEACAM1]] | B | IQANK1 activity raises CEACAM1's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.94× lower at baseline in the lines without IQANK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[ARHGEF5]] | B | IQANK1 activity raises ARHGEF5's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without IQANK1 | 0.047 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[PTK6]] | B | IQANK1 activity raises PTK6's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.70× lower at baseline in the lines without IQANK1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[GLIS3]] | B | IQANK1 activity lowers GLIS3's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 4.03× higher at baseline in the lines without IQANK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[ELMO3]] | B | IQANK1 activity raises ELMO3's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without IQANK1 | 0.061 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.5, 53.8); signed map (58.8, 9.7). **Vector** length 77.2, 19.8% of its response variance represented; |z| ≥ 3 in 774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +1.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -14.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.2 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.2 | -10.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.2 | -6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif and ankyrin repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,734,139-143,790,645 (+) |
| Ensembl biotype | protein_coding |
| Also known as | onco-lncRNA-3, CACClnc; previously FAM83H-AS1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [A8MXQ7](https://www.uniprot.org/uniprotkb/A8MXQ7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49576) · Entrez [642574](https://www.ncbi.nlm.nih.gov/gene/642574) · UniProt [A8MXQ7](https://www.uniprot.org/uniprotkb/A8MXQ7) · Ensembl [ENSG00000203499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203499)

## Data

Gene col 12770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12770); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12770]; `tensor/DDL_lfc|DDL_z.npy` [12770]; `embed/gene_vectors.npy` [12770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12770 or target_col == 12770). Every well: [[IQANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
