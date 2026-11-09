---
symbol: "VPS26B"
type: "gene"
col: 7531
ensembl_id: "ENSG00000151502"
name: "VPS26 retromer complex component B"
location: "11q25"
module: 57
arm: "+"
pooled_cpm: 17.86
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# VPS26B

*VPS26 retromer complex component B* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.59× (z +9.3, q 6e-18, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.536× (z -17.9, q 0e+00, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM183A]] (+0.69, fdr 7e-06), [[PAPSS1]] (+0.65, fdr 7e-06), [[C2CD2L]] (+0.65, fdr 8e-06); moves opposite to [[HDAC9]] (-0.60, fdr 1e-05), [[PLA2G4C]] (-0.58, fdr 4e-05), [[C12orf50]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7531.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +9.3 | 6e-18 | 30/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.9 | 2e-16 | 17/31 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +8.8 | 3e-16 | 30/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +7.7 | 1e-12 | 28/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 4e-10 | 27/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +6.4 | 2e-08 | 19/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +6.3 | 2e-08 | 25/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.8 | 1e-04 | 20/41 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.27×** | +4.6 | 3e-04 | 18/47 (SW1417, SW 900, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.16× | +4.3 | 1e-03 | 14/48 (SW480, SW1417, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.3 | 0.001 | 8/48 (KATO III, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 15/45 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.002 | 6/48 (CFPAC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.014 | 8/46 (NCI-H1573, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.6 | 0.014 | 6/48 (NCI-H1792, HT-29, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.016 | 7/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.022 | 8/47 (A549, KATO III, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.028 | 10/45 (LS 180, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.033 | 3/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.536×** | -17.9 | 0e+00 | 29/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -11.9 | 4e-30 | 39/48 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -11.2 | 1e-26 | 32/46 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -11.1 | 1e-26 | 33/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.621×** | -9.3 | 2e-18 | 30/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -8.8 | 1e-16 | 30/47 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.654×** | -8.6 | 6e-16 | 27/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -8.0 | 1e-13 | 29/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -5.2 | 1e-05 | 15/47 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.780×** | -5.1 | 2e-05 | 19/47 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -5.0 | 3e-05 | 22/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -4.6 | 2e-04 | 16/48 (Hs 766T, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.876× | -3.8 | 0.006 | 15/48 (KATO III, SW 1088, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.833×** | -3.7 | 0.008 | 15/47 (HT-29, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.827×** | -3.6 | 0.014 | 15/47 (A549, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.034 | 11/46 (SNU-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -19.1) |
| [[A549 (line)]] | wt | 14.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.6) |
| [[PANC-1 (line)]] | alt | 34.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -20.0) |
| [[LOX-IMVI (line)]] | wt | 22.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.0) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -8.9) |
| [[H4 (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 9.71 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.111× (z -9.0) |
| [[HT-29 (line)]] | alt | 26.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.339× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -10.0) |
| [[J82 (line)]] | alt | 9.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -13.5) |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -8.7) |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.1) |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM183A]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PAPSS1]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[C2CD2L]] | +0.65 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[UBAC1]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[QARS1]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SPAST]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SKP2]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[GPD1L]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SETD3]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RAB4A]] | +0.62 | +0.65 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC9]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[PLA2G4C]] | -0.58 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[C12orf50]] | -0.57 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SLC9A8]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[LINC02516]] | -0.55 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[HDX]] | -0.54 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SSUH2]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[RAB30-DT]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[KMO]] | -0.54 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[XIAP]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[LINC00486]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PBDC1]] | -0.53 | -0.39 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers VPS26B's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.51× higher at baseline in the lines without ZNF341-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.7, -13.8); signed map (-36.9, -13.7). **Vector** length 81.4, 15.5% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +8.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -17.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -5.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | VPS26 retromer complex component B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:134,224,671-134,247,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10485, Pep8b |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0F5](https://www.uniprot.org/uniprotkb/Q4G0F5) (Vacuolar protein sorting-associated protein 26B):

> Acts as a component of the retromer cargo-selective complex (CSC). The CSC is believed to be the core functional component of retromer or respective retromer complex variants acting to prevent missorting of selected transmembrane cargo proteins into the lysosomal degradation pathway. The recruitment of the CSC to the endosomal membrane involves RAB7A and SNX3. The SNX-BAR retromer mediates retrograde transport of cargo proteins from endosomes to the trans-Golgi network (TGN) and is involved in …

**Summary**, from NCBI Gene [112936](https://www.ncbi.nlm.nih.gov/gene/112936):

> Predicted to be involved in intracellular protein transport and retrograde transport, endosome to Golgi. Predicted to act upstream of or within cellular response to type II interferon. Predicted to be located in early endosome and late endosome. Predicted to be part of retromer, cargo-selective complex. Predicted to be active in endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28119) · Entrez [112936](https://www.ncbi.nlm.nih.gov/gene/112936) · UniProt [Q4G0F5](https://www.uniprot.org/uniprotkb/Q4G0F5) · Ensembl [ENSG00000151502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151502)

## Data

Gene col 7531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7531); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7531]; `tensor/DDL_lfc|DDL_z.npy` [7531]; `embed/gene_vectors.npy` [7531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7531 or target_col == 7531). Every well: [[VPS26B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS26B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
