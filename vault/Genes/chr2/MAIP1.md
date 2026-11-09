---
symbol: "MAIP1"
type: "gene"
col: 8608
ensembl_id: "ENSG00000162972"
name: "matrix AAA peptidase interacting protein 1"
location: "2q33.1"
module: 23
arm: "+"
pooled_cpm: 29.01
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MAIP1

*matrix AAA peptidase interacting protein 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.46× (z +17.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.579× (z -10.9, q 6e-25, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C3orf38]] (+0.77, fdr 2e-05), [[MFF-DT]] (+0.74, fdr 3e-05), [[TP53]] (+0.70, fdr 2e-05); moves opposite to [[GPRIN1]] (-0.64, fdr 6e-05), [[EHD4]] (-0.64, fdr 4e-05), [[KCTD17]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.46×** | +17.6 | 0e+00 | 46/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +17.0 | 0e+00 | 41/48 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +14.0 | 2e-42 | 40/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.29×** | +12.4 | 5e-33 | 39/47 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +10.7 | 8e-25 | 38/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +10.4 | 1e-23 | 39/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +8.1 | 4e-14 | 25/32 (NCI-H1573, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +8.0 | 7e-14 | 35/47 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +7.8 | 6e-13 | 34/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +7.6 | 2e-12 | 34/46 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +7.4 | 6e-12 | 28/48 (CFPAC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +6.9 | 2e-10 | 27/48 (CFPAC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +6.7 | 8e-10 | 23/40 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 5e-09 | 25/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +6.4 | 5e-09 | 27/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +6.0 | 7e-08 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 6e-05 | 21/48 (C-33 A, A549, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 8e-05 | 16/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.57×** | +4.7 | 8e-05 | 17/46 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8608.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -10.9 | 6e-25 | 43/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.623×** | -9.5 | 7e-19 | 40/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -9.0 | 5e-17 | 26/37 (C32, HCT15, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.645×** | -8.8 | 2e-16 | 32/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.717×** | -8.4 | 5e-15 | 37/48 (A-172, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.662×** | -8.3 | 1e-14 | 38/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.769×** | -5.3 | 1e-05 | 19/43 (C32, SW480, …) | rises with dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.709×** | -3.6 | 0.022 | 14/47 (SW48, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.735×** | -3.2 | 0.075 | 9/48 (NCI-H23, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.2 | 0.075 | 12/48 (SW480, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 30.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +15.5) | — |
| [[NCI-H2030 (line)]] | alt | 27.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 28.6 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.98× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 32.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.56× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 23.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +12.7) | — |
| [[LoVo (line)]] | wt | 27.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 34.6 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 34.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 44.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -11.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.9) | — |
| [[A-172 (line)]] | wt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 24.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 39.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 32.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.9) | — |
| [[J82 (line)]] | alt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.2) | — |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0963× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.7) | — |
| [[A-427 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf38]] | +0.77 | +0.79 / +0.47 | both halves | 2e-05 |  |
| [[MFF-DT]] | +0.74 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[TP53]] | +0.70 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[LATS1]] | +0.70 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[YARS2]] | +0.70 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[VPS13B-DT]] | +0.70 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CCDC59]] | +0.70 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[PPP1R42]] | +0.69 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[CNPY2-AS1]] | +0.69 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[PRANCR]] | +0.69 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[TSTD3]] | +0.69 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[AP5M1]] | +0.69 | +0.60 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN1]] | -0.64 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[EHD4]] | -0.64 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[KCTD17]] | -0.62 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[DGKD]] | -0.62 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[MAPK8]] | -0.60 | -0.57 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MAIP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MAIP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-0.7, 17.3); signed map (23.4, -12.8). **Vector** length 99.0, 24.4% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +17.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.4 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.5 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +17.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +12.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -10.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -9.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | +0.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | matrix AAA peptidase interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:199,955,317-200,008,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp666A212, FLJ22555; previously C2orf47 |
| Reactome | 3 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWC4](https://www.uniprot.org/uniprotkb/Q8WWC4) (m-AAA protease-interacting protein 1, mitochondrial):

> Promotes sorting of SMDT1/EMRE in mitochondria by ensuring its maturation. Interacts with the transit peptide region of SMDT1/EMRE precursor protein in the mitochondrial matrix, leading to protect it against protein degradation by YME1L1, thereby ensuring SMDT1/EMRE maturation by the mitochondrial processing peptidase (PMPCA and PMPCB).

**Summary**, from NCBI Gene [79568](https://www.ncbi.nlm.nih.gov/gene/79568):

> Predicted to enable ribosome binding activity. Involved in calcium import into the mitochondrion; mitochondrial calcium ion homeostasis; and protein insertion into mitochondrial membrane. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26198) · Entrez [79568](https://www.ncbi.nlm.nih.gov/gene/79568) · UniProt [Q8WWC4](https://www.uniprot.org/uniprotkb/Q8WWC4) · Ensembl [ENSG00000162972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162972)

## Data

Gene col 8608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8608); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8608]; `tensor/DDL_lfc|DDL_z.npy` [8608]; `embed/gene_vectors.npy` [8608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8608 or target_col == 8608). Every well: [[MAIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
