---
symbol: "ARHGEF17"
type: "gene"
col: 3124
ensembl_id: "ENSG00000110237"
name: "Rho guanine nucleotide exchange factor 17"
location: "11q13.4"
module: 46
arm: "+"
pooled_cpm: 20.55
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ARHGEF17

*Rho guanine nucleotide exchange factor 17* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +12.0, q 1e-30, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.431× (z -11.2, q 2e-26, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID1A]] (+0.66, fdr 3e-05), [[SETD1B]] (+0.61, fdr 4e-05), [[LATS2]] (+0.60, fdr 1e-05); moves opposite to [[ARPC1A]] (-0.58, fdr 2e-04), [[NBPF3]] (-0.56, fdr 3e-04), [[CYB5R4]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PXDC1]] → it (grade B ⚠); 9 go from it, the strongest it → [[STK11]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +12.0 | 1e-30 | 32/44 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +4.9 | 3e-04 | 22/44 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.7 | 5e-04 | 24/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.25× | +3.0 | 0.34 | 8/44 (HS-578T, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.431×** | -11.2 | 2e-26 | 35/44 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.481×** | -9.7 | 5e-20 | 35/44 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.515×** | -8.8 | 2e-16 | 31/44 (HEC-1-A, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.616×** | -6.5 | 1e-08 | 26/44 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.418×** | -6.1 | 1e-07 | 26/44 (SW480, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.637×** | -6.0 | 2e-07 | 25/39 (RPMI-7951, NCI-H23, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.659×** | -5.5 | 2e-06 | 24/44 (SK-MEL-2, HT-29, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.466×** | -5.3 | 7e-06 | 27/43 (LS 180, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.652×** | -5.3 | 9e-06 | 21/36 (HCT15, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.688×** | -5.0 | 4e-05 | 24/44 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -4.9 | 6e-05 | 22/44 (HT-29, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.656×** | -4.0 | 0.003 | 17/44 (SW480, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.750×** | -3.8 | 0.006 | 18/44 (NCI-H1792, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -3.6 | 0.012 | 19/44 (SNU-423, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -3.6 | 0.012 | 17/42 (NCI-H2030, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.757×** | -3.5 | 0.016 | 16/44 (AN3 CA, LS 180, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.617×** | -3.4 | 0.025 | 15/43 (SW1417, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.624×** | -3.3 | 0.030 | 14/44 (SW1417, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | 0.847× | -3.1 | 0.048 | 10/44 (C32, PANC-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.720×** | -3.1 | 0.048 | 10/44 (HCT15, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.641×** | -3.1 | 0.049 | 11/44 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 82.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 39.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 36.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.355× (z -8.6) |
| [[A498 (line)]] | wt | 28.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.343× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.181× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 22.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.174× (z -9.8) ⚠ toxic |
| [[A549 (line)]] | wt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[AsPC-1 (line)]] | alt | 9.02 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0966× (z -8.8) |
| [[H4 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0835× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HT-29 (line)]] | alt | 28.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.148× (z -11.6) |
| [[LoVo (line)]] | wt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 5.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 7.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0685× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.120× (z -12.1) |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.267× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 18.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.267× (z -9.7) |
| [[A-427 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID1A]] | +0.66 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[SETD1B]] | +0.61 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[LATS2]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SIX5]] | +0.59 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PHF2]] | +0.58 | +0.37 / +0.41 | both halves | 8e-05 |  |
| [[AJUBA]] | +0.58 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[STK11]] | +0.58 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[BRD1]] | +0.57 | +0.50 / +0.31 | both halves | 2e-04 |  |
| [[INPPL1]] | +0.57 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[FBRS]] | +0.57 | +0.39 / +0.38 | both halves | 6e-05 |  |
| [[MEPCE]] | +0.57 | +0.49 / +0.29 | both halves | 3e-04 |  |
| [[AMOTL2]] | +0.56 | +0.64 / +0.41 | both halves | 4e-05 | STRING 478 |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC1A]] | -0.58 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[NBPF3]] | -0.56 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[CYB5R4]] | -0.56 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[BMERB1]] | -0.54 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[CSNK2A1]] | -0.54 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[PIP4K2A]] | -0.53 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[MFSD9]] | -0.53 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[PLA2G12A]] | -0.53 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[SERAC1]] | -0.53 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[COMMD2]] | -0.52 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[RADX]] | -0.51 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[SH3PXD2B]] | -0.51 | -0.40 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXDC1]] | B | PXDC1 activity raises ARHGEF17's level | lines that do not express PXDC1 (9) vs lines expressing it (41) | 2.06× lower at baseline in the lines without PXDC1 | 0.086 | ⚠ within organs, on part of the lines; also absent: TSPAN4, OSMR, VIM |
| [[SIX4]] | B | SIX4 activity raises ARHGEF17's level | lines that do not express SIX4 (5) vs lines expressing it (45) | 3.36× lower at baseline in the lines without SIX4 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CPLANE1, FGFR1 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK11]] | C | ARHGEF17 activity raises STK11's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[PIEZO1]] | C | ARHGEF17 activity raises PIEZO1's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[AJUBA]] | C | ARHGEF17 activity raises AJUBA's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[SIX5]] | C | ARHGEF17 activity raises SIX5's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[FAM174B]] | C | ARHGEF17 activity lowers FAM174B's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.55× higher at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[HDAC7]] | C | ARHGEF17 activity raises HDAC7's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.51× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[HNRNPH3]] | C | ARHGEF17 activity raises HNRNPH3's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[LATS2]] | C | ARHGEF17 activity raises LATS2's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without ARHGEF17 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[AMOTL2]] | C | ARHGEF17 activity raises AMOTL2's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without ARHGEF17 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (14.9, 8.2); signed map (26.2, -24.2). **Vector** length 91.2, 19.9% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.8 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.6 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.2 | -8.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.1 | -11.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,308,276-73,369,388 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEM4, KIAA0337, p164-RhoGEF |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Reactome | 13 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PE2](https://www.uniprot.org/uniprotkb/Q96PE2) (Rho guanine nucleotide exchange factor 17):

> Acts as a guanine nucleotide exchange factor (GEF) for RhoA GTPases.

**Summary**, from NCBI Gene [9828](https://www.ncbi.nlm.nih.gov/gene/9828):

> Enables guanyl-nucleotide exchange factor activity. Acts upstream of or within actin cytoskeleton organization. Predicted to be located in cytosol. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21726) · Entrez [9828](https://www.ncbi.nlm.nih.gov/gene/9828) · UniProt [Q96PE2](https://www.uniprot.org/uniprotkb/Q96PE2) · Ensembl [ENSG00000110237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110237)

## Data

Gene col 3124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3124); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3124]; `tensor/DDL_lfc|DDL_z.npy` [3124]; `embed/gene_vectors.npy` [3124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3124 or target_col == 3124). Every well: [[ARHGEF17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
