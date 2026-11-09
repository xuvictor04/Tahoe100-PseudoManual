---
symbol: "ALG9"
type: "gene"
col: 1474
ensembl_id: "ENSG00000086848"
name: "ALG9 alpha-1,2-mannosyltransferase"
location: "11q23.1"
module: 65
arm: "+"
pooled_cpm: 46.95
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ALG9

*ALG9 alpha-1,2-mannosyltransferase* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.21× (z +6.3, q 1e-07, up in 33 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.463× (z -15.3, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRMT9]] (+0.77, fdr 7e-06), [[FAM168A]] (+0.76, fdr 7e-06), [[PMS2P3]] (+0.75, fdr 7e-06); moves opposite to [[TUT7]] (-0.70, fdr 7e-06), [[SKIL]] (-0.67, fdr 1e-05), [[SSUH2]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +6.3 | 1e-07 | 33/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.025 | 22/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.099 | 18/48 (NCI-H2030, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +3.4 | 0.099 | 12/48 (SHP-77, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.463×** | -15.3 | 0e+00 | 40/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -13.0 | 5e-36 | 36/40 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.440×** | -12.5 | 2e-33 | 42/47 (H4, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.521×** | -9.9 | 4e-21 | 36/48 (HCT15, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.549×** | -9.1 | 8e-18 | 43/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -7.5 | 8e-12 | 32/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -7.0 | 2e-10 | 35/47 (NCI-H2347, BT-474, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.614×** | -6.9 | 5e-10 | 30/43 (A-172, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -5.5 | 2e-06 | 23/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.799×** | -4.5 | 4e-04 | 19/48 (NCI-H2347, CHP-212, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.747×** | -4.3 | 0.001 | 27/49 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.757×** | -4.2 | 0.001 | 21/48 (HS-578T, HOP62, …) | two highest doses |  |
| [[Thymol (drug)]] 5 µM |  | **0.819×** | -3.9 | 0.004 | 19/48 (SNU-1, PANC-1, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.775×** | -3.9 | 0.005 | 23/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.783×** | -3.7 | 0.008 | 20/48 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.787×** | -3.6 | 0.010 | 20/48 (LS 180, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.802×** | -3.3 | 0.026 | 16/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.802×** | -3.3 | 0.026 | 19/48 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.824×** | -2.9 | 0.079 | 11/47 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.824×** | -2.9 | 0.079 | 11/48 (A549, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 77.0 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.2) |
| [[AN3 CA (line)]] | alt | 81.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 33.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.0) |
| [[H4 (line)]] | wt | 51.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0654× (z -21.5) |
| [[HOP62 (line)]] | alt | 38.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -24.8) |
| [[RPMI-7951 (line)]] | alt | 58.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.6) |
| [[A-172 (line)]] | wt | 27.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0767× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 52.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 64.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -19.2) |
| [[Hs 766T (line)]] | wt | 59.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.303× (z -11.8) |
| [[HS-578T (line)]] | alt | 65.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 60.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.443× (z -8.9) |
| [[PANC-1 (line)]] | alt | 61.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.470× (z -9.2) |
| [[SNU-423 (line)]] | alt | 44.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.7) |
| [[SW480 (line)]] | alt | 47.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.485× (z -8.6) |
| [[C32 (line)]] | wt | 35.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.1) |
| [[HCT15 (line)]] | alt | 56.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0351× (z -24.9) |
| [[HEC-1-A (line)]] | alt | 49.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.313× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 45.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 56.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 40.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.6) |
| [[SNU-1 (line)]] | wt | 80.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.4) |
| [[SW 900 (line)]] | alt | 34.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -12.7) |
| [[SW1417 (line)]] | alt | 71.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.3) |
| [[BT-474 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -9.7) ⚠ toxic |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.129× (z -9.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.5) |
| [[J82 (line)]] | alt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.5) |
| [[KATO III (line)]] | alt | 63.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.8) |
| [[LS 180 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0885× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 65.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -12.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT9]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[FAM168A]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[PMS2P3]] | +0.75 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.74 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[LRIG2]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[SNX4]] | +0.74 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.73 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[TRIT1]] | +0.73 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[MMS19]] | +0.72 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[COPS4]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[KCTD6]] | +0.71 | +0.71 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | -0.70 | -0.61 / -0.77 | both halves | 7e-06 |  |
| [[SKIL]] | -0.67 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[SSUH2]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[DDX5]] | -0.62 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.62 | -0.71 / -0.46 | both halves | 2e-05 |  |
| [[ANKLE2]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises ALG9's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.52× lower at baseline in the lines without KATNAL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[TOP2A]] | B | TOP2A activity raises ALG9's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HACE1]] | C | HACE1 activity raises ALG9's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.66× lower at baseline in the lines without HACE1 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |
| [[PLEKHA2]] | C | PLEKHA2 activity lowers ALG9's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 1.84× higher at baseline in the lines without PLEKHA2 | 0.091 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.867). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.8, -12.0); signed map (-32.6, -10.3). **Vector** length 110, 30.8% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | +4.3 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -1.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -9.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.4 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ALG9 alpha-1,2-mannosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:111,782,195-111,871,581 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DIBD1 |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6U8](https://www.uniprot.org/uniprotkb/Q9H6U8) (Alpha-1,2-mannosyltransferase ALG9):

> Mannosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including two GlcNAcs, nine mannoses and three …

**Summary**, from NCBI Gene [79796](https://www.ncbi.nlm.nih.gov/gene/79796):

> This gene encodes an alpha-1,2-mannosyltransferase enzyme that functions in lipid-linked oligosaccharide assembly. Mutations in this gene result in congenital disorder of glycosylation type Il. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:15672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15672) · Entrez [79796](https://www.ncbi.nlm.nih.gov/gene/79796) · UniProt [Q9H6U8](https://www.uniprot.org/uniprotkb/Q9H6U8) · Ensembl [ENSG00000086848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086848)

## Data

Gene col 1474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1474); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1474]; `tensor/DDL_lfc|DDL_z.npy` [1474]; `embed/gene_vectors.npy` [1474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1474 or target_col == 1474). Every well: [[ALG9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
