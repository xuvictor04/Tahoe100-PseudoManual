---
symbol: "CLCN5"
type: "gene"
col: 10097
ensembl_id: "ENSG00000171365"
name: "Cl-/H+ antiporter 5"
location: "Xp11.23"
module: 18
arm: "+"
pooled_cpm: 30.94
n_lines_expressing: 49
n_dd_up: 40
n_dd_down: 6
n_dd_up_clean: 31
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CLCN5

*Cl-/H+ antiporter 5* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +20.7, q 0e+00, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.507× (z -7.4, q 7e-11, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNPDA1]] (+0.52, fdr 1e-05), [[CLN6]] (+0.51, fdr 2e-05), [[VPS8]] (+0.50, fdr 1e-05); moves opposite to [[KDM5A]] (-0.48, fdr 3e-05), [[C18orf25]] (-0.48, fdr 1e-03, ⚠ one half only (not replicated)), [[ZNF350]] (-0.44, fdr 1e-04), [[TCAF2]] (-0.44, fdr 8e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PPFIBP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +20.7 | 0e+00 | 37/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +14.9 | 0e+00 | 38/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +12.2 | 4e-32 | 41/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +11.1 | 2e-26 | 39/46 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +10.6 | 5e-24 | 34/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +10.5 | 6e-24 | 39/46 (LoVo, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +10.4 | 1e-23 | 36/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +10.1 | 4e-22 | 35/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +9.3 | 8e-19 | 31/45 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.2 | 1e-18 | 28/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +8.6 | 6e-16 | 32/47 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +8.5 | 1e-15 | 33/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +8.0 | 7e-14 | 30/46 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +7.0 | 1e-10 | 32/47 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.60×** | +7.0 | 1e-10 | 24/47 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.88×** | +6.8 | 3e-10 | 22/46 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.80×** | +6.4 | 7e-09 | 23/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.507×** | -7.4 | 7e-11 | 29/47 (LoVo, SHP-77, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.531×** | -6.9 | 1e-09 | 24/45 (A549, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.746×** | -5.9 | 6e-07 | 15/34 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.630×** | -5.1 | 6e-05 | 18/43 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.752×** | -4.3 | 0.002 | 18/46 (AN3 CA, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.805×** | -4.2 | 0.002 | 17/39 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.857× | -3.3 | 0.091 | 16/41 (SNU-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.811× | -3.1 | 0.12 | 7/43 (RPMI-7951, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +22.5) | — |
| [[NCI-H1573 (line)]] | alt | 29.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 38.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +14.2) | [[vincristine (drug)]] 5 µM 0.107× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 39.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.9) | — |
| [[A-427 (line)]] | wt | 55.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 20.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.73× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.5) | — |
| [[KATO III (line)]] | alt | 80.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 58.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.3) | — |
| [[NCI-H2347 (line)]] | alt | 26.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +19.3) | — |
| [[SNU-1 (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +9.1) | — |
| [[A549 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -12.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +12.4) | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.05 µM 0.0634× (z -8.8) |
| [[COLO 205 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -10.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +10.6) | — |
| [[J82 (line)]] | alt | 35.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +18.0) | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +12.7) | — |
| [[RKO (line)]] | wt | 36.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.238× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[SNU-423 (line)]] | alt | 38.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.4) | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPDA1]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CLN6]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[VPS8]] | +0.50 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SCMH1]] | +0.48 | +0.52 / +0.27 | both halves | 3e-04 |  |
| [[SLC25A13]] | +0.46 | +0.53 / +0.33 | both halves | 1e-04 | same gene group |
| [[HEXB]] | +0.45 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[PTPDC1]] | +0.45 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[DUSP3]] | +0.44 | +0.41 / +0.38 | both halves | 7e-05 |  |
| [[GALNT11]] | +0.44 | +0.27 / +0.50 | both halves | 3e-04 |  |
| [[MTCH2]] | +0.44 | +0.49 / +0.37 | both halves | 7e-05 |  |
| [[SLC36A1]] | +0.44 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[COPRS]] | +0.43 | +0.49 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM5A]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[C18orf25]] | -0.48 | -0.53 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[ZNF350]] | -0.44 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[TCAF2]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[TMCO1]] | -0.43 | -0.47 / -0.26 | both halves | 3e-04 |  |
| [[SH3BP5L]] | -0.42 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[RETREG3]] | -0.42 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[XRCC6]] | -0.42 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ILF2]] | -0.41 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[ING4]] | -0.41 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[ZNF17]] | -0.41 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[OTUD5]] | -0.41 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[SNRPD3]] | -0.41 | -0.42 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPFIBP2]] | B | PPFIBP2 activity raises CLCN5's level | lines that do not express PPFIBP2 (5) vs lines expressing it (45) | 2.07× lower at baseline in the lines without PPFIBP2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LRRC8D |
| [[TCAF2]] | C | TCAF2 activity lowers CLCN5's level | lines that do not express TCAF2 (4) vs lines expressing it (46) | 2.51× higher at baseline in the lines without TCAF2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.279). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.4, -50.2); signed map (7.3, -47.1). **Vector** length 82.9, 17.3% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.2 | +10.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +6.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.2 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.0 | +10.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.2 | +7.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.7 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.6 | -6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.1 | -2.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | Cl-/H+ antiporter 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,922,596-50,099,235 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DENTS, XLRH, hClC-K2, hCIC-K2, CLC5, XRN, ClC-5; previously NPHL2, NPHL1 |
| Gene groups (HGNC) | CLC chloride channel and transporter family; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P51795](https://www.uniprot.org/uniprotkb/P51795) (H(+)/Cl(-) exchange transporter 5):

> Proton-coupled chloride transporter. Functions as antiport system and exchanges chloride ions against protons. Important for normal acidification of the endosome lumen. May play an important role in renal tubular function. The CLC channel family contains both chloride channels and proton-coupled anion transporters that exchange chloride or another anion for protons. The absence of conserved gating glutamate residues is typical for family members that function as channels (Probable).

**Summary**, from NCBI Gene [1184](https://www.ncbi.nlm.nih.gov/gene/1184):

> This gene encodes a member of the ClC family of chloride ion channels and ion transporters. The encoded protein is primarily localized to endosomal membranes and may function to facilitate albumin uptake by the renal proximal tubule. Mutations in this gene have been found in Dent disease and renal tubular disorders complicated by nephrolithiasis. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:2023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2023) · Entrez [1184](https://www.ncbi.nlm.nih.gov/gene/1184) · UniProt [P51795](https://www.uniprot.org/uniprotkb/P51795) · Ensembl [ENSG00000171365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171365)

## Data

Gene col 10097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10097); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10097]; `tensor/DDL_lfc|DDL_z.npy` [10097]; `embed/gene_vectors.npy` [10097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10097 or target_col == 10097). Every well: [[CLCN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLCN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
