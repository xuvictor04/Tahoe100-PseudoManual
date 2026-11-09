---
symbol: "HSDL1"
type: "gene"
col: 2328
ensembl_id: "ENSG00000103160"
name: "hydroxysteroid dehydrogenase like 1"
location: "16q24.1"
module: 30
arm: "+"
pooled_cpm: 20.13
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# HSDL1

*hydroxysteroid dehydrogenase like 1* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.38× (z +16.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.510× (z -12.5, q 6e-33, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LCMT1]] (+0.71, fdr 2e-05), [[STX7]] (+0.68, fdr 1e-05), [[MPND]] (+0.68, fdr 1e-05); moves opposite to [[TRIP12]] (-0.65, fdr 2e-05), [[SKIL]] (-0.63, fdr 1e-05), [[CACNA2D1]] (-0.63, fdr 5e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GJB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.38×** | +16.6 | 0e+00 | 46/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +15.8 | 0e+00 | 45/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +12.9 | 1e-35 | 40/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.9 | 5e-07 | 20/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +5.1 | 3e-05 | 16/48 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.8 | 1e-04 | 19/48 (SW480, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +4.8 | 1e-04 | 8/48 (RKO, J82, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 2e-04 | 17/45 (HCT15, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.002 | 17/46 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.9 | 0.006 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.010 | 11/45 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.016 | 8/44 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.062 | 9/48 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.073 | 4/47 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.17× | +3.0 | 0.087 | 6/46 (HT-29, BT-474, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.510×** | -12.5 | 6e-33 | 35/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.682×** | -6.8 | 3e-09 | 19/39 (CFPAC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -6.7 | 4e-09 | 27/47 (SW480, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.725×** | -6.2 | 7e-08 | 21/47 (Panc 03.27, SW480, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.726×** | -6.2 | 7e-08 | 25/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.729×** | -6.1 | 1e-07 | 22/41 (HT-29, HOP62, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.752×** | -5.5 | 3e-06 | 24/47 (SW480, NCI-H460, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.776×** | -4.9 | 6e-05 | 22/48 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.776×** | -4.9 | 6e-05 | 21/46 (SW480, NCI-H460, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.842× | -4.5 | 4e-04 | 19/47 (SW480, SW1417, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.797×** | -4.4 | 6e-04 | 20/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.670×** | -4.0 | 0.003 | 14/28 (SW 900, A-427, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.680×** | -3.9 | 0.004 | 14/47 (NCI-H23, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -3.8 | 0.005 | 17/48 (SW480, A-427, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.816×** | -3.8 | 0.006 | 11/46 (hTERT-HPNE, SW48, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.832×** | -3.4 | 0.028 | 10/47 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Olanzapine (drug)]] 5 µM |  | 0.894× | -3.0 | 0.079 | 4/48 (CFPAC-1, A549, …) | top dose only | position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.859× | -2.9 | 0.094 | 4/47 (NCI-H2030, HEC-1-A, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.0 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 15.7 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.9) ⚠ cell-cycle shift, explains ~71% of this change | [[Harringtonine (drug)]] 0.5 µM 0.297× (z -11.4) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.352× (z -9.4) |
| [[A-427 (line)]] | wt | 22.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.8) ⚠ cell-cycle shift, explains ~71% of this change | [[Harringtonine (drug)]] 5 µM 0.284× (z -9.4) |
| [[A498 (line)]] | wt | 14.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.189× (z -8.8) |
| [[KATO III (line)]] | alt | 13.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 29.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 21.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.321× (z -8.8) |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.155× (z -12.4) |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.259× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 28.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -9.9) |
| [[PANC-1 (line)]] | alt | 18.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.157× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -11.0) |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.228× (z -8.9) |
| [[A-172 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | +0.71 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[STX7]] | +0.68 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MPND]] | +0.68 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[SLC15A4]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.67 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.66 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[PLD3]] | +0.66 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MTM1]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[CABLES2]] | +0.65 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MMS19]] | +0.64 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[HEATR5B]] | +0.64 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[RNF41]] | +0.64 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP12]] | -0.65 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[SKIL]] | -0.63 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.63 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[TASOR]] | -0.62 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ST7L]] | -0.61 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[LINC01934]] | -0.61 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[C1RL-AS1]] | -0.61 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ARRDC3-AS1]] | -0.60 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[DGKH]] | -0.60 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ARAP2]] | -0.60 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ADAMTS3]] | -0.59 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[LEKR1]] | -0.59 | -0.35 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GJB2]] | B | GJB2 activity lowers HSDL1's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.21× higher at baseline in the lines without GJB2 | 0.052 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[THRB]] | B | THRB activity lowers HSDL1's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.28× higher at baseline in the lines without THRB | 0.060 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[XKR8]] | B | XKR8 activity lowers HSDL1's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.31× higher at baseline in the lines without XKR8 | 0.084 | ⚠ within organs, on part of the lines; also absent: MORC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.4, -4.5); signed map (-37.2, -2.2). **Vector** length 88.2, 17.7% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +16.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +15.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +12.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -4.5 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.5 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid dehydrogenase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,122,141-84,145,192 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR12C3 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Matched by | ensembl_id |

UniProt [Q3SXM5](https://www.uniprot.org/uniprotkb/Q3SXM5) carries no function annotation.

**Summary**, from NCBI Gene [83693](https://www.ncbi.nlm.nih.gov/gene/83693):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16475) · Entrez [83693](https://www.ncbi.nlm.nih.gov/gene/83693) · UniProt [Q3SXM5](https://www.uniprot.org/uniprotkb/Q3SXM5) · Ensembl [ENSG00000103160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103160)

## Data

Gene col 2328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2328); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2328]; `tensor/DDL_lfc|DDL_z.npy` [2328]; `embed/gene_vectors.npy` [2328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2328 or target_col == 2328). Every well: [[HSDL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSDL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
