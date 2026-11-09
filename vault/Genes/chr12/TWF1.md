---
symbol: "TWF1"
type: "gene"
col: 7498
ensembl_id: "ENSG00000151239"
name: "twinfilin actin binding protein 1"
location: "12q12"
module: 25
arm: "+"
pooled_cpm: 65.83
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TWF1

*twinfilin actin binding protein 1* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.31× (z +11.1, q 1e-25, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.49× (z +5.4, q 7e-06, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.853× (z -7.2, q 3e-10, down in 13 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.519× (z -6.1, q 3e-07, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN7C]] (+0.79, fdr 7e-06), [[MOB1A]] (+0.76, fdr 7e-06), [[AP2M1]] (+0.76, fdr 7e-06); moves opposite to [[NSUN5P1-1]] (-0.72, fdr 1e-05), [[RPL36AL]] (-0.70, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[NSUN5P2-1]] (-0.68, fdr 3e-05, ⚠ NSUN5P2-1 in the vector space only through flagged drug-doses), [[INAFM1]] (-0.67, fdr 1e-05), [[TMEM258]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AKT1]], [[AKT2]], [[AKT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +11.1 | 1e-25 | 41/44 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +10.5 | 3e-23 | 44/49 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +8.2 | 5e-14 | 40/45 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 7e-06 | 36/48 (HOP62, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.31×** | +5.2 | 2e-05 | 22/48 (AsPC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +4.9 | 7e-05 | 35/49 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.3 | 0.002 | 32/48 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.002 | 29/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +3.9 | 0.007 | 24/48 (NCI-H2347, A498, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.6 | 0.016 | 24/47 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.016 | 28/48 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.31×** | +3.6 | 0.016 | 24/47 (A498, COLO 205, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.020 | 30/48 (NCI-H460, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.038 | 23/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.038 | 22/48 (CFPAC-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.060 | 21/48 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.063 | 21/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.853× | -7.2 | 3e-10 | 13/49 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.519×** | -6.1 | 3e-07 | 42/48 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.597×** | -4.8 | 3e-04 | 39/48 (HT-29, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.647×** | -4.0 | 0.007 | 31/48 (Hs 766T, AN3 CA, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.683×** | -3.5 | 0.045 | 25/48 (RKO, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -3.3 | 0.096 | 18/48 (NCI-H1573, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 43.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +10.9) ⚠ toxic; transcription drop | [[Adagrasib (drug)]] 0.05 µM 0.660× (z -10.9) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 63.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 62.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 44.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 89.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 49.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 49.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 67.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.87× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 45.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 74.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 66.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +12.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 73.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +9.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 82.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.0) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[NCI-H661 (line)]] | alt | 71.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0895× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 70.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 59.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.72× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 83.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -8.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A549 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.76 | +0.61 / +0.85 | both halves | 7e-06 |  |
| [[AP2M1]] | +0.76 | +0.70 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[EIF4H]] | +0.76 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[AKAP11]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[CAPRIN1]] | +0.72 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[EIF4G2]] | +0.72 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[NRAS]] | +0.70 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[ZNF664]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.69 | +0.49 / +0.85 | both halves | 1e-05 |  |
| [[DR1]] | +0.69 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[UBQLN1]] | +0.68 | +0.57 / +0.71 | both halves | 9e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5P1-1]] | -0.72 | -0.50 / -0.80 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.70 | -0.55 / -0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P2-1]] ⚠ | -0.68 | -0.43 / -0.74 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[INAFM1]] | -0.67 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.67 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[RPL36]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.66 | -0.51 / -0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG19]] | -0.66 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[C19orf81]] | -0.66 | -0.47 / -0.70 | both halves | 2e-05 |  |
| [[ZBTB7A]] | -0.65 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.65 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[ATP5ME]] | -0.65 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[SNHG9]] | -0.65 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[COX6B1]] | -0.64 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[MRPL23]] | -0.64 | -0.46 / -0.66 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKT1]], [[AKT2]], [[AKT3]] | B | AKT1, AKT2, AKT3 activity raises TWF1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SCOC]] | C | SCOC activity lowers TWF1's level | lines that do not express SCOC (4) vs lines expressing it (46) | 1.67× higher at baseline in the lines without SCOC | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.819). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.7, -21.2); signed map (-17.0, -37.7). **Vector** length 125, 40.5% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +5.4 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +3.7 | +2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +3.3 | +2.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +3.3 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +3.1 | +1.7 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -7.5 | -6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | -0.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -4.6 | -4.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -4.5 | -3.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -4.5 | -4.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | twinfilin actin binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:43,793,723-43,806,328 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A6; previously PTK9 |
| Gene groups (HGNC) | Twinfilin actin binding protein family |
| Reactome | 9 pathways, smallest: RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle; Sensory processing of sound by outer hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12792](https://www.uniprot.org/uniprotkb/Q12792) (Twinfilin-1):

> Actin-binding protein involved in motile and morphological processes. Inhibits actin polymerization, likely by sequestering G-actin. By capping the barbed ends of filaments, it also regulates motility. Seems to play an important role in clathrin-mediated endocytosis and distribution of endocytic organelles (By similarity).

**Summary**, from NCBI Gene [5756](https://www.ncbi.nlm.nih.gov/gene/5756):

> This gene encodes twinfilin, an actin monomer-binding protein conserved from yeast to mammals. Studies of the mouse counterpart suggest that this protein may be an actin monomer-binding protein, and its localization to cortical G-actin-rich structures may be regulated by the small GTPase RAC1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9620) · Entrez [5756](https://www.ncbi.nlm.nih.gov/gene/5756) · UniProt [Q12792](https://www.uniprot.org/uniprotkb/Q12792) · Ensembl [ENSG00000151239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151239)

## Data

Gene col 7498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7498); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7498]; `tensor/DDL_lfc|DDL_z.npy` [7498]; `embed/gene_vectors.npy` [7498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7498 or target_col == 7498). Every well: [[TWF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TWF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
