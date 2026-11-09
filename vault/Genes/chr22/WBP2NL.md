---
symbol: "WBP2NL"
type: "gene"
col: 11365
ensembl_id: "ENSG00000183066"
name: "WBP2 N-terminal like"
location: "22q13.2"
module: 12
arm: "+"
pooled_cpm: 8.2
n_lines_expressing: 33
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# WBP2NL

*WBP2 N-terminal like* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +6.4, q 7e-08, up in 22 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.374× (z -9.0, q 6e-17, down in 26 of 31 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.374× (z -9.0, q 6e-17, down in 24 of 29 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMB2P1]] (+0.57, fdr 1e-05), [[SRSF11]] (+0.56, fdr 1e-05, ⚠ SRSF11 in the vector space only through flagged drug-doses), [[ZNF444]] (+0.55, fdr 7e-05), [[ZNF559-ZNF177]] (+0.55, fdr 1e-05); moves opposite to [[PGRMC1]] (-0.59, fdr 1e-05), [[PRPS2]] (-0.55, fdr 1e-05), [[PTDSS1]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF271P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.4 | 7e-08 | 22/30 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +4.7 | 8e-04 | 19/29 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.3 | 0.003 | 3/16 (NCI-H2347, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.027 | 10/29 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.095 | 12/30 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.45×** | +3.3 | 0.099 | 11/29 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.41× | +3.0 | 0.21 | 9/29 (SW480, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.374×** | -9.0 | 6e-17 | 26/31 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.374×** | -9.0 | 6e-17 | 24/29 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.461×** | -7.1 | 2e-10 | 25/29 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -6.3 | 5e-08 | 23/29 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.518×** | -6.0 | 2e-07 | 19/29 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.567×** | -5.2 | 2e-05 | 21/29 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.594×** | -4.8 | 1e-04 | 17/29 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.591×** | -4.6 | 2e-04 | 19/28 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.597×** | -4.6 | 3e-04 | 14/29 (A498, SW 900, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.402×** | -4.4 | 7e-04 | 16/28 (SW 900, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -3.9 | 0.005 | 14/29 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.651×** | -3.8 | 0.007 | 15/27 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.621×** | -3.7 | 0.008 | 13/30 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **0.671×** | -3.5 | 0.018 | 14/27 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.704×** | -3.2 | 0.050 | 12/29 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.795×** | -3.0 | 0.096 | 5/29 (LS 180, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.4 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0917× (z -15.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.110× (z -14.0) |
| [[A498 (line)]] | wt | 20.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 94.6 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -14.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.185× (z -8.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -11.0) |
| [[HCT15 (line)]] | alt | 7.14 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0562× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 7.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0612× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 6.70 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0976× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 5.00 | 0 | 1 | — | [[Pimitespib (drug)]] 0.05 µM 0.0553× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 8.66 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 8.59 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 5.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.845 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMB2P1]] | +0.57 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[SRSF11]] ⚠ | +0.56 | +0.60 / +0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF444]] | +0.55 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[ZNF559-ZNF177]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ZNF271P]] | +0.54 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZNF780B]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ZC3H15]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RNF32-DT]] | +0.53 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PRPF38B]] | +0.52 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[C19orf18]] | +0.52 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF559]] | +0.52 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[LINC01535]] | +0.52 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ZNF605]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGRMC1]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PTDSS1]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[KNTC1]] | -0.52 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[GINS4]] | -0.50 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[NAGA]] | -0.49 | -0.41 / -0.58 | both halves | 4e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TYMS]] | -0.49 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TPI1]] | -0.49 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[PCLAF]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[GPAA1]] | -0.49 | -0.16 / -0.61 | ⚠ one half (not replicated) | 0.001 |  |
| [[PASK]] | -0.48 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[IVNS1ABP]] | -0.48 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[PIGX]] | -0.48 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[SUMO3]] | -0.48 | -0.37 / -0.54 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WBP2NL's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF271P]] | B | WBP2NL activity lowers ZNF271P's level | lines that do not express WBP2NL (17) vs lines expressing it (33) | 1.35× higher at baseline in the lines without WBP2NL | 0.015 | ⚠ within organs, on part of the lines; also absent: ATP2A3, GCNT2, ENSG00000235726; maybe low, not absent |
| [[SEC62]] | B | WBP2NL activity lowers SEC62's level | lines that do not express WBP2NL (17) vs lines expressing it (33) | 1.18× higher at baseline in the lines without WBP2NL | 0.091 | ⚠ within organs, on part of the lines; also absent: ATP2A3, GCNT2, ENSG00000235726; maybe low, not absent |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-43.6, 15.1); signed map (-13.2, -18.8). **Vector** length 56.8, 12.3% of its response variance represented; |z| ≥ 3 in 599 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +4.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.4 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.4 | -9.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.1 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | WBP2 N-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,998,725-42,058,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ26145, MGC26816, PAWP, GRAMD7 |
| Gene groups (HGNC) | GRAM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ICG8](https://www.uniprot.org/uniprotkb/Q6ICG8) (Postacrosomal sheath WW domain-binding protein):

> May play a role in meiotic resumption and pronuclear formation, mediated by a WW domain-signaling pathway during fertilization.

**Summary**, from NCBI Gene [164684](https://www.ncbi.nlm.nih.gov/gene/164684):

> WBP2NL is a sperm-specific WW domain-binding protein that promotes meiotic resumption and pronuclear development during oocyte fertilization (Wu et al., 2007 [PubMed 17289678]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28389) · Entrez [164684](https://www.ncbi.nlm.nih.gov/gene/164684) · UniProt [Q6ICG8](https://www.uniprot.org/uniprotkb/Q6ICG8) · Ensembl [ENSG00000183066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183066)

## Data

Gene col 11365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11365); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11365]; `tensor/DDL_lfc|DDL_z.npy` [11365]; `embed/gene_vectors.npy` [11365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11365 or target_col == 11365). Every well: [[WBP2NL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WBP2NL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
