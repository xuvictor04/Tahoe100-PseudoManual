---
symbol: "AFG3L1P"
type: "gene"
col: 13371
ensembl_id: "ENSG00000223959"
name: "AFG3 like matrix AAA peptidase subunit 1, pseudogene"
location: "16q24.3"
module: 88
arm: "+"
pooled_cpm: 20.88
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# AFG3L1P

*AFG3 like matrix AAA peptidase subunit 1, pseudogene* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +21.2, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.635× (z -8.3, q 6e-14, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTG2]] (+0.75, fdr 7e-06), [[FKRP]] (+0.70, fdr 3e-05), [[FIZ1]] (+0.70, fdr 3e-05); moves opposite to [[PPP1R2]] (-0.63, fdr 1e-05), [[LTA4H]] (-0.62, fdr 1e-05), [[SLC25A23]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +21.2 | 0e+00 | 40/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +12.9 | 2e-35 | 34/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +12.8 | 2e-35 | 36/47 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +9.6 | 8e-20 | 29/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +5.9 | 3e-07 | 25/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +5.9 | 4e-07 | 19/40 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +5.7 | 8e-07 | 21/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +4.7 | 2e-04 | 15/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.8 | 0.009 | 14/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.044 | 20/47 (HepG2/C3A, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.044 | 9/48 (SW 900, COLO 205, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.044 | 9/45 (NCI-H460, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.081 | 6/46 (HepG2/C3A, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.081 | 7/45 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.081 | 2/45 (PANC-1, HT-29) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.635×** | -8.3 | 6e-14 | 28/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -8.0 | 3e-13 | 30/48 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.669×** | -7.4 | 4e-11 | 27/48 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.709×** | -6.3 | 4e-08 | 24/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.715×** | -6.1 | 9e-08 | 23/46 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -4.8 | 1e-04 | 16/48 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.627×** | -4.5 | 6e-04 | 16/46 (SNU-1, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.643×** | -4.2 | 0.002 | 15/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.810×** | -3.9 | 0.007 | 9/48 (KATO III, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.813×** | -3.8 | 0.008 | 15/48 (PANC-1, NCI-H460, …) | top dose only | composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.017 | 13/47 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.4 | 0.031 | 16/48 (AsPC-1, A-427, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.2 | 0.063 | 8/46 (SK-MEL-2, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.4 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +18.1) | [[Belinostat (drug)]] 5 µM 0.340× (z -11.2) |
| [[SW480 (line)]] | alt | 22.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +19.0) | — |
| [[NCI-H460 (line)]] | wt | 25.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +25.1) | [[Digitoxin (drug)]] 5 µM 0.285× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 22.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +18.4) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 21.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.233× (z -10.8) |
| [[LoVo (line)]] | wt | 15.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +36.0) | — |
| [[SW48 (line)]] | wt | 17.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +12.6) | — |
| [[A-172 (line)]] | wt | 23.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.302× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.317× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 15.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.116× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.21× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +20.2) | — |
| [[NCI-H1792 (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +19.9) | — |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -11.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 32.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.37× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 1 | — | [[Brivudine (drug)]] 5 µM 0.0567× (z -8.5) |
| [[SNU-423 (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +9.5) | — |
| [[A-427 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTG2]] | +0.75 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[FKRP]] | +0.70 | +0.75 / +0.43 | both halves | 3e-05 |  |
| [[FIZ1]] | +0.70 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[BRD1]] | +0.69 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ST7L]] | +0.67 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[LTO1]] | +0.67 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[EXOSC6]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RNASEH1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[GMEB2]] | +0.64 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PEF1]] | +0.63 | +0.64 / +0.37 | both halves | 9e-05 |  |
| [[PPP1R3F]] | +0.63 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[ALDH16A1]] | +0.63 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R2]] | -0.63 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[LTA4H]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[SLC25A23]] | -0.61 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[STRN]] | -0.61 | -0.63 / -0.37 | both halves | 7e-05 |  |
| [[GM2A]] | -0.61 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[HERC3]] | -0.60 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[FHIP1A]] | -0.60 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[ORC4]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 | same gene group |
| [[MOSPD3]] | -0.59 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[NPTN]] | -0.59 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[ARL3]] | -0.58 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[PJA2]] | -0.58 | -0.63 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity lowers AFG3L1P's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.45× higher at baseline in the lines without ADD3 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[NR3C2]] | B | NR3C2 activity lowers AFG3L1P's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.35× higher at baseline in the lines without NR3C2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-8.2, 5.7); signed map (19.2, -25.8). **Vector** length 104, 23.3% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.8 | +21.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.3 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +12.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -5.4 | -8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.8 | -2.2 |
|  | [[Aliskiren (drug)]] 0.5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | AFG3 like matrix AAA peptidase subunit 1, pseudogene |
| Locus type | pseudogene |
| Location | 16q24.3 — chr16:89,972,631-90,000,668 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ; previously AFG3, AFG3L1 |
| Gene groups (HGNC) | AAA ATPases; Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [172](https://www.ncbi.nlm.nih.gov/gene/172):

> Predicted to be involved in protein processing. Predicted to act upstream of or within cristae formation; mitochondrial fusion; and mitochondrial protein processing. Predicted to be located in mitochondrial inner membrane. Predicted to be part of m-AAA complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:314) · Entrez [172](https://www.ncbi.nlm.nih.gov/gene/172) · Ensembl [ENSG00000223959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223959)

## Data

Gene col 13371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13371); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13371]; `tensor/DDL_lfc|DDL_z.npy` [13371]; `embed/gene_vectors.npy` [13371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13371 or target_col == 13371). Every well: [[AFG3L1P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFG3L1P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
