---
symbol: "CRYZL1"
type: "gene"
col: 13008
ensembl_id: "ENSG00000205758"
name: "crystallin zeta like 1"
location: "21q22.11"
module: 30
arm: "+"
pooled_cpm: 50.21
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CRYZL1

*crystallin zeta like 1* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.41× (z +6.1, q 6e-07, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.538× (z -16.6, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP14]] (+0.81, fdr 7e-06), [[KLHDC10]] (+0.78, fdr 7e-06), [[FLYWCH1]] (+0.75, fdr 7e-06); moves opposite to [[THOC6]] (-0.72, fdr 7e-06), [[DDX5]] (-0.70, fdr 7e-06), [[MSRA]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NRP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +6.1 | 6e-07 | 34/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.3 | 4e-05 | 28/48 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +5.0 | 1e-04 | 29/48 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 0.001 | 25/48 (KATO III, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 0.002 | 18/48 (LoVo, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.009 | 20/47 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.009 | 22/48 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.027 | 14/48 (SK-MEL-2, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.037 | 23/48 (SHP-77, LoVo, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.045 | 12/49 (PANC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.3 | 0.048 | 13/45 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.088 | 13/49 (HOP62, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -16.6 | 0e+00 | 40/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.554×** | -11.1 | 2e-26 | 42/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.631×** | -8.4 | 1e-14 | 36/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.735×** | -8.2 | 3e-14 | 35/48 (HS-578T, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -7.8 | 9e-13 | 31/44 (A-427, BT-474, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.689×** | -7.0 | 2e-10 | 29/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -6.3 | 3e-08 | 28/47 (CHP-212, A498, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -5.7 | 9e-07 | 2/49 (AN3 CA, SW 1088) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.756×** | -5.3 | 8e-06 | 25/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.769×** | -5.0 | 4e-05 | 28/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.774×** | -4.8 | 7e-05 | 26/48 (NCI-H23, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.794×** | -4.2 | 0.001 | 20/41 (NCI-H1573, C-33 A, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.803×** | -4.2 | 0.001 | 24/48 (NCI-H460, SW 900, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.813×** | -3.9 | 0.004 | 23/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.837× | -3.4 | 0.029 | 16/48 (SW 900, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 96.3 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.319× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 84.9 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.318× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 55.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -15.8) |
| [[A498 (line)]] | wt | 61.4 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.409× (z -10.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.487× (z -8.5) |
| [[C32 (line)]] | wt | 53.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.5) |
| [[HOP62 (line)]] | alt | 56.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.8) |
| [[A549 (line)]] | wt | 45.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.6) |
| [[AN3 CA (line)]] | alt | 56.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 52.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -14.4) |
| [[COLO 205 (line)]] | alt | 43.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.2) |
| [[HCT15 (line)]] | alt | 62.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[HS-578T (line)]] | alt | 57.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.7) |
| [[LoVo (line)]] | wt | 34.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 58.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -10.2) |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.3) |
| [[SW480 (line)]] | alt | 51.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -20.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -12.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[CHP-212 (line)]] | wt | 63.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0498× (z -14.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 54.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -10.9) |
| [[J82 (line)]] | alt | 31.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 66.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.9) |
| [[SNU-1 (line)]] | wt | 61.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.2) |
| [[SNU-423 (line)]] | alt | 46.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP14]] | +0.81 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[FLYWCH1]] | +0.75 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[USP30]] | +0.75 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ABCD4]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[C12orf76]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[FAM193B]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[SPATA7]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.72 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ASB7]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[MGST3]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.72 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[DDX5]] | -0.70 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[MSRA]] | -0.68 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.67 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[TUG1]] | -0.66 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[SKIL]] | -0.65 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.64 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[CYREN]] | -0.64 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[RBM12]] | -0.63 | -0.61 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP1]] | B | NRP1 activity lowers CRYZL1's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.28× higher at baseline in the lines without NRP1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[DUXAP10]] | B | DUXAP10 activity raises CRYZL1's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without DUXAP10 | 0.035 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[PKIG]] | B | PKIG activity raises CRYZL1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without PKIG | 0.046 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[SLC37A2]] | B | SLC37A2 activity raises CRYZL1's level | lines that do not express SLC37A2 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without SLC37A2 | 0.054 | ⚠ within organs, on part of the lines; also absent: FAM111B; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers CRYZL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers CRYZL1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.829). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.0, -12.6); signed map (-33.2, -4.2). **Vector** length 124, 33.8% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -16.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -11.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.9 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | crystallin zeta like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,589,341-33,643,926 (-) |
| Ensembl biotype | protein_coding |
| Also known as | QOH-1, 4P11, Fy-4, FERRY4 |
| Gene groups (HGNC) | FERRY complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [O95825](https://www.uniprot.org/uniprotkb/O95825) (Ferry endosomal RAB5 effector complex subunit 4):

> Component of the FERRY complex (Five-subunit Endosomal Rab5 and RNA/ribosome intermediary). The FERRY complex directly interacts with mRNAs and RAB5A, and functions as a RAB5A effector involved in the localization and the distribution of specific mRNAs most likely by mediating their endosomal transport. The complex recruits mRNAs and ribosomes to early endosomes through direct mRNA-interaction.

**Summary**, from NCBI Gene [9946](https://www.ncbi.nlm.nih.gov/gene/9946):

> This gene encodes a protein that has sequence similarity to zeta crystallin, also known as quinone oxidoreductase. This zeta crystallin-like protein also contains an NAD(P)H binding site. Alternatively spliced transcript variants have been observed but their full-length nature has not been completely determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2420) · Entrez [9946](https://www.ncbi.nlm.nih.gov/gene/9946) · UniProt [O95825](https://www.uniprot.org/uniprotkb/O95825) · Ensembl [ENSG00000205758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205758)

## Data

Gene col 13008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13008); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13008]; `tensor/DDL_lfc|DDL_z.npy` [13008]; `embed/gene_vectors.npy` [13008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13008 or target_col == 13008). Every well: [[CRYZL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYZL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
