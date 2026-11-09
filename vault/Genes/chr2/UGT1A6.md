---
symbol: "UGT1A6"
type: "gene"
col: 9427
ensembl_id: "ENSG00000167165"
name: "UDP glucuronosyltransferase family 1 member A6"
location: "2q37.1"
module: 44
arm: "+"
pooled_cpm: 22.78
n_lines_expressing: 15
n_dd_up: 25
n_dd_down: 26
n_dd_up_clean: 19
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 52
direction_downstream: 84
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# UGT1A6

*UDP glucuronosyltransferase family 1 member A6* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.12× (z +14.5, q 1e-44, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.65× (z +6.5, q 1e-08, up in 8 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.387× (z -10.1, q 3e-21, down in 12 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGT1A9]] (+0.92, fdr 7e-06, ⚠ same locus), [[UGT1A1]] (+0.92, fdr 7e-06, ⚠ same locus), [[UGT1A8]] (+0.88, fdr 7e-06, ⚠ same locus), [[GCNT3]] (+0.76, fdr 7e-06), [[PIP5K1B]] (+0.74, fdr 7e-06), [[LGALS4]] (+0.74, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.54, fdr 2e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 84 go from it, the strongest it → [[MECOM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.12×** | +14.5 | 1e-44 | 3/10 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.77×** | +14.1 | 9e-43 | 5/12 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +10.7 | 2e-24 | 3/10 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.65×** | +6.5 | 1e-08 | 8/13 (AsPC-1, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.82×** | +6.1 | 1e-07 | 10/12 (J82, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.68×** | +5.5 | 4e-06 | 10/13 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.67×** | +5.3 | 1e-05 | 7/12 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.0 | 4e-05 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.61×** | +4.8 | 1e-04 | 7/13 (AsPC-1, J82, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 9/13 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **2.17×** | +4.3 | 8e-04 | 7/12 (LS 180, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.15×** | +4.3 | 9e-04 | 6/12 (AsPC-1, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.006 | 6/13 (LS 180, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +3.7 | 0.009 | 9/13 (J82, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.010 | 9/12 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.015 | 8/13 (AsPC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.016 | 8/13 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.017 | 3/12 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.017 | 4/12 (J82, AsPC-1, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.030 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.387×** | -10.1 | 3e-21 | 12/12 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.458×** | -8.3 | 3e-14 | 11/13 (HT-29, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.533×** | -6.7 | 4e-09 | 13/13 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.556×** | -6.3 | 6e-08 | 12/13 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.547×** | -6.2 | 8e-08 | 11/13 (HT-29, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.685×** | -5.7 | 1e-06 | 12/13 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.580×** | -5.6 | 2e-06 | 7/13 (Hs 766T, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -5.1 | 2e-05 | 9/12 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.415×** | -4.9 | 6e-05 | 3/13 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.631×** | -4.9 | 6e-05 | 8/12 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.668×** | -4.3 | 9e-04 | 8/12 (LS 180, HT-29, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.677×** | -4.1 | 0.002 | 7/12 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.688×** | -4.0 | 0.003 | 8/12 (HT-29, LS 180, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.694×** | -3.9 | 0.004 | 8/13 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.689×** | -3.8 | 0.005 | 9/12 (HT-29, LS 180, …) | top dose only |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.719×** | -3.5 | 0.015 | 0/13 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -3.4 | 0.023 | 10/13 (LS 180, HT-29, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 159 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0555× (z -26.3) |
| [[LoVo (line)]] | wt | 229 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0463× (z -31.7) |
| [[COLO 205 (line)]] | alt | 107 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0804× (z -20.1) |
| [[LS 180 (line)]] | wt | 90.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -18.3) |
| [[NCI-H1792 (line)]] | alt | 72.8 | 1 (1 ⚠) | 4 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +8.8) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -14.4) |
| [[KATO III (line)]] | alt | 128 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.6) |
| [[Hs 766T (line)]] | wt | 53.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0749× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 8.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -9.6) |
| [[SNU-423 (line)]] | alt | 8.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0594× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGT1A9]] | +0.92 | +0.92 / +0.89 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 998; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UGT1A1]] | +0.92 | +0.93 / +0.88 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 998; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UGT1A8]] | +0.88 | +0.89 / +0.84 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 997; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GCNT3]] | +0.76 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[PIP5K1B]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.74 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[TSPAN8]] | +0.74 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[PRR15]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[CDH17]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[HEPH]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[PRR15L]] | +0.72 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[TM4SF4]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[GPA33]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[MUC13]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[ST6GALNAC1]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 1, C 51. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers UGT1A6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[UGT1A1]] | C | UGT1A1 activity raises UGT1A6's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 13.09× lower at baseline in the lines without UGT1A1 | 5e-06 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[UGT1A8]], [[UGT1A9]] | C | UGT1A8, UGT1A9 activity raises UGT1A6's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 8.89× lower at baseline in the lines without UGT1A8, UGT1A9 | 5e-05 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[CREB3L1]] | C | CREB3L1 activity raises UGT1A6's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 4.67× lower at baseline in the lines without CREB3L1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises UGT1A6's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 16.63× lower at baseline in the lines without NPSR1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[PTPRR]] | C | PTPRR activity raises UGT1A6's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 4.17× lower at baseline in the lines without PTPRR | 0.003 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |
| [[IL20RA]] | C | IL20RA activity raises UGT1A6's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 5.75× lower at baseline in the lines without IL20RA | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises UGT1A6's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 8.61× lower at baseline in the lines without PLA2G2A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[LINC01133]] | C | LINC01133 activity raises UGT1A6's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 5.59× lower at baseline in the lines without LINC01133 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises UGT1A6's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 10.70× lower at baseline in the lines without FAM3D | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[TSPAN8]] | C | TSPAN8 activity raises UGT1A6's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 5.65× lower at baseline in the lines without TSPAN8 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises UGT1A6's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 7.82× lower at baseline in the lines without LINC01559 | 0.007 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 24, C 60. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MECOM]] | B | UGT1A6 activity raises MECOM's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 4.74× lower at baseline in the lines without UGT1A6 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[RSPH1]] | B | UGT1A6 activity raises RSPH1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 1.74× lower at baseline in the lines without UGT1A6 | 0.014 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[C4orf19]] | B | UGT1A6 activity raises C4orf19's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.48× lower at baseline in the lines without UGT1A6 | 0.020 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[PLA2R1]] | B | UGT1A6 activity raises PLA2R1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.75× lower at baseline in the lines without UGT1A6 | 0.024 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[MUC3A]] | B | UGT1A6 activity raises MUC3A's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.60× lower at baseline in the lines without UGT1A6 | 0.031 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[LINC02580]] | B | UGT1A6 activity raises LINC02580's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 1.66× lower at baseline in the lines without UGT1A6 | 0.035 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[PLCH1]] | B | UGT1A6 activity strengthens PLCH1's drug response | lines that do not express UGT1A6 (27) vs lines expressing it (9) | the lines without UGT1A6 respond 0.68× as strongly (z diff +0.77); strongest at Panobinostat 0.5 µM: 0.60x vs 0.37x (z diff +3.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; target measured in part of the lines; artifact flags |
| [[MUC12]] | B | UGT1A6 activity raises MUC12's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.00× lower at baseline in the lines without UGT1A6 | 0.040 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[ASS1]] | B | UGT1A6 activity strengthens ASS1's drug response | lines that do not express UGT1A6 (24) vs lines expressing it (10) | the lines without UGT1A6 respond 0.52× as strongly (z diff +2.64); strongest at Homoharringtonine 0.5 µM: 0.53x vs 0.28x (z diff +4.0) | 0.044 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; target measured in part of the lines; artifact flags |
| [[ATP8B1]] | B | UGT1A6 activity raises ATP8B1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 3.12× lower at baseline in the lines without UGT1A6 | 0.051 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[MUC12]] | B | UGT1A6 activity weakens MUC12's drug response | lines that do not express UGT1A6 (19) vs lines expressing it (8) | (z diff -2.61); strongest at Homoharringtonine 5 µM: 2.12x vs 0.49x (z diff -7.4) | 0.057 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; target measured in part of the lines; artifact flags |
| [[DYRK2]] | B | UGT1A6 activity raises DYRK2's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 1.39× lower at baseline in the lines without UGT1A6 | 0.060 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.6, 51.5); signed map (63.4, 3.9). **Vector** length 71.6, 31.7% of its response variance represented; |z| ≥ 3 in 445 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.56 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.56 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +14.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +5.3 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -4.9 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -5.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | UDP glucuronosyltransferase family 1 member A6 |
| Locus type | complex locus constituent (other) |
| Location | 2q37.1 — chr2:233,691,607-233,773,300 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HLUGP, GNT1, UGT1F |
| Gene groups (HGNC) | UDP glucuronosyltransferases |
| Reactome | 6 pathways, smallest: Glucuronidation; Aspirin ADME; Paracetamol ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P19224](https://www.uniprot.org/uniprotkb/P19224) (UDP-glucuronosyltransferase 1A6):

> [Isoform 1]: UDP-glucuronosyltransferase (UGT) that catalyzes phase II biotransformation reactions in which lipophilic substrates are conjugated with glucuronic acid to facilitate their inactivation and excretion from the body. Essential for the elimination and detoxification of drugs, xenobiotics and endogenous compounds. Involved in the glucuronidation of arachidonic acid (AA) and AA-derived eicosanoids including 15-HETE and 20-HETE. Conjugates small planar phenolic molecules such as …

**Summary**, from NCBI Gene [54578](https://www.ncbi.nlm.nih.gov/gene/54578):

> This gene encodes a UDP-glucuronosyltransferase, an enzyme of the glucuronidation pathway that transforms small lipophilic molecules, such as steroids, bilirubin, hormones, and drugs, into water-soluble, excretable metabolites. This gene is part of a complex locus that encodes several UDP-glucuronosyltransferases. The locus includes thirteen unique alternate first exons followed by four common exons. Four of the alternate first exons are considered pseudogenes. Each of the remaining nine 5' …

**Accessions** — [HGNC:12538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12538) · Entrez [54578](https://www.ncbi.nlm.nih.gov/gene/54578) · UniProt [P19224](https://www.uniprot.org/uniprotkb/P19224) · Ensembl [ENSG00000167165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167165)

## Data

Gene col 9427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9427); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9427]; `tensor/DDL_lfc|DDL_z.npy` [9427]; `embed/gene_vectors.npy` [9427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9427 or target_col == 9427). Every well: [[UGT1A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGT1A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
