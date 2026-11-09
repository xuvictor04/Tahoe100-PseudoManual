---
symbol: "SOGA3"
type: "gene"
col: 13196
ensembl_id: "ENSG00000214338"
name: "MTCL family member 3"
location: "6q22.33"
module: 82
arm: "+"
pooled_cpm: 11.98
n_lines_expressing: 29
n_dd_up: 30
n_dd_down: 11
n_dd_up_clean: 29
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 15
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# SOGA3

*MTCL family member 3* — 6q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +12.7, q 3e-34, up in 20 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.592× (z -7.3, q 2e-10, down in 14 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA0408]] (+0.91, fdr 7e-06, ⚠ same locus), [[JAKMIP2]] (+0.62, fdr 3e-04), [[RBM11]] (+0.57, fdr 1e-05), [[NFASC]] (+0.57, fdr 2e-05); moves opposite to [[LEMD3]] (-0.54, fdr 3e-05), [[TRPV1]] (-0.54, fdr 2e-04), [[PSKH1]] (-0.53, fdr 1e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 15 go from it, the strongest it → [[TTLL7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 1 with an alert ⚠; shown: the 15 strongest. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +12.7 | 3e-34 | 20/27 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.05×** | +10.0 | 5e-21 | 21/27 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +9.6 | 1e-19 | 17/27 (HOP62, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +8.6 | 8e-16 | 16/27 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +8.1 | 5e-14 | 21/27 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +7.9 | 4e-13 | 18/27 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +7.6 | 3e-12 | 13/26 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.68×** | +7.2 | 3e-11 | 16/27 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +6.9 | 4e-10 | 17/26 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +6.9 | 4e-10 | 15/27 (A-172, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +6.7 | 1e-09 | 14/27 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +5.3 | 7e-06 | 13/26 (A549, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +5.2 | 9e-06 | 10/25 (A549, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 1e-05 | 13/27 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +5.1 | 1e-05 | 9/26 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.592×** | -7.3 | 2e-10 | 14/26 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -6.7 | 3e-09 | 14/26 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.615×** | -6.7 | 3e-09 | 14/27 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -6.3 | 5e-08 | 14/27 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -5.7 | 1e-06 | 15/25 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -4.4 | 9e-04 | 4/27 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -4.3 | 0.001 | 13/26 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -4.2 | 0.002 | 9/27 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.754×** | -3.9 | 0.006 | 9/26 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -3.8 | 0.007 | 10/26 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.589×** | -3.8 | 0.007 | 9/25 (HOP62, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.792×** | -3.1 | 0.094 | 8/24 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.39 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.22× (z +10.7) | — |
| [[A-172 (line)]] | wt | 14.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -8.8) |
| [[HOP62 (line)]] | alt | 22.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.22× (z +8.8) | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -10.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 108 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.276× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -11.0) |
| [[A-427 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.963 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.996 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0408]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | STRING 715; ⚠ same locus (13.4 kb, same strand: neighbours can correlate without regulation) |
| [[JAKMIP2]] | +0.62 | +0.29 / +0.68 | both halves | 3e-04 |  |
| [[RBM11]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[NFASC]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[WDR17]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[TBC1D19]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[RNF180]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[RPAP3]] | +0.54 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZSCAN12]] | +0.54 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[MAP6]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[CCDC112]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PAK1]] | +0.52 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CYRIA]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEMD3]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TRPV1]] | -0.54 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[PSKH1]] | -0.53 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[MIATNB]] | -0.52 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[TNXB]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TNRC18]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TMEM11-DT]] | -0.50 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[ANKMY1]] | -0.50 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SMUG1]] | -0.49 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[UBAP1L]] | -0.49 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[CRYGS]] | -0.48 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[ARIH2]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SOGA3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TTLL7]] | B | TTLL7 activity raises SOGA3's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 4.77× lower at baseline in the lines without TTLL7 | 0.047 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[JAZF1]] | B | JAZF1 activity raises SOGA3's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 4.49× lower at baseline in the lines without JAZF1 | 0.058 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[SPEG]] | B | SPEG activity raises SOGA3's level | lines that do not express SPEG (16) vs lines expressing it (34) | 3.86× lower at baseline in the lines without SPEG | 0.059 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[KIAA0408]] | C | KIAA0408 activity raises SOGA3's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 7.83× lower at baseline in the lines without KIAA0408 | 5e-05 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises SOGA3's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.68× lower at baseline in the lines without MAP1A | 0.049 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[CCNYL2]], [[CCNYL2-1]] | C | CCNYL2, CCNYL2-1 activity raises SOGA3's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 4.35× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[WDR17]] | C | WDR17 activity raises SOGA3's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 4.76× lower at baseline in the lines without WDR17 | 0.075 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 9, C 6. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTLL7]] | B | SOGA3 activity raises TTLL7's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 3.83× lower at baseline in the lines without SOGA3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[ZNF22]] | B | SOGA3 activity raises ZNF22's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.61× lower at baseline in the lines without SOGA3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[SPEG]] | B | SOGA3 activity raises SPEG's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 2.90× lower at baseline in the lines without SOGA3 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[ZSCAN26]] | B | SOGA3 activity raises ZSCAN26's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.30× lower at baseline in the lines without SOGA3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[COMMD8]] | B | SOGA3 activity raises COMMD8's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.26× lower at baseline in the lines without SOGA3 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[NXPE3]] | B | SOGA3 activity raises NXPE3's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 2.18× lower at baseline in the lines without SOGA3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[MSANTD4]] | B | SOGA3 activity raises MSANTD4's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without SOGA3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[COMMD2]] | B | SOGA3 activity raises COMMD2's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.25× lower at baseline in the lines without SOGA3 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[FYTTD1]] | B | SOGA3 activity raises FYTTD1's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.12× lower at baseline in the lines without SOGA3 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[KIAA0408]] | C | SOGA3 activity raises KIAA0408's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 7.64× lower at baseline in the lines without SOGA3 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1; co-absent with the target |
| [[ZSCAN12]] | C | SOGA3 activity raises ZSCAN12's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 2.91× lower at baseline in the lines without SOGA3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1; co-absent with the target |
| [[WDR17]] | C | SOGA3 activity raises WDR17's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 3.31× lower at baseline in the lines without SOGA3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, 34.2); signed map (34.6, 32.5). **Vector** length 63.5, 14.1% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +8.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +4.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -6.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -7.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -4.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | MTCL family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.33 — chr6:127,472,806-127,519,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ403A15.3; previously C6orf174, SOGA3 |
| Matched by | ensembl_id |

UniProt [Q5TF21](https://www.uniprot.org/uniprotkb/Q5TF21) carries no function annotation.

**Summary**, from NCBI Gene [387104](https://www.ncbi.nlm.nih.gov/gene/387104):

> Predicted to be involved in regulation of autophagy. Predicted to be located in membrane and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21494) · Entrez [387104](https://www.ncbi.nlm.nih.gov/gene/387104) · UniProt [Q5TF21](https://www.uniprot.org/uniprotkb/Q5TF21) · Ensembl [ENSG00000214338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214338)

## Data

Gene col 13196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13196); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13196]; `tensor/DDL_lfc|DDL_z.npy` [13196]; `embed/gene_vectors.npy` [13196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13196 or target_col == 13196). Every well: [[SOGA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOGA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
