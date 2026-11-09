---
symbol: "TTYH2"
type: "gene"
col: 6539
ensembl_id: "ENSG00000141540"
name: "tweety family member 2"
location: "17q25.1"
module: 154
arm: "+"
pooled_cpm: 6.23
n_lines_expressing: 41
n_dd_up: 37
n_dd_down: 4
n_dd_up_clean: 28
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# TTYH2

*tweety family member 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.84× (z +21.1, q 0e+00, up in 22 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.713× (z -4.9, q 5e-04, down in 15 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTAC1]] (+0.57, fdr 1e-05), [[CELSR1]] (+0.55, fdr 9e-05), [[SNAI1]] (+0.55, fdr 6e-05); moves opposite to [[TAF8]] (-0.53, fdr 4e-05), [[ZNF214]] (-0.48, fdr 4e-04), [[YIPF4]] (-0.47, fdr 4e-04).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CYP26B1]] → it (grade B ⚠); 7 go from it, the strongest it → [[SCMH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +21.1 | 0e+00 | 22/32 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.18×** | +20.5 | 0e+00 | 33/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.11×** | +20.2 | 0e+00 | 30/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.33×** | +17.2 | 0e+00 | 28/37 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +10.3 | 1e-22 | 21/37 (SW480, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +9.9 | 3e-21 | 20/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +9.9 | 3e-21 | 13/32 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +8.7 | 3e-16 | 12/29 (HOP62, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.4 | 2e-15 | 15/33 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.80×** | +8.0 | 5e-14 | 8/23 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.71×** | +7.3 | 1e-11 | 1/10 (MIA PaCa-2) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +7.0 | 1e-10 | 14/37 (C32, SW480, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.7 | 9e-10 | 15/34 (SW480, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +6.7 | 9e-10 | 13/34 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.41×** | +6.6 | 2e-09 | 8/35 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +6.1 | 3e-08 | 13/28 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[EX229 (drug)]] 5 µM |  | **2.15×** | +5.7 | 4e-07 | 8/27 (NCI-H460, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +5.3 | 3e-06 | 7/33 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6539.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.713×** | -4.9 | 5e-04 | 15/37 (PANC-1, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -4.2 | 0.008 | 9/37 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.755×** | -4.1 | 0.008 | 13/37 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.763×** | -4.0 | 0.011 | 14/30 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.790× | -3.3 | 0.10 | 6/35 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.808× | -3.1 | 0.17 | 11/36 (A549, SW 900, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.813× | -3.0 | 0.17 | 8/37 (NCI-H1792, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -3.0 | 0.17 | 12/37 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 13.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0974× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.0989× (z -11.5) |
| [[PANC-1 (line)]] | alt | 7.11 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.16× (z +9.8) | — |
| [[RKO (line)]] | wt | 9.68 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 7.07 | 0 | 2 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0599× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 58.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.0) |
| [[SNU-423 (line)]] | alt | 9.95 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.79× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 3.89 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0544× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.215× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 4.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 7.44 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0628× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 4.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0594× (z -12.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW48 (line)]] | wt | 11.7 | 0 | 1 | — | [[Verapamil (drug)]] 0.05 µM 0.0607× (z -9.2) |
| [[SW480 (line)]] | alt | 5.34 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.04× (z +10.3) | — |
| [[A-172 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAC1]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CELSR1]] | +0.55 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[SNAI1]] | +0.55 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[WNT7B]] | +0.54 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[OTUB2]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PLTP]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[TNFRSF11A]] | +0.53 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[RTN4RL2]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CDKL2]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[GALNT12]] | +0.50 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[CELF5]] | +0.50 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[ADAM7-AS1]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF8]] | -0.53 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[ZNF214]] | -0.48 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[YIPF4]] | -0.47 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[ENOX2]] | -0.46 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[TRAPPC8]] | -0.46 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[AP4E1]] | -0.45 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[ZNF649]] | -0.44 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[SLC26A2]] | -0.43 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[ZNF700]] | -0.43 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[KIF27]] | -0.43 | -0.30 / -0.28 | both halves | 3e-04 |  |
| [[CPSF2]] | -0.43 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[SCMH1]] | -0.43 | -0.46 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP26B1]] | B | CYP26B1 activity raises TTYH2's level | lines that do not express CYP26B1 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without CYP26B1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, ENSG00000242029, ELOVL2 |
| [[LOXL2]] | B | LOXL2 activity raises TTYH2's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without LOXL2 | 0.079 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[TOP2A]] | B | TOP2A activity lowers TTYH2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCMH1]] | B | TTYH2 activity raises SCMH1's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without TTYH2 | 0.012 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[SEPTIN6]] | B | TTYH2 activity raises SEPTIN6's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without TTYH2 | 0.015 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[C20orf96]] | B | TTYH2 activity raises C20orf96's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without TTYH2 | 0.034 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[NDRG1]] | B | TTYH2 activity lowers NDRG1's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 2.09× higher at baseline in the lines without TTYH2 | 0.058 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[SCMH1]] | B | TTYH2 activity strengthens SCMH1's drug response | lines that do not express TTYH2 (9) vs lines expressing it (41) | the lines without TTYH2 respond 0.79× as strongly (z diff +1.96); strongest at Dinaciclib 5 µM: 0.67x vs 0.46x (z diff +4.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent; artifact flags |
| [[NPTN]] | B | TTYH2 activity lowers NPTN's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.29× higher at baseline in the lines without TTYH2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[HCN2]] | B | TTYH2 activity raises HCN2's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without TTYH2 | 0.096 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, -1.9); signed map (-3.6, 48.9). **Vector** length 63.0, 10.2% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.1 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +21.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +5.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.2 | -1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | tweety family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,213,571-74,262,020 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C17orf29 |
| Gene groups (HGNC) | Tweety family |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSA4](https://www.uniprot.org/uniprotkb/Q9BSA4) (Protein tweety homolog 2):

> Calcium-independent, swelling-dependent volume-regulated anion channel (VRAC-swell) which plays a pivotal role in the process of regulatory volume decrease (RVD) in the brain through the efflux of anions like chloride and organic osmolytes like glutamate (By similarity). Probable large-conductance Ca(2+)-activated chloride channel.

**Summary**, from NCBI Gene [94015](https://www.ncbi.nlm.nih.gov/gene/94015):

> This gene encodes a member of the tweety family of proteins. Members of this family function as chloride anion channels. The encoded protein functions as a calcium(2+)-activated large conductance chloride(-) channel, and may play a role in kidney tumorigenesis. Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13877) · Entrez [94015](https://www.ncbi.nlm.nih.gov/gene/94015) · UniProt [Q9BSA4](https://www.uniprot.org/uniprotkb/Q9BSA4) · Ensembl [ENSG00000141540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141540)

## Data

Gene col 6539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6539); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6539]; `tensor/DDL_lfc|DDL_z.npy` [6539]; `embed/gene_vectors.npy` [6539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6539 or target_col == 6539). Every well: [[TTYH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTYH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
