---
symbol: "TMEM178B"
type: "gene"
col: 15326
ensembl_id: "ENSG00000261115"
name: "transmembrane protein 178B"
location: "7q34"
module: 152
arm: "+"
pooled_cpm: 75.24
n_lines_expressing: 28
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 12
direction_downstream: 10
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# TMEM178B

*transmembrane protein 178B* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +16.8, q 0e+00, up in 9 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.605× (z -9.8, q 6e-20, down in 15 of 26 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGFBP5]] (+0.59, fdr 3e-05), [[RARB]] (+0.58, fdr 4e-05), [[SFMBT2]] (+0.56, fdr 2e-05); moves opposite to [[PTPDC1]] (-0.44, fdr 8e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[ZNF521]] → it (grade B ⚠); 10 go from it, the strongest it → [[LINC02506]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +16.8 | 0e+00 | 9/27 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +15.8 | 0e+00 | 11/26 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +12.1 | 3e-31 | 16/26 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +8.2 | 3e-14 | 16/26 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +7.2 | 9e-11 | 15/27 (NCI-H23, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +7.1 | 2e-10 | 9/27 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +6.4 | 1e-08 | 13/26 (A498, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.2 | 3e-08 | 5/28 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +5.0 | 4e-05 | 11/25 (A549, HS-578T, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +4.9 | 4e-05 | 9/26 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 1/27 (NCI-H1573) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +4.5 | 4e-04 | 10/27 (SNU-423, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 7/27 (A549, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +3.7 | 0.010 | 8/25 (A498, A549, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.010 | 7/26 (A549, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.033 | 5/27 (NCI-H460, SW 900, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -9.8 | 6e-20 | 15/26 (BT-474, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.718×** | -6.4 | 3e-08 | 19/24 (BT-474, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.726×** | -6.2 | 8e-08 | 17/26 (BT-474, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.738×** | -5.9 | 4e-07 | 12/26 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.717×** | -5.8 | 6e-07 | 9/25 (HS-578T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.783×** | -4.8 | 2e-04 | 12/25 (SNU-423, RPMI-7951, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.795×** | -4.5 | 6e-04 | 12/26 (C32, RPMI-7951, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.649×** | -4.4 | 7e-04 | 8/26 (C32, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **0.798×** | -4.4 | 7e-04 | 10/26 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.799×** | -4.4 | 7e-04 | 7/26 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.802×** | -4.3 | 9e-04 | 8/26 (C32, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -4.3 | 9e-04 | 17/26 (RPMI-7951, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.807×** | -4.2 | 0.001 | 11/26 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.805×** | -4.1 | 0.002 | 16/24 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.868× | -3.9 | 0.004 | 13/27 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.816×** | -3.8 | 0.005 | 8/26 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.693×** | -3.7 | 0.006 | 9/24 (SW 900, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.007 | 10/26 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Decitabine (drug)]] 0.5 µM |  | **0.829×** | -3.6 | 0.008 | 10/26 (NCI-H23, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 692 | 0 | 23 (14 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.190× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 632 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0786× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0909× (z -15.9) |
| [[SHP-77 (line)]] | alt | 270 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.290× (z -13.5) |
| [[A-172 (line)]] | wt | 34.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +20.4) | — |
| [[BT-474 (line)]] | alt | 166 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.213× (z -13.4) |
| [[C-33 A (line)]] | alt | 187 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0470× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 295 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0507× (z -11.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.227× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 156 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -11.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 32.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 4.44× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -9.7) |
| [[SNU-423 (line)]] | alt | 172 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 166 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 102 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.6) | — |
| [[H4 (line)]] | wt | 20.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +12.6) | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0725× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 33.0 | 0 | 2 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.250× (z -9.2) |
| [[A549 (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 45.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 55.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 105 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.233× (z -8.8) |
| [[A-427 (line)]] | wt | 8.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.25 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.82 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.86 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.51 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP5]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 | **novel candidate** |
| [[RARB]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[SFMBT2]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[PTPRD]] | +0.55 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[PI15]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MEIS1]] | +0.55 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PDE10A]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 | **novel candidate** |
| [[ST8SIA4]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[LRP2]] | +0.53 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[NREP]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[HMCN1]] | +0.52 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[EYA1]] | +0.52 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPDC1]] | -0.44 | -0.41 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF521]] | B | ZNF521 activity weakens TMEM178B's drug response | lines that do not express ZNF521 (12) vs lines expressing it (15) | the lines without ZNF521 respond 2.78× as strongly (z diff -2.17); rises at some drug-doses, falls at others (71% from rises): Idarubicin (hydrochloride) 5 µM: 1.24x vs 0.84x (z diff -3.7); Panobinostat 5 µM: 1.56x vs 0.99x (z diff -3.3); Ouabain (Octahydrate) 5 µM: 0.44x vs 0.65x (z diff -3.2) | 0.046 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[MAN1C1]] | B | MAN1C1 activity raises TMEM178B's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 3.41× lower at baseline in the lines without MAN1C1 | 0.090 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TMEM178B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GPRIN3]] | B | GPRIN3 activity raises TMEM178B's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.42× lower at baseline in the lines without GPRIN3 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[NELL1]] | C | NELL1 activity raises TMEM178B's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without NELL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises TMEM178B's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.37× lower at baseline in the lines without KCNE4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[SETBP1]] | C | SETBP1 activity raises TMEM178B's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.05× lower at baseline in the lines without SETBP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises TMEM178B's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 3.47× lower at baseline in the lines without IGFBP5 | 0.029 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[TEX41]] | C | TEX41 activity raises TMEM178B's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 4.02× lower at baseline in the lines without TEX41 | 0.030 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |
| [[RARB]] | C | RARB activity raises TMEM178B's level | lines that do not express RARB (28) vs lines expressing it (22) | 4.46× lower at baseline in the lines without RARB | 0.073 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |
| [[ZMAT4]] | C | ZMAT4 activity raises TMEM178B's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without ZMAT4 | 0.083 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[SNAP25]] | C | SNAP25 activity raises TMEM178B's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without SNAP25 | 0.086 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02506]] | B | TMEM178B activity raises LINC02506's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 1.95× lower at baseline in the lines without TMEM178B | 0.048 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2 |
| [[ATRNL1]] | B | TMEM178B activity raises ATRNL1's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without TMEM178B | 0.049 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2 |
| [[SEMA6D]] | B | TMEM178B activity raises SEMA6D's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 1.55× lower at baseline in the lines without TMEM178B | 0.060 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2 |
| [[RNF150]] | B | TMEM178B activity raises RNF150's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without TMEM178B | 0.064 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2 |
| [[PDE3A]] | B | TMEM178B activity raises PDE3A's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 2.08× lower at baseline in the lines without TMEM178B | 0.096 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2 |
| [[TEX41]] | C | TMEM178B activity raises TEX41's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 4.82× lower at baseline in the lines without TMEM178B | 0.014 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2; co-absent with the target |
| [[EBF1]] | C | TMEM178B activity raises EBF1's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 3.54× lower at baseline in the lines without TMEM178B | 0.026 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2; co-absent with the target |
| [[BAALC]] | C | TMEM178B activity raises BAALC's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 2.38× lower at baseline in the lines without TMEM178B | 0.027 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2; co-absent with the target |
| [[KCNE4]] | C | TMEM178B activity raises KCNE4's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without TMEM178B | 0.041 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2; co-absent with the target |
| [[NREP]] | C | TMEM178B activity raises NREP's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 2.38× lower at baseline in the lines without TMEM178B | 0.055 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.5, 29.9); signed map (37.9, 39.5). **Vector** length 75.3, 17.4% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.4 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.9 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.9 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | -0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +5.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.2 | -5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.0 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 178B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:141,074,064-141,480,380 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp547G036 |
| Matched by | ensembl_id |

UniProt [H3BS89](https://www.uniprot.org/uniprotkb/H3BS89) carries no function annotation.

**Summary**, from NCBI Gene [100507421](https://www.ncbi.nlm.nih.gov/gene/100507421):

> Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:44112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44112) · Entrez [100507421](https://www.ncbi.nlm.nih.gov/gene/100507421) · UniProt [H3BS89](https://www.uniprot.org/uniprotkb/H3BS89) · Ensembl [ENSG00000261115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261115)

## Data

Gene col 15326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15326); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15326]; `tensor/DDL_lfc|DDL_z.npy` [15326]; `embed/gene_vectors.npy` [15326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15326 or target_col == 15326). Every well: [[TMEM178B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM178B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
