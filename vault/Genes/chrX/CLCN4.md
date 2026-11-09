---
symbol: "CLCN4"
type: "gene"
col: 1050
ensembl_id: "ENSG00000073464"
name: "Cl-/H+ antiporter 4"
location: "Xp22.2"
module: 47
arm: "+"
pooled_cpm: 5.34
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 21
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 9
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CLCN4

*Cl-/H+ antiporter 4* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.86× (z +14.7, q 0e+00, up in 28 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.601× (z -5.1, q 2e-04, down in 16 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01776]] (+0.60, fdr 1e-05), [[ITPR2-AS1]] (+0.60, fdr 4e-05), [[LINC01934]] (+0.59, fdr 1e-05); moves opposite to [[SDHAP2]] (-0.58, fdr 3e-05), [[SDHAP1]] (-0.57, fdr 5e-05), [[RNF149]] (-0.54, fdr 4e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 9 go from it, the strongest it → [[CCN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +14.7 | 0e+00 | 28/35 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.47×** | +12.3 | 2e-32 | 29/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +11.7 | 3e-29 | 26/37 (NCI-H1792, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.03×** | +11.0 | 7e-26 | 25/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.5 | 3e-19 | 9/13 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +8.5 | 2e-15 | 24/41 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +8.3 | 7e-15 | 24/40 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.29×** | +8.2 | 2e-14 | 24/40 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +7.0 | 2e-10 | 19/35 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.95×** | +6.6 | 2e-09 | 19/40 (HOP62, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.91×** | +6.4 | 7e-09 | 13/22 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +5.7 | 5e-07 | 18/37 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.7 | 6e-07 | 14/41 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +5.3 | 4e-06 | 17/39 (A-172, NCI-H1792, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.74×** | +5.1 | 2e-05 | 10/18 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +4.8 | 5e-05 | 17/36 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.50×** | +4.8 | 7e-05 | 11/37 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.7 | 9e-05 | 16/39 (HOP62, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.601×** | -5.1 | 2e-04 | 16/39 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.635×** | -4.5 | 0.002 | 15/39 (RPMI-7951, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.652×** | -4.3 | 0.003 | 13/40 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -4.3 | 0.003 | 16/39 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -3.9 | 0.011 | 16/40 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.689×** | -3.7 | 0.019 | 12/32 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.697×** | -3.5 | 0.044 | 7/40 (BT-474, A-172, …) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.707×** | -3.3 | 0.063 | 9/38 (H4, A-427, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.720× | -3.2 | 0.10 | 9/40 (A-172, LoVo, …) | top dose only | plate-row cell shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.649× | -3.1 | 0.12 | 6/41 (NCI-H460, Hs 766T, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +14.2) | — |
| [[NCI-H1792 (line)]] | alt | 6.75 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 15.4× (z +9.6) | [[Saquinavir (drug)]] 0.05 µM 0.0767× (z -9.1) |
| [[PANC-1 (line)]] | alt | 4.44 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 9.87× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.0444× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.131× (z -8.5) |
| [[J82 (line)]] | alt | 3.77 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 8.11 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +10.2) | [[Digitoxin (drug)]] 0.5 µM 0.153× (z -10.3) |
| [[SW480 (line)]] | alt | 6.98 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.162× (z -9.8) |
| [[KATO III (line)]] | alt | 22.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0788× (z -15.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0990× (z -9.2) |
| [[HOP62 (line)]] | alt | 3.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 5.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 2.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 4.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 7.30 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.107× (z -8.6) |
| [[A498 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.934 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01776]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | +0.60 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[LINC01934]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[DYNLRB2-AS1]] | +0.58 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[ALPK2]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[DGKI]] | +0.57 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CALD1]] | +0.56 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[AMOTL2]] | +0.56 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[CUBN]] | +0.56 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.55 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FSIP1]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SYNE1]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP2]] | -0.58 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[SDHAP1]] | -0.57 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[RNF149]] | -0.54 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[HSPB11]] | -0.54 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[ZNF250]] | -0.53 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[PMS2P3-1]] | -0.53 | -0.66 / -0.36 | both halves | 9e-05 |  |
| [[PRKRA]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ECI2]] | -0.53 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.51 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[SNHG30]] | -0.50 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[CBFA2T2]] | -0.50 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[LCMT1]] | -0.50 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN1]] | B | CLCN4 activity lowers CCN1's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 3.16× higher at baseline in the lines without CLCN4 | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SDHAP4]] | B | CLCN4 activity raises SDHAP4's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without CLCN4 | 0.010 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[THOC6]] | B | CLCN4 activity lowers THOC6's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 1.51× higher at baseline in the lines without CLCN4 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DDAH1]] | B | CLCN4 activity strengthens DDAH1's drug response | lines that do not express CLCN4 (7) vs lines expressing it (39) | the lines without CLCN4 respond 0.46× as strongly (z diff +1.56); strongest at Homoharringtonine 5 µM: 1.02x vs 1.57x (z diff +5.6) | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[LINC02516]] | B | CLCN4 activity lowers LINC02516's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 2.34× higher at baseline in the lines without CLCN4 | 0.054 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CCN1]] | B | CLCN4 activity weakens CCN1's drug response | lines that do not express CLCN4 (7) vs lines expressing it (36) | the lines without CLCN4 respond 1.28× as strongly (z diff -0.95); strongest at c-Kit-IN-1 0.05 µM: 0.22x vs 0.54x (z diff -4.4) | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[AOX1]] | B | CLCN4 activity lowers AOX1's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 2.19× higher at baseline in the lines without CLCN4 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DDAH1]] | B | CLCN4 activity lowers DDAH1's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 2.06× higher at baseline in the lines without CLCN4 | 0.065 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM51]] | B | CLCN4 activity raises TMEM51's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 1.85× lower at baseline in the lines without CLCN4 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -9.0); signed map (24.5, 12.0). **Vector** length 60.5, 9.12% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | Cl-/H+ antiporter 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:10,156,975-10,237,660 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLC4, ClC-4 |
| Gene groups (HGNC) | CLC chloride channel and transporter family |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P51793](https://www.uniprot.org/uniprotkb/P51793) (H(+)/Cl(-) exchange transporter 4):

> Strongly outwardly rectifying, electrogenic H(+)/Cl(-)exchanger which mediates the exchange of chloride ions against protons. The CLC channel family contains both chloride channels and proton-coupled anion transporters that exchange chloride or another anion for protons. The presence of conserved gating glutamate residues is typical for family members that function as antiporters.

**Summary**, from NCBI Gene [1183](https://www.ncbi.nlm.nih.gov/gene/1183):

> The CLCN family of voltage-dependent chloride channel genes comprises nine members (CLCN1-7, Ka and Kb) which demonstrate quite diverse functional characteristics while sharing significant sequence homology. Chloride channel 4 has an evolutionary conserved CpG island and is conserved in both mouse and hamster. This gene is mapped in close proximity to APXL (Apical protein Xenopus laevis-like) and OA1 (Ocular albinism type I), which are both located on the human X chromosome at band p22.3. The …

**Accessions** — [HGNC:2022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2022) · Entrez [1183](https://www.ncbi.nlm.nih.gov/gene/1183) · UniProt [P51793](https://www.uniprot.org/uniprotkb/P51793) · Ensembl [ENSG00000073464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073464)

## Data

Gene col 1050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1050); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1050]; `tensor/DDL_lfc|DDL_z.npy` [1050]; `embed/gene_vectors.npy` [1050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1050 or target_col == 1050). Every well: [[CLCN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLCN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
