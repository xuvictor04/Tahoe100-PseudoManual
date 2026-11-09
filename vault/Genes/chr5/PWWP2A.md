---
symbol: "PWWP2A"
type: "gene"
col: 9917
ensembl_id: "ENSG00000170234"
name: "PWWP domain containing 2A"
location: "5q33.3"
module: 57
arm: "-"
pooled_cpm: 61.67
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# PWWP2A

*PWWP domain containing 2A* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +11.3, q 6e-27, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.606× (z -13.2, q 5e-37, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD7]] (+0.63, fdr 1e-05), [[ASH1L]] (+0.57, fdr 7e-05), [[HIVEP1]] (+0.53, fdr 2e-05); moves opposite to [[STARD3NL]] (-0.57, fdr 1e-05), [[VAMP7]] (-0.56, fdr 8e-05), [[ATP2C1]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +11.3 | 6e-27 | 33/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +8.9 | 1e-16 | 29/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.5 | 4e-15 | 30/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +8.2 | 5e-14 | 31/48 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +7.3 | 5e-11 | 28/48 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +6.3 | 3e-08 | 27/47 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +4.7 | 2e-04 | 24/49 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +4.6 | 3e-04 | 19/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.19× | +4.5 | 4e-04 | 18/48 (KATO III, HepG2/C3A, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.19× | +4.5 | 4e-04 | 19/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.5 | 4e-04 | 16/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.14× | +3.3 | 0.033 | 13/48 (HS-578T, CFPAC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.14× | +3.3 | 0.033 | 16/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.14× | +3.3 | 0.033 | 7/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.033 | 3/48 (LS 180, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -13.2 | 5e-37 | 38/48 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.747×** | -10.9 | 3e-25 | 37/48 (Hs 766T, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -10.0 | 4e-21 | 24/42 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.716×** | -8.8 | 2e-16 | 32/49 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.723×** | -7.9 | 3e-13 | 27/45 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.798×** | -5.6 | 2e-06 | 25/48 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.819×** | -5.3 | 9e-06 | 23/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.827×** | -5.0 | 3e-05 | 23/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.784×** | -3.4 | 0.047 | 11/47 (COLO 205, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.802× | -3.1 | 0.13 | 18/38 (SW 900, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 85.1 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.6) | [[Auranofin (drug)]] 5 µM 0.527× (z -9.9) |
| [[HT-29 (line)]] | alt | 94.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -12.0) |
| [[SW1417 (line)]] | alt | 97.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.518× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 72.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.502× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 57.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.404× (z -12.1) |
| [[LS 180 (line)]] | wt | 71.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.454× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -14.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 50.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 60.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0840× (z -23.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.29× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 46.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 47.4 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.177× (z -8.9) ⚠ cell-cycle shift, explains ~18% of this change |
| [[COLO 205 (line)]] | alt | 79.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.514× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 51.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.309× (z -8.9) |
| [[HOP62 (line)]] | alt | 63.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 86.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.558× (z -11.2) |
| [[KATO III (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -15.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 66.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.352× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 55.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 61.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.467× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 43.0 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0911× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.219× (z -9.1) ⚠ toxic |
| [[RKO (line)]] | wt | 84.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -8.5) |
| [[SHP-77 (line)]] | alt | 62.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -13.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 99.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.429× (z -10.0) |
| [[SNU-423 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.166× (z -10.2) ⚠ toxic |
| [[SW48 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -12.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 76.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.438× (z -14.4) |
| [[A-427 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD7]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[ASH1L]] | +0.57 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[HIVEP1]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[TAPT1]] | +0.53 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[ARID1A]] | +0.53 | +0.34 / +0.46 | both halves | 1e-04 | pathway: ATP-dependent chromatin remodelers |
| [[BAZ1A]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ZNF318]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SRSF4]] | +0.53 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[IRX5]] | +0.52 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[IGIP]] | +0.52 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[AKAP8L]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[UNK]] | +0.52 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD3NL]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[VAMP7]] | -0.56 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[ATP2C1]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[TCP1]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CYB5R4]] | -0.53 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[VDAC2]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[MBOAT2]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PSMB7]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[GPN1]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[FAM91A1]] | -0.50 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[HSP90AA2P]] | -0.50 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[OPA1]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PWWP2A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PWWP2A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.3, -5.9); signed map (20.9, -9.8). **Vector** length 96.8, 21.4% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +11.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +3.7 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +3.2 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +8.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.6 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -13.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.6 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.0 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | PWWP domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:160,061,801-160,119,450 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1935 |
| Gene groups (HGNC) | PWWP domain containing |
| Reactome | 5 pathways, smallest: NuRD complex assembly; CHD3, CHD4, CHD5 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N64](https://www.uniprot.org/uniprotkb/Q96N64) (PWWP domain-containing protein 2A):

> Chromatin-binding protein that acts as an adapter between distinct nucleosome components (H3K36me3 or H2A.Z) and chromatin-modifying complexes, contributing to the regulation of the levels of histone acetylation at actively transcribed genes. Competes with CHD4 and MBD3 for interaction with MTA1 to form a NuRD subcomplex, preventing the formation of full NuRD complex (containing CHD4 and MBD3), leading to recruitment of HDACs to gene promoters resulting in turn in the deacetylation of nearby …

**Summary**, from NCBI Gene [114825](https://www.ncbi.nlm.nih.gov/gene/114825):

> Enables several functions, including NuRD complex binding activity; histone H3K36me3 reader activity; and histone binding activity. Involved in chromatin remodeling. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29406) · Entrez [114825](https://www.ncbi.nlm.nih.gov/gene/114825) · UniProt [Q96N64](https://www.uniprot.org/uniprotkb/Q96N64) · Ensembl [ENSG00000170234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170234)

## Data

Gene col 9917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9917); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9917]; `tensor/DDL_lfc|DDL_z.npy` [9917]; `embed/gene_vectors.npy` [9917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9917 or target_col == 9917). Every well: [[PWWP2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PWWP2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
