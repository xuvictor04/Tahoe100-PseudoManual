---
symbol: "SPANXA2-OT1"
type: "gene"
col: 15888
ensembl_id: "ENSG00000277215"
name: "SPANXA2 overlapping transcript 1"
location: "Xq27.2"
module: 19
arm: "+"
pooled_cpm: 18.36
n_lines_expressing: 28
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SPANXA2-OT1

*SPANXA2 overlapping transcript 1* — Xq27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +6.3, q 2e-07, up in 18 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.339× (z -11.3, q 5e-27, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLIT3]] (+0.58, fdr 3e-05), [[LGSN]] (+0.57, fdr 1e-05), [[LINC00648]] (+0.56, fdr 1e-05); moves opposite to [[ABO]] (-0.48, fdr 5e-05), [[TNFRSF14-AS1]] (-0.47, fdr 9e-05), [[PROM1]] (-0.47, fdr 4e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CNTN1]] → it (grade B ⚠); 8 go from it, the strongest it → [[CCDC7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.3 | 2e-07 | 18/26 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.005 | 14/26 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 0.005 | 16/25 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.085 | 13/26 (NCI-H1573, A549, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.36× | +3.2 | 0.15 | 10/26 (Hs 766T, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15888.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.339×** | -11.3 | 5e-27 | 24/26 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.390×** | -9.9 | 1e-20 | 25/26 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.400×** | -9.6 | 2e-19 | 24/26 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.405×** | -9.5 | 4e-19 | 23/26 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.525×** | -9.4 | 7e-19 | 25/25 (A549, NCI-H2030, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.414×** | -8.9 | 6e-17 | 22/25 (A549, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.491×** | -7.5 | 7e-12 | 20/26 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.566×** | -6.0 | 2e-07 | 18/25 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.588×** | -5.6 | 2e-06 | 18/26 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.571×** | -5.6 | 2e-06 | 21/25 (J82, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.597×** | -5.4 | 3e-06 | 18/25 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -5.1 | 1e-05 | 17/21 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.606×** | -4.7 | 1e-04 | 19/26 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -4.5 | 3e-04 | 18/25 (A-427, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -4.2 | 0.001 | 14/26 (NCI-H23, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.672×** | -4.2 | 0.001 | 17/26 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.541×** | -3.4 | 0.024 | 15/25 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.744×** | -3.1 | 0.054 | 10/26 (NCI-H2030, Hs 766T, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.662×** | -3.1 | 0.055 | 9/26 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.578×** | -3.0 | 0.068 | 10/23 (NCI-H23, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 104 | 0 | 19 (13 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0234× (z -27.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0490× (z -23.2) |
| [[A-427 (line)]] | wt | 51.3 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0649× (z -25.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0450× (z -20.7) |
| [[NCI-H2030 (line)]] | alt | 150 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0556× (z -25.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -17.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0689× (z -15.9) |
| [[A549 (line)]] | wt | 45.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0446× (z -25.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0678× (z -16.1) |
| [[HOP62 (line)]] | alt | 30.7 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -13.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0961× (z -12.6) |
| [[A498 (line)]] | wt | 28.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0543× (z -23.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.186× (z -9.8) |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0191× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 43.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -13.0) |
| [[J82 (line)]] | alt | 16.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -10.2) |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0924× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.110× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0220× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 13.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0435× (z -14.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0416× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 7.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -8.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0695× (z -8.6) |
| [[H4 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -9.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 1271 (line)]] | alt | 66.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0558× (z -8.6) |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0470× (z -12.8) |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLIT3]] | +0.58 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[LGSN]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LINC00648]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[FGF14]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[BASP1-AS1]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LRRC63]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[FBXO15]] | +0.54 | +0.55 / +0.41 | both halves | 4e-05 | **novel candidate** |
| [[ODAD2]] | +0.54 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[ZNF287]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[C2orf74-DT]] | +0.52 | +0.51 / +0.37 | both halves | 9e-05 |  |
| [[PRR16]] | +0.52 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[GRAMD1B]] | +0.51 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABO]] | -0.48 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[TNFRSF14-AS1]] | -0.47 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[PROM1]] | -0.47 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[PRR15-DT]] | -0.46 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[IL20RA]] | -0.45 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[VSNL1]] | -0.45 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[KCNE3]] | -0.45 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[FGD5]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[BDH1]] | -0.44 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[PRDM16]] | -0.43 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[PROX1-AS1]] | -0.43 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[ERBB3]] | -0.43 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTN1]] | B | CNTN1 activity raises SPANXA2-OT1's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 1.10× lower at baseline in the lines without CNTN1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9 |
| [[CACNG7]] | B | CACNG7 activity raises SPANXA2-OT1's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without CACNG7 | 0.076 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[LINC01814]] | B | LINC01814 activity lowers SPANXA2-OT1's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 2.51× higher at baseline in the lines without LINC01814 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[GJA1]] | C | GJA1 activity raises SPANXA2-OT1's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 5.06× lower at baseline in the lines without GJA1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[BMPER]] | C | BMPER activity raises SPANXA2-OT1's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.30× lower at baseline in the lines without BMPER | 0.035 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R; co-absent with the target |
| [[NALCN]] | C | NALCN activity raises SPANXA2-OT1's level | lines that do not express NALCN (22) vs lines expressing it (28) | 4.12× lower at baseline in the lines without NALCN | 0.036 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[TRIM9]] | C | TRIM9 activity raises SPANXA2-OT1's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 4.23× lower at baseline in the lines without TRIM9 | 0.045 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[MSRB3]] | C | MSRB3 activity raises SPANXA2-OT1's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 3.13× lower at baseline in the lines without MSRB3 | 0.058 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1; co-absent with the target |
| [[LDOC1]] | C | LDOC1 activity raises SPANXA2-OT1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 7.02× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC7]] | B | SPANXA2-OT1 activity raises CCDC7's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without SPANXA2-OT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | SPANXA2-OT1 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (26) | the lines without SPANXA2-OT1: 0.99× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3 |
| [[LDOC1]] | C | SPANXA2-OT1 activity raises LDOC1's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 6.67× lower at baseline in the lines without SPANXA2-OT1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3; co-absent with the target |
| [[EHD3]] | C | SPANXA2-OT1 activity raises EHD3's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 2.68× lower at baseline in the lines without SPANXA2-OT1 | 0.041 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3; co-absent with the target |
| [[BMPER]] | C | SPANXA2-OT1 activity raises BMPER's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 3.69× lower at baseline in the lines without SPANXA2-OT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3; co-absent with the target |
| [[VEGFC]] | C | SPANXA2-OT1 activity raises VEGFC's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 5.49× lower at baseline in the lines without SPANXA2-OT1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3; co-absent with the target |
| [[MIR646HG]] | C | SPANXA2-OT1 activity raises MIR646HG's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without SPANXA2-OT1 | 0.096 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3; co-absent with the target |
| [[TWIST2]] | C | SPANXA2-OT1 activity raises TWIST2's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 5.71× lower at baseline in the lines without SPANXA2-OT1 | 0.099 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.414). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.3, 37.9); signed map (38.4, 41.6). **Vector** length 78.8, 23.1% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.7 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.9 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -11.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -0.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SPANXA2 overlapping transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq27.2 — chrX:141,177,284-141,649,927 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ36186; previously CXorf18 |
| Gene groups (HGNC) | Overlapping transcripts |
| Matched by | ensembl_id |

UniProt [Q8N9U9](https://www.uniprot.org/uniprotkb/Q8N9U9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31683) · Entrez [619455](https://www.ncbi.nlm.nih.gov/gene/619455) · UniProt [Q8N9U9](https://www.uniprot.org/uniprotkb/Q8N9U9) · Ensembl [ENSG00000277215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277215)

## Data

Gene col 15888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15888); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15888]; `tensor/DDL_lfc|DDL_z.npy` [15888]; `embed/gene_vectors.npy` [15888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15888 or target_col == 15888). Every well: [[SPANXA2-OT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPANXA2-OT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
